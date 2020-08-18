from Code.constants import *


price_paid_headers = ['tid', 'price', 'date', 'postcode', 'property_type', 'old_new', 'duration', 'paon', 'saon',
                      'street', 'locality', 'city', 'district', 'county', 'ppd_type', 'status']

columns_to_drop = ['tid', 'paon', 'saon', 'street', 'locality', 'city', 'postcode', 'status', 'ppd_type']


def combine_price_parts(file_1, file_2):
    """
    A function that combines two price data files.
    :param file_1: The first file.
    :param file_2: The second file.
    :return: None.
    """
    df_1 = pd.read_csv(os.path.join(ORIGINAL_PRICE_DATA_PATH, file_1), index_col='Unnamed: 0')
    df_2 = pd.read_csv(os.path.join(ORIGINAL_PRICE_DATA_PATH, file_2), index_col='Unnamed: 0')
    new_df = pd.concat([df_1, df_2], ignore_index=True)
    new_df.index.rename('id', inplace=True)
    new_df.to_csv(os.path.join(PRICE_DATA_PATH, file_1[:-10] + '.csv'))


def add_headers(file_name, path, headers):
    """
    A function that add headers to a file.
    :param file_name: The file name to add headers to.
    :param path: The file path.
    :param headers: The list of headers to add.
    :return: None.
    """
    df = pd.read_csv(os.path.join(path, file_name), header=None)
    df.columns = headers
    df.to_csv(os.path.join(path, file_name))


def fix_index_col(file_name):
    """
    A function that sets/resets the index column to be 'id'.
    :param file_name: The name of the file to reset the index of.
    :return: None.
    """
    df = pd.read_csv(os.path.join(PRICE_DATA_PATH, file_name), index_col='Unnamed: 0')
    df.index.rename('id', inplace=True)
    df.to_csv(os.path.join(PRICE_DATA_PATH, file_name))


def fill_missing_districts(df):
    """
    A function that fills in missing district values based on the city values.
    :param df: The dataframe to fill in the missing values.
    :return: The dataframe.
    """
    for i in range(len(df)):
        if pd.isna(df['district'][i]):
            df_city = df.loc[df['city'] == df['city'][i]]
            df['district'][i] = df_city['district'].mode().values[0]
    return df


def drop_unnecessary_columns(year):
    """
    A function that drops unnecessary columns in the dataframe representing a given year.
    :param year: The year whose data should be 'cleansed'.
    :return: None.
    """
    # df_yr = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')
    df_yr = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)), index_col='id')

    df_yr.drop(columns_to_drop, axis=1, inplace=True)
    # df_yr.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)))
    df_yr.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)))


def drop_all_unnecessary_columns():
    """
    A function that calls drop_unnecessary_columns for each of the years.
    :return: None.
    """
    for yr in range(1999, 2019):
        drop_unnecessary_columns(yr)


def preprocess_price_df(df):
    """
    A function that performs some preprocessing functions on a given price dataframe, including transforming the text to
    be uniformly lowercase and replacing old names with new ones.
    :param df: The dataframe.
    :return: The dataframe.
    """
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
    """
    A function that adds the number of days before/after brexit to each home sale.
    :param df: The dataframe to add to.
    :return: The dataframe.
    """
    from_brexit = []
    for i in range(len(df)):
        from_brexit.append((date(*list(map(int, df['date'].loc[i].split(' ')[0].split('-')))) - date(2016, 6, 24)).days)
    df['brexit'] = from_brexit
    return df


def convert_to_binary(year, columns, values_to_one):
    """
    A function that converts given columns to binary, using the provided info as to which value should become 1, for the
    home prices of a given year.
    :param year: The year to perform this on.
    :param columns: The columns to convert to binary.
    :param values_to_one: The values for each column to become 1.
    :return: None.
    """
    # df = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')
    df = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)), index_col='id')

    for col, val in zip(columns, values_to_one):
        df.loc[df[col] != val, col] = 0
        df.loc[df[col] == val, col] = 1
    # df.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)))
    df.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)))


def convert_columns_to_binary(columns, values_to_one):
    """
    A function that calls convert_to_binary for each of the years.
    :param columns: The columns to convert to binary.
    :param values_to_one: The values for each column to become 1.
    :return: None.
    """
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
