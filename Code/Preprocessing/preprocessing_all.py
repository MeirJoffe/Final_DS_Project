from Code.Preprocessing.preprocessing_price_data import *
from Code.Preprocessing.preprocessing_income_data import *
from Code.Preprocessing.preprocessing_prosperity_data import *
import warnings
warnings.filterwarnings('ignore')


def get_prosperity_df():
    prosperity_df = pd.read_csv(os.path.join(PROSPERITY_DATA_PATH, '2016UKProsperityScores.csv'), header=[1])
    create_district_region_map(prosperity_df)
    prosperity_df = preprocess_prosperity_df(prosperity_df)
    return prosperity_df


def get_income_data():
    means, medians = get_mean_and_median_years()
    return means, medians


for yr in range(1999, 2019):
    # print('c1 - {}'.format(yr))
    # # yr = 2015
    # df_yr = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(yr)), index_col='id')
    # print('c2 - {}'.format(yr))
    mean_yr = get_year_df(yr, 'Mean')
    median_yr = get_year_df(yr, 'Median')
    # print('c3 - {}'.format(yr))
    # df_yr = df_yr.join(mean_yr['Mean'], 'district').join(median_yr['Median'], 'district')
    # mean_med_missing = set()
    mean_missing = set()
    med_missing = set()
    # for i in range(len(mean_yr)):
    #     if pd.isna(mean_yr['Mean'][i]) or mean_yr['Mean'][i] == 'x':
    #         mean_missing.add(mean_yr.iloc[i])
    # for i in range(len(median_yr)):
    #     if pd.isna(median_yr['Median'][i]) or median_yr['Median'][i] == 'x':
    #         med_missing.add(median_yr.iloc[i])
    # for i in range(len(df_yr)):
    #     if pd.isna(df_yr['Mean'][i]):
    #         mean_med_missing.add(df_yr['district'][i])
    print(yr, mean_missing)
    print(yr, med_missing)
x = 2
