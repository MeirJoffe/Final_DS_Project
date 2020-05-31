from Code.constants import *


price_paid_headers = ['tid', 'price', 'date', 'postcode', 'property_type', 'old_new', 'duration', 'paon', 'saon',
                      'street', 'locality', 'city', 'district', 'county', 'ppd_type', 'status']

columns_to_drop = ['tid', 'paon', 'saon', 'street', 'locality', 'city', 'postcode', 'status', 'ppd_type']


def combine_price_parts(file_1, file_2):
    df_1 = pd.read_csv(os.path.join(ORIGINAL_PRICE_DATA_PATH, file_1), index_col='Unnamed: 0')
    df_2 = pd.read_csv(os.path.join(ORIGINAL_PRICE_DATA_PATH, file_2), index_col='Unnamed: 0')
    new_df = pd.concat([df_1, df_2], ignore_index=True)
    new_df.index.rename('id', inplace=True)
    new_df.to_csv(os.path.join(PRICE_DATA_PATH, file_1[:-10] + '.csv'))


def add_headers(file_name, path, headers):
    df = pd.read_csv(os.path.join(path, file_name), header=None)
    df.columns = headers
    df.to_csv(os.path.join(path, file_name))


def fix_index_col(file_name):
    df = pd.read_csv(os.path.join(PRICE_DATA_PATH, file_name), index_col='Unnamed: 0')
    df.index.rename('id', inplace=True)
    df.to_csv(os.path.join(PRICE_DATA_PATH, file_name))


def fill_missing_districts(df):
    for i in range(len(df)):
        if pd.isna(df['district'][i]):
            df_city = df.loc[df['city'] == df['city'][i]]
            df['district'][i] = df_city['district'].mode().values[0]
    return df


def drop_unnecessary_columns(year):
    # df_yr = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')
    df_yr = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)), index_col='id')
    df_yr.drop(columns_to_drop, axis=1, inplace=True)
    # df_yr.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)))
    df_yr.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)))


def drop_all_unnecessary_columns():
    for yr in range(1999, 2019):
        drop_unnecessary_columns(yr)


def preprocess_price_df(df):
    df['district'] = df['district'].str.lower().str.strip()
    df['county'] = df['county'].str.lower().str.strip()
    for i in range(len(df)):
        if df['district'][i] in district_changes:
            df['district'][i] = district_changes[df['district'][i]]
        if df['county'][i] in county_changes:
            df['county'][i] = county_changes[df['county'][i]]
        if df['district'][i] == 'city of london':
            df['county'][i] = 'city of london'
    return df


def add_time_from_brexit(df):
    from_brexit = []
    for i in range(len(df)):
        from_brexit.append((date(*list(map(int, df['date'].loc[i].split(' ')[0].split('-')))) - date(2016, 6, 24)).days)
    df['brexit'] = from_brexit
    return df


def convert_to_binary(year, columns, values_to_one):
    # df = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')
    df = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)), index_col='id')
    for col, val in zip(columns, values_to_one):
        df.loc[df[col] != val, col] = 0
        df.loc[df[col] == val, col] = 1
    # df.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)))
    df.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)))


def convert_columns_to_binary(columns, values_to_one):
    for yr in range(1999, 2019):
        convert_to_binary(yr, columns, values_to_one)


# # Add headers to each of the pricing data files.
# for i in range(2013, 2019):
#     add_headers('pp-{}.csv'.format(i), PRICE_DATA_PATH, price_paid_headers)
# for j in range(1999, 2013):
#     add_headers('pp-{}-part1.csv'.format(j), ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
#     add_headers('pp-{}-part2.csv'.format(j), ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
#
# # Combine files that each represent only half of the year's data
# for k in range(1999, 2013):
#     combine_price_parts('pp-{}-part1.csv'.format(k), 'pp-{}-part2.csv'.format(k))
#
# # Set the index column
# for l in range(2013, 2019):
#     fix_index_col('pp-{}.csv'.format(l))
