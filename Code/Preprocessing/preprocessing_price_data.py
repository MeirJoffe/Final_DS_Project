from Code.constants import *

price_paid_headers = ['tid', 'price', 'date', 'postcode', 'property_type', 'old_new', 'duration', 'paon', 'saon',
                      'street', 'locality', 'city', 'district', 'county', 'ppd_type', 'status']


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


# Add headers to each of the pricing data files.
for i in range(2013, 2019):
    add_headers('pp-{}.csv'.format(i), PRICE_DATA_PATH, price_paid_headers)
for j in range(1999, 2013):
    add_headers('pp-{}-part1.csv'.format(j), ORIGINAL_PRICE_DATA_PATH, price_paid_headers)
    add_headers('pp-{}-part2.csv'.format(j), ORIGINAL_PRICE_DATA_PATH, price_paid_headers)

# Combine files that each represent only half of the year's data
for k in range(1999, 2013):
    combine_price_parts('pp-{}-part1.csv'.format(k), 'pp-{}-part2.csv'.format(k))

# Set the index column
for l in range(2013, 2019):
    fix_index_col('pp-{}.csv'.format(l))