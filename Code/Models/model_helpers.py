from Code.constants import *


def get_df_year(yr, binary=False):
    """
    A function that returns the preprocessed data for a given year.
    :param yr: The year to return the data for.
    :param binary: A boolean whether the preprocessed data's property_type column is a discrete column of 4 binary
    columns.
    :return: The dataframe.
    """
    if binary:
        # return pd.read_csv(os.path.join(MODEL_BIN_DATA_PATH, 'm_b-preprocessed-{}.csv'.format(yr)), index_col='id')
        return pd.read_csv(os.path.join(MODEL_BIN_DATA_PATH_A, 'm_b-preprocessed-{}.csv'.format(yr)), index_col='id')
    else:
        # return pd.read_csv(os.path.join(MODEL_DIS_DATA_PATH, 'm_d-preprocessed-{}.csv'.format(yr)), index_col='id')
        return pd.read_csv(os.path.join(MODEL_DIS_DATA_PATH_A, 'm_d-preprocessed-{}.csv'.format(yr)), index_col='id')


def get_model_dis_train_df(year):
    """
    A function that returns the preprocessed training data for a given year (after train-test split).
    :param yr: The year to return the data for.
    :param binary: A boolean whether the preprocessed data's property_type column is a discrete column of 4 binary
    columns.
    :return: The dataframe.
    """
    return pd.read_csv(os.path.join(MODEL_DIS_TRAIN_A, 'train-d-{}.csv'.format(year)), index_col='id')


def get_model_dis_test_df(year):
    """
    A function that returns the preprocessed test data for a given year (after train-test split).
    :param yr: The year to return the data for.
    :param binary: A boolean whether the preprocessed data's property_type column is a discrete column of 4 binary
    columns.
    :return: The dataframe.
    """
    return pd.read_csv(os.path.join(MODEL_DIS_TEST_A, 'test-d-{}.csv'.format(year)), index_col='id')


def get_model_bin_train_df(year):
    """
    A function that returns the preprocessed training data for a given year (after train-test split).
    :param yr: The year to return the data for.
    :param binary: A boolean whether the preprocessed data's property_type column is a discrete column of 4 binary
    columns.
    :return: The dataframe.
    """
    return pd.read_csv(os.path.join(MODEL_BIN_TRAIN_A, 'train-b-{}.csv'.format(year)), index_col='id')


def get_model_bin_test_df(year):
    """
    A function that returns the preprocessed test data for a given year (after train-test split).
    :param yr: The year to return the data for.
    :param binary: A boolean whether the preprocessed data's property_type column is a discrete column of 4 binary
    columns.
    :return: The dataframe.
    """
    return pd.read_csv(os.path.join(MODEL_BIN_TEST_A, 'test-b-{}.csv'.format(year)), index_col='id')


def get_model_bin_all_df(part):
    """
    A function that returns the preprocessed data for a given part number (after randomly splitting the data into n=20
    parts) for data where the property_type column has been transformed into 4 binary columns.
    :param part: The number part to return the data for.
    :return: The dataframe.
    """
    return pd.read_csv(os.path.join(MODEL_BIN_COMB_A, 'm_b-preprocessed-part-{}.csv'.format(part)), index_col='id')


def get_model_dis_all_df(part):
    """
    A function that returns the preprocessed data for a given part number (after randomly splitting the data into n=20
    parts) for data where the property_type column has been transformed into a discrete column.
    :param part: The number part to return the data for.
    :return: The dataframe.
    """
    return pd.read_csv(os.path.join(MODEL_DIS_COMB_A, 'm_d-preprocessed-part-{}.csv'.format(part)), index_col='id')


def model_get_preprocessed_train_test_by_year(year, binary=False, add_intercept=False):
    """
    A function that returns the preprocessed train and test data of a given year split to X and y (each).
    :param year: The year to return the data for.
    :param binary: A boolean whether the preprocessed data's property_type column is a discrete column of 4 binary
    columns.
    :param add_intercept: A boolean whether to add a column of 1 (all values equal 1) to represent the intercept (in
    case of a SGD model).
    :return: The train and test data, split into X and y.
    """
    if binary:
        df_yr_tr = get_model_bin_train_df(year)
        df_yr_ts = get_model_bin_test_df(year)
    else:
        df_yr_tr = get_model_dis_train_df(year)
        df_yr_ts = get_model_dis_test_df(year)

    df_keys = list(df_yr_tr.keys())
    df_keys = [i for i in df_keys if i != 'price']

    y_tr = df_yr_tr['price'].values
    y_tr = np.reshape(y_tr, (y_tr.shape[0], 1))
    df_yr_tr.drop('price', axis=1, inplace=True)
    y_ts = df_yr_ts['price'].values
    y_ts = np.reshape(y_ts, (y_ts.shape[0], 1))
    df_yr_ts.drop('price', axis=1, inplace=True)
    if add_intercept:
        df_yr_tr = np.c_[np.ones(df_yr_tr.shape[0]), df_yr_tr.values]
        df_yr_ts = np.c_[np.ones(df_yr_ts.shape[0]), df_yr_ts.values]
    return df_yr_tr, y_tr, df_yr_ts, y_ts, df_keys


def model_get_preprocessed_all_years(part, binary=False, add_intercept=False):
    """
    A function that returns the preprocessed data of a given part number (after randomly splitting the data into n=20
    parts) split to X and y.
    :param part: The number of the part to return the data for.
    :param binary: A boolean whether the preprocessed data's property_type column is a discrete column of 4 binary
    columns.
    :param add_intercept: A boolean whether to add a column of 1 (all values equal 1) to represent the intercept (in
    case of a SGD model).
    :return: The part's data, split into X and y.
    """
    if binary:
        df = get_model_bin_all_df(part)
    else:
        df = get_model_dis_all_df(part)

    df_keys = list(df.keys())
    df_keys = [i for i in df_keys if i != 'price']

    y_tr = df['price'].values
    y_tr = np.reshape(y_tr, (y_tr.shape[0], 1))
    df.drop('price', axis=1, inplace=True)
    if add_intercept:
        df = np.c_[np.ones(df.shape[0]), df.values]
    return df, y_tr, df_keys


def create_mini_batches(X, y, batch_size, shuffle_data=False):
    """
    A function that receives a data matrix and a labels vector (X and y) and separates them into mini-batches.
    :param X: The data matrix.
    :param y: The labels vector.
    :param batch_size: The size of each batch (except perhaps the last one which may be smaller).
    :param shuffle_data: A boolean whether to shuffle the data before splitting it into batches.
    :return: The batches.
    """
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
    """
    A function that receives a data matrix (X) and separates them into mini-batches.
    :param X: The data matrix.
    :param batch_size: The size of each batch (except perhaps the last one which may be smaller).
    :return: The batches.
    """
    batches = []
    num_batches = X.shape[0] // batch_size
    for i in range(num_batches + 1):
        mini_batch = X[i * batch_size:(i + 1) * batch_size, :]
        batch_X = mini_batch[:, :-1]
        batches.append(batch_X)
    return batches


def bootstrap(model, df, year, n_iters=20, binary=False, acc=0.9):
    """
    A function that performs bootstrapping (for regression) in order to provide a confidence interval for the values of
    the learned weight vector (theta).
    :param model: The model the train on (assumed to be SGDRegression).
    :param df: The data to perform the bootstrapping for.
    :param year: The year this data represents.
    :param n_iters: The number of iterations to train the model for bootstrapping purposes.
    :param binary: A boolean whether the preprocessed data's property_type column is a discrete column of 4 binary
    columns.
    :param acc: The level of confidence we want to provide, i.e. which values to choose to be the threshold for the
    theta values.
    :return: None.
    """
    thetas = []
    to_save = []
    for i in range(n_iters):
        if i % 5 == 0:
            print(year, i)
        x_i = df.sample(df.shape[0], replace=True)
        y_i = x_i['price'].values
        y_i = np.reshape(y_i, (y_i.shape[0], 1))
        x_i.drop('price', axis=1, inplace=True)
        x_i = np.c_[np.ones(x_i.shape[0]), x_i.values]
        model_i = model()
        model_i.train(x_i, y_i)
        thetas.append(list(model_i.theta))
    for j in range(len(thetas[0])):
        j_th_values = []
        for k in range(len(thetas)):
            j_th_values.append(thetas[k][j])
        j_th_values = sorted(j_th_values)
        to_save.append([j_th_values[round(n_iters * ((1 - acc) / 2)) - 1][0],
                        j_th_values[round(n_iters * (1 - ((1 - acc) / 2)))][0]])
    file_name = 'bootstrap_{}_{}.p'.format('bin' if binary else 'dis', year)
    file = open(file_name, 'wb')
    pickle.dump(to_save, file)
    file.close()


# def bootstrap_all_years(model, train_indices, n_iters=20, binary=False, acc=0.9):
def bootstrap_all_years(model, train_indices, n_iters=20, binary=False, acc=0.9, start_index=0):
    """
    A function that performs bootstrapping (for regression) in order to provide a confidence interval for the values of
    the learned weight vector (theta).
    :param model: The model the train on (assumed to be SGDRegression).
    :param train_indices: The indices of the part numbers to use for training.
    :param n_iters: The number of iterations to train the model for bootstrapping purposes.
    :param binary: A boolean whether the preprocessed data's property_type column is a discrete column of 4 binary
    columns.
    :param acc: The level of confidence we want to provide, i.e. which values to choose to be the threshold for the
    theta values.
    :return: None.
    """
    thetas = []
    to_save = []
    # for i in range(n_iters):
    for i in range(start_index, n_iters):
        model_i = model()
        print(i)
        rand_bootstrap_parts = np.random.choice(train_indices, len(train_indices), replace=True)
        for j in rand_bootstrap_parts:
            if binary:
                df = get_model_bin_all_df(j)
            else:
                df = get_model_dis_all_df(j)
            x_ij = df.sample(df.shape[0], replace=True)
            y_ij = x_ij['price'].values
            y_ij = np.reshape(y_ij, (y_ij.shape[0], 1))
            x_ij.drop('price', axis=1, inplace=True)
            x_ij = np.c_[np.ones(x_ij.shape[0]), x_ij.values]
            model_i.train(x_ij, y_ij)
        thetas.append(list(model_i.theta))
        file_name = 'bootstrap_{}_all_{}.p'.format('bin' if binary else 'dis', i)
        file = open(file_name, 'wb')
        pickle.dump(model_i.theta, file)
        file.close()

    for k in range(len(thetas[0])):
        k_th_values = []
        for l in range(len(thetas)):
            k_th_values.append(thetas[l][k])
        k_th_values = sorted(k_th_values)
        to_save.append([k_th_values[round(n_iters * ((1 - acc) / 2)) - 1][0],
                        k_th_values[round(n_iters * (1 - ((1 - acc) / 2)))][0]])
    file_name = 'bootstrap_{}_all.p'.format('bin' if binary else 'dis')
    file = open(file_name, 'wb')
    pickle.dump(to_save, file)
    file.close()
