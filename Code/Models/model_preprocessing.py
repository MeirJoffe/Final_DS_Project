from Code.constants import *
from Code.Models.model_helpers import *


def get_preprocessed_df(year):
    """
    A function that receives a year and returns the preprocessed file containing the data for that year.
    :param year: The year.
    :return: A dataframe containing the data.
    """
    return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')


def convert_categorical_to_binaries(df, column, values_to_drop=()):
    """
    A function that receives a dataframe and a column containing categorical values and converts that column into
    multiple (n) binary columns.
    :param df: The dataframe.
    :param column: The column to convert.
    :param values_to_drop: Values in the column to not include, i.e. not to create a new column for.
    :return: The dataframe after the conversion.
    """
    for val in values_to_drop:
        df = df[df[column] != val].reset_index(drop=True)
    df.index.rename('id', inplace=True)
    df = pd.get_dummies(df, columns=[column])
    return df


def convert_property_type_to_discrete(df):
    """
    A function that receives a dataframe and converts the property_type column's values into discrete numbers (1,2,...).
    :param df: The dataframe.
    :return: The dataframe after the conversion.
    """
    df = df[df['property_type'] != 'O'].reset_index(drop=True)
    df.index.rename('id', inplace=True)
    value_map = {'D': 4, 'S': 3, 'T': 2, 'F': 1}
    df['property_type'].replace(value_map, inplace=True)
    return df


def convert_time_to_month_year(df):
    """
    A function that receives a dataframe and converts its 'date' column into a 'year' column and a 'month' column.
    :param df: The dataframe.
    :return: The dataframe after the conversion.
    """
    df['year'] = df['date'].apply(lambda x: pd.Timestamp(x).year)
    df['date'] = df['date'].apply(lambda x: pd.Timestamp(x).month)
    df.rename(columns={'date': 'month'}, inplace=True)
    return df


def model_preprocess_yr(year, binary=True):
    """
    A function that returns a fully preprocessed, ready for model use dataframe.
    :param year: The year to return the data for.
    :param binary: Whether to convert the property_type column to binary or to discrete.
    :return: The model-ready, preprocessed dataframe.
    """
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
    """
    A function that calls model_preprocess_yr for each year, converting the property_type column to binary columns and
    saves the resulting dataframes for later use.
    :return: None.
    """
    for yr in range(1999, 2019):
        df_yr = model_preprocess_yr(yr)
        df_yr.to_csv(os.path.join(MODEL_BIN_DATA_PATH, 'm_b-preprocessed-{}.csv'.format(yr)))


def model_dis_preprocess_all():
    """
    A function that calls model_preprocess_yr for each year, converting the property_type column to a discrete column
    and saves the resulting dataframes for later use.
    :return: None.
    """
    for yr in range(1999, 2019):
        df_yr = model_preprocess_yr(yr, binary=False)
        df_yr.to_csv(os.path.join(MODEL_DIS_DATA_PATH, 'm_d-preprocessed-{}.csv'.format(yr)))


def split_year_to_train_test(year, frac=0.2, binary=False):
    """
    A function that splits a given year's data to train and test, and saves each.
    :param year: The year to split the data of.
    :param frac: The percentage of the data to be set aside for testing.
    :param binary: Whether to perform this for the data whose property_type column has been converted to binary columns
    or to a discrete column.
    :return: None.
    """
    df_yr = get_df_year(year, binary)
    df_indices = list(df_yr.index)
    np.random.shuffle(df_indices)
    train_indices = df_indices[:round((1 - frac) * len(df_indices))]
    test_indices = df_indices[round((1 - frac) * len(df_indices)):]
    train_df = df_yr.loc[train_indices]
    test_df = df_yr.loc[test_indices]
    if binary:
        train_df.to_csv(os.path.join(MODEL_BIN_TRAIN, 'train-b-{}.csv'.format(year)))
        test_df.to_csv(os.path.join(MODEL_BIN_TEST, 'test-b-{}.csv'.format(year)))
    else:
        train_df.to_csv(os.path.join(MODEL_DIS_TRAIN, 'train-d-{}.csv'.format(year)))
        test_df.to_csv(os.path.join(MODEL_DIS_TEST, 'test-d-{}.csv'.format(year)))


def split_to_train_test_all_years(binary=False):
    """
    A function that repeatedly calls split_year_to_train_test for each year and both values for the bool param binary.
    :binary: A boolean whether to convert the property_type column to 4 binary columns or a discrete column.
    :return: None.
    """
    for yr in range(1999, 2019):
        split_year_to_train_test(yr, binary)


def get_len_years():
    """
    A function that calculates the number of rows in each year, i.e. how many homes were sold.
    :return: A dictionary containing the number of homes sold per year.
    """
    len_yrs = {i: len(get_df_year(i).index) for i in range(1999, 2019)}
    return len_yrs


def get_cum_years():
    """
    A function that returns the starting indices for each of years of data, were they to be sequential.
    :return: A dictionary containing the starting indices for each year's data.
    """
    len_yrs = get_len_years()
    cum_years = {1999: len_yrs[1999]}
    for yr in range(2000, 2019):
        cum_years[yr] = cum_years[yr - 1] + len_yrs[yr]
    return cum_years


def index_mapper(ind):
    """
    A function that maps indices to years.
    :param ind: The index to map.
    :return: The year containing that index.
    """
    cum_years = get_cum_years()
    for yr in range(1999, 2019):
        if ind < cum_years[yr]:
            return yr


def split_data_into_batches(test_size=0.1, num_batches=10):
    """
    A function that splits the data across all years into batches.
    :param test_size: The fraction of batches that should be for testing.
    :param num_batches: The number of batches to split each year into.
    :return: None.
    """
    len_yrs = get_len_years()
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
    """
    A function that combines each the batches into files containing data across all years.
    :param batch_num: The batch number.
    :param batch_idx: The batch indices.
    :return: None.
    """
    cum_years = get_cum_years()
    df_yr = get_df_year(1999)
    batch_yr = df_yr.loc[batch_idx]
    batch_indices = [i - cum_years[1999] for i in batch_idx if i - cum_years[1999] > 0]
    for yr in range(2000, 2019):
        df_yr = get_df_year(yr)
        batch_yr_indices = [i for i in batch_indices if i < cum_years[yr]]
        batch_yr = pd.concat([batch_yr, df_yr.loc[batch_yr_indices]], ignore_index=True)
        batch_indices = [i - cum_years[yr] for i in batch_indices if i - cum_years[yr] > 0]
    batch_yr.to_csv(os.path.join(DATA_PATH, 'batch-{}.csv'.format(batch_num)))


####### To complete the model preprocessing
# model_bin_preprocess_all()
# model_dis_preprocess_all()

####### To split all of the years to train and test files
# split_to_train_test_all_years()
# split_to_train_test_all_years(binary=True)
