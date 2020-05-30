from Code.constants import *


def get_preprocessed_df(year):
    # return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')
    return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)), index_col='id')


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
