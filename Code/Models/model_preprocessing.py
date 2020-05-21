from Code.constants import *


def get_preprocessed_df(year):
    return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')


def convert_categorical_to_binaries(df, column, values_to_drop=()):
    for val in values_to_drop:
        df = df[df[column] != val].reset_index(drop=True)
    df = pd.concat([df, pd.get_dummies(df, columns=[column])], axis=1).drop(columns=column, axis=1)
    return df


def convert_property_type_to_discrete(df):
    df = df[df['property_type'] != 'O'].reset_index(drop=True)
    value_map = {'D': 4, 'S': 3, 'T': 2, 'F': 1}
    df['property_type'].replace(value_map, inplace=True)
    return df


def convert_time_to_month_year(df):
    df['year'] = df['date'].apply(lambda x: pd.Timestamp(x).year)
    df['date'] = df['date'].apply(lambda x: pd.Timestamp(x).month)
    df.rename(columns={'date': 'month'}, inplace=True)
    return df

