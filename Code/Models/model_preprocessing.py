from Code.constants import *
from Code.Models.model_helpers import *


def get_preprocessed_df(year):
    # return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')
    # return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)), index_col='id')

    return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-city-{}.csv'.format(year)), index_col='id')


def convert_categorical_to_binaries(df, column, values_to_drop=()):
    for val in values_to_drop:
        df = df[df[column] != val].reset_index(drop=True)
    df.index.rename('id', inplace=True)
    df = pd.get_dummies(df, columns=[column])
    return df


def convert_property_type_to_discrete(df):
    df = df[df['property_type'] != 'O'].reset_index(drop=True)
    df.index.rename('id', inplace=True)
    value_map = {'D': 4, 'S': 3, 'T': 2, 'F': 1}
    df['property_type'].replace(value_map, inplace=True)
    return df


def convert_time_to_month_year(df):
    df['year'] = df['date'].apply(lambda x: pd.Timestamp(x).year)
    df['date'] = df['date'].apply(lambda x: pd.Timestamp(x).month)
    df.rename(columns={'date': 'month'}, inplace=True)
    return df


def model_preprocess_yr(year, binary=True):
    df_yr = get_preprocessed_df(year)
    df_yr = convert_time_to_month_year(df_yr)
    if binary:
        df_yr = convert_categorical_to_binaries(df_yr, 'property_type', ['O'])
    else:
        df_yr = convert_property_type_to_discrete(df_yr)
    df_yr = convert_categorical_to_binaries(df_yr, 'region')
    df_yr = convert_categorical_to_binaries(df_yr, 'county')
    df_yr = convert_categorical_to_binaries(df_yr, 'district')

    df_yr = convert_categorical_to_binaries(df_yr, 'city')

    return df_yr


def model_bin_preprocess_all():
    for yr in range(1999, 2019):
        df_yr = model_preprocess_yr(yr)
        # df_yr.to_csv(os.path.join(MODEL_BIN_DATA_PATH, 'm_b-preprocessed-{}.csv'.format(yr)))
        df_yr.to_csv(os.path.join(MODEL_BIN_DATA_PATH_A, 'm_b-preprocessed-{}.csv'.format(yr)))


def model_dis_preprocess_all():
    for yr in range(1999, 2019):
        df_yr = model_preprocess_yr(yr, binary=False)
        # df_yr.to_csv(os.path.join(MODEL_DIS_DATA_PATH, 'm_d-preprocessed-{}.csv'.format(yr)))
        df_yr.to_csv(os.path.join(MODEL_DIS_DATA_PATH_A, 'm_d-preprocessed-{}.csv'.format(yr)))


# model_bin_preprocess_all()
# model_dis_preprocess_all()


def split_year_to_train_test(year, frac=0.2, binary=False):
    print(year, binary)
    df_yr = get_df_year(year, binary)
    df_indices = list(df_yr.index)
    np.random.shuffle(df_indices)
    train_indices = df_indices[:round((1 - frac) * len(df_indices))]
    test_indices = df_indices[round((1 - frac) * len(df_indices)):]
    train_df = df_yr.loc[train_indices]
    test_df = df_yr.loc[test_indices]
    if binary:
        train_df.to_csv(os.path.join(MODEL_BIN_TRAIN_A, 'train-b-{}.csv'.format(year)))
        test_df.to_csv(os.path.join(MODEL_BIN_TEST_A, 'test-b-{}.csv'.format(year)))
    else:
        train_df.to_csv(os.path.join(MODEL_DIS_TRAIN_A, 'train-d-{}.csv'.format(year)))
        test_df.to_csv(os.path.join(MODEL_DIS_TEST_A, 'test-d-{}.csv'.format(year)))


def split_to_train_test_all_years():
    for yr in range(1999, 2019):
        split_year_to_train_test(yr)
        split_year_to_train_test(yr, binary=True)


# split_to_train_test_all_years()




len_yrs = {1999: 1194146, 2000: 1128619, 2001: 1245137, 2002: 1351018, 2003: 1234779, 2004: 1231248, 2005: 1060845,
           2006: 1325380, 2007: 1271682, 2008: 649287, 2009: 624954, 2010: 662942, 2011: 660773, 2012: 668332,
           2013: 806155, 2014: 971371, 2015: 990175, 2016: 999673, 2017: 989681, 2018: 962579}
cum_years = {1999: len_yrs[1999]}
for yr in range(2000, 2019):
    cum_years[yr] = cum_years[yr - 1] + len_yrs[yr]


def index_mapper(ind):
    for yr in range(1999, 2019):
        if ind < cum_years[yr]:
            return yr


def split_data_to_train_test(test_size=0.1, num_batches=10):
    mixed_indices = np.arange(sum(len_yrs.values()))
    np.random.shuffle(mixed_indices)
    train_indices = mixed_indices[:round((1 - test_size) * len(mixed_indices))]
    test_indices = mixed_indices[round((1 - test_size) * len(mixed_indices)):]
    train_batches = {}
    for i in range(num_batches):
        train_batches[i] = sorted(train_indices[round((i / num_batches) * len(train_indices)): round(((i + 1) / num_batches) * len(train_indices))])
    indices = {'train': train_batches, 'test': test_indices}
    indices_fname = 'indices.p'
    indices_file = open(indices_fname, 'wb')
    pickle.dump(indices, indices_file)
    indices_file.close()


def put_batches_into_files(batch_num, batch_idx):
    df_yr = get_df_year(1999)
    batch_yr = df_yr.loc[batch_idx]
    batch_indices = [i - cum_years[1999] for i in batch_idx if i - cum_years[1999] > 0]
    for yr in range(2000, 2019):
        print(yr)
        df_yr = get_df_year(yr)
        batch_yr_indices = [i for i in batch_indices if i < cum_years[yr]]
        batch_yr = pd.concat([batch_yr, df_yr.loc[batch_yr_indices]], ignore_index=True)
        batch_indices = [i - cum_years[yr] for i in batch_indices if i - cum_years[yr] > 0]
    batch_yr.to_csv(os.path.join(ALT_DATA_PATH, 'batch-{}.csv'.format(batch_num)))


# split_data_to_train_test()
#
# indices_fname = 'indices.p'
# indices_file = open(indices_fname, 'rb')
# ind = pickle.load(indices_file)
# indices_file.close()
# tr = ind['train']
# ts = ind['test']
# print(len(tr), len(ts), len(tr[0]))
#
# put_batches_into_files(0, tr[0])
