from Code.constants import *


def get_df_year(yr, binary=False):
    if binary:
        # return pd.read_csv(os.path.join(MODEL_BIN_DATA_PATH, 'm_b-preprocessed-{}.csv'.format(yr)), index_col='id')
        return pd.read_csv(os.path.join(MODEL_BIN_DATA_PATH_A, 'm_b-preprocessed-{}.csv'.format(yr)), index_col='id')
    else:
        # return pd.read_csv(os.path.join(MODEL_DIS_DATA_PATH, 'm_d-preprocessed-{}.csv'.format(yr)), index_col='id')
        return pd.read_csv(os.path.join(MODEL_DIS_DATA_PATH_A, 'm_d-preprocessed-{}.csv'.format(yr)), index_col='id')


def get_model_dis_train_df(year):
    return pd.read_csv(os.path.join(MODEL_DIS_TRAIN_A, 'train-d-{}.csv'.format(year)), index_col='id')


def get_model_dis_test_df(year):
    return pd.read_csv(os.path.join(MODEL_DIS_TEST_A, 'test-d-{}.csv'.format(year)), index_col='id')


def get_model_bin_train_df(year):
    return pd.read_csv(os.path.join(MODEL_BIN_TRAIN_A, 'train-b-{}.csv'.format(year)), index_col='id')


def get_model_bin_test_df(year):
    return pd.read_csv(os.path.join(MODEL_BIN_TEST_A, 'test-b-{}.csv'.format(year)), index_col='id')


def model_get_preprocessed_train_test(year, binary=False, add_intercept=False):
    if binary:
        df_yr_tr = get_model_bin_train_df(year)
        df_yr_ts = get_model_bin_test_df(year)
    else:
        df_yr_tr = get_model_dis_train_df(year)
        df_yr_ts = get_model_dis_test_df(year)

    # df_yr_tr = df_yr_tr[df_yr_tr['region_london'] == 0]
    # df_yr_ts = df_yr_ts[df_yr_ts['region_london'] == 0]

    y_tr = df_yr_tr['price'].values
    y_tr = np.reshape(y_tr, (y_tr.shape[0], 1))
    df_yr_tr.drop('price', axis=1, inplace=True)
    y_ts = df_yr_ts['price'].values
    y_ts = np.reshape(y_ts, (y_ts.shape[0], 1))
    df_yr_ts.drop('price', axis=1, inplace=True)
    if add_intercept:
        df_yr_tr = np.c_[np.ones(df_yr_tr.shape[0]), df_yr_tr.values]
        df_yr_ts = np.c_[np.ones(df_yr_ts.shape[0]), df_yr_ts.values]
    return df_yr_tr, y_tr, df_yr_ts, y_ts


def create_mini_batches(X, y, batch_size, shuffle_data=False):
    batches = []
    batch_full_data = np.hstack((X, y))
    if shuffle_data:
        np.random.shuffle(batch_full_data)
    num_batches = X.shape[0] // batch_size
    for i in range(num_batches + 1):
        mini_batch = batch_full_data[i * batch_size:(i + 1) * batch_size, :]
        batch_X = mini_batch[:, :-1]
        batch_y = mini_batch[:, -1].reshape((-1, 1))
        batches.append((batch_X, batch_y))
    return batches


def create_mini_batches_X_only(X, batch_size):
    batches = []
    # np.random.shuffle(X)
    num_batches = X.shape[0] // batch_size
    for i in range(num_batches + 1):
        mini_batch = X[i * batch_size:(i + 1) * batch_size, :]
        batch_X = mini_batch[:, :-1]
        batches.append(batch_X)
    return batches


def bootstrap(model, df, n_iters=10000, batch_size=1000):
    thetas = {}
    for i in range(n_iters):
        model_i = model()
        # model.train(X)
