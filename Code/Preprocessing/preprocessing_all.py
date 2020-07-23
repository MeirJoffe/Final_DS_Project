from Code.Preprocessing.preprocessing_price_data import *
from Code.Preprocessing.preprocessing_income_data import *
from Code.Preprocessing.preprocessing_prosperity_data import *
import warnings
warnings.filterwarnings('ignore')


def convert_columns_to_lowercase(year):
#     df_yr = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')
#     df_yr = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)), index_col='id')

    df_yr = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-city-{}.csv'.format(year)), index_col='id')

    df_yr.columns = map(str.lower, df_yr.columns)
#     df_yr.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)))
#     df_yr.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)))

    df_yr.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-city-{}.csv'.format(year)))


def convert_all_columns_to_lowercase():
    for year in range(1999, 2019):
        convert_columns_to_lowercase(year)


def get_prosperity_df():
    prosperity_df = pd.read_csv(os.path.join(PROSPERITY_DATA_PATH, '2016UKProsperityScores.csv'), header=[1])
    create_district_region_map(prosperity_df)
    prosperity_df = preprocess_prosperity_df(prosperity_df)
    return prosperity_df


def get_income_data():
    means, medians = get_mean_and_median_years()
    return means, medians


def join_income_data(df, year):
    mean_yr = get_year_df(year, 'Mean')
    median_yr = get_year_df(year, 'Median')
    df = df.join(mean_yr['Mean'], 'district').join(median_yr['Median'], 'district')
    return df


def join_prosperity_data(df, prosperity_df):
    for dist in set(df['district']):
        if dist not in list(prosperity_df.index):
            prosperity_df = add_new_prosp_row(prosperity_df, dist, dist_reg_map[dist])
    df = df.join(prosperity_df, 'district')
    return df


def preprocess_price_once(year, prosperity_df):
    # df_year = pd.read_csv(os.path.join(PRICE_DATA_PATH, 'pp-{}.csv'.format(year)), index_col='id')
    df_year = pd.read_csv(os.path.join(PRICE_DATA_PATH_A, 'pp-{}.csv'.format(year)), index_col='id')
    df_year = fill_missing_districts(df_year)
    df_year = preprocess_price_df(df_year)
    df_year = add_time_from_brexit(df_year)
    df_year = join_income_data(df_year, year)
    df_year = join_prosperity_data(df_year, prosperity_df)
    # df_year.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)))
    # df_year.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)))

    df_year.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-city-{}.csv'.format(year)))


def preprocess_price_all_years():
    prosperity_df = get_prosperity_df()
    for yr in range(1999, 2019):
        preprocess_price_once(yr, prosperity_df)


def full_preprocessing_year(year):
    prosperity_df = get_prosperity_df()
    preprocess_price_once(year, prosperity_df)
    drop_unnecessary_columns(yr)
    convert_columns_to_lowercase(yr)
    convert_to_binary(yr, ['old_new', 'duration'], ['Y', 'F'])


def full_preprocessing_all_years():
    for year in range(1999, 2019):
        full_preprocessing_year(year)


for yr in range(2014, 2019):
    print('starting preprocessing', yr)
    preprocess_price_once(yr, get_prosperity_df())
    print('dropping unnecessary columns', yr)
    drop_unnecessary_columns(yr)
    print('converting to lowercase', yr)
    convert_columns_to_lowercase(yr)
    print('converting old_new and duration to binary', yr)
    convert_to_binary(yr, ['old_new', 'duration'], ['Y', 'F'])
    from Code.Models.model_preprocessing import model_preprocess_yr
    print('starting model preprocessing', yr)
    df = model_preprocess_yr(yr, binary=True)
    # np.random.shuffle(df)
    for i in range(10):
        df_i = df.iloc[i * (len(df) // 10): (i + 1) * (len(df) // 10)]
        df_i.to_csv(os.path.join(MODEL_BIN_DATA_PATH_A, 'm_b-preprocessed-city-{}-{}.csv'.format(yr, i)))
