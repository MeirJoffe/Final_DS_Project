from Code.Preprocessing.preprocessing_price_data import *
from Code.Preprocessing.preprocessing_income_data import *
from Code.Preprocessing.preprocessing_prosperity_data import *
import warnings
warnings.filterwarnings('ignore')


def convert_columns_to_lowercase(year):
    """
    A function the converts all of the columns in a given year's dataframe to lowercase.
    :param year: The year whose data should be transformed.
    :return: None.
    """
    # df_yr = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')
    df_yr = pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)), index_col='id')

    df_yr.columns = map(str.lower, df_yr.columns)
    # df_yr.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)))
    df_yr.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)))


def convert_all_columns_to_lowercase():
    """
    A function that successively calls convert_columns_to_lowercase for each year.
    :return: None.
    """
    for year in range(1999, 2019):
        convert_columns_to_lowercase(year)


def get_prosperity_df():
    """
    A function that returns the preprocessed prosperity data.
    :return: The prosperity data.
    """
    prosperity_df = pd.read_csv(os.path.join(PROSPERITY_DATA_PATH, '2016UKProsperityScores.csv'), header=[1])
    create_district_region_map(prosperity_df)
    prosperity_df = preprocess_prosperity_df(prosperity_df)
    return prosperity_df


def get_income_data():
    """
    A function that returns the mean and median incomes for all of the relevant years.
    :return: The mean and the median incomes.
    """
    means, medians = get_mean_and_median_years()
    return means, medians


def join_income_data(df, year):
    """
    A function that joins the mean and median income data of a given year with the prices of homes sold that same year.
    :param df: The home prices dataframe.
    :param year: The year.
    :return: The dataframe after adding the income data to it.
    """
    mean_yr = get_year_df(year, 'Mean')
    median_yr = get_year_df(year, 'Median')
    df = df.join(mean_yr['Mean'], 'district').join(median_yr['Median'], 'district')
    return df


def join_prosperity_data(df, prosperity_df):
    """
    A function that joins the prosperity data to the home prices data.
    :param df: The home prices data.
    :param prosperity_df: The prosperity data.
    :return: The combined dataframe.
    """
    for dist in set(df['district']):
        if dist not in list(prosperity_df.index):
            prosperity_df = add_new_prosp_row(prosperity_df, dist, dist_reg_map[dist])
    df = df.join(prosperity_df, 'district')
    return df


def preprocess_price_once(year, prosperity_df):
    """
    A function that performs all of the preprocessing (not including the model preprocessing) for a given year,
    including joining the income and prosperity data with it.
    :param year: The year to preprocess.
    :param prosperity_df: A dataframe containing the prosperity data.
    :return: None.
    """
    # df_year = pd.read_csv(os.path.join(PRICE_DATA_PATH, 'pp-{}.csv'.format(year)), index_col='id')
    df_year = pd.read_csv(os.path.join(PRICE_DATA_PATH_A, 'pp-{}.csv'.format(year)), index_col='id')
    df_year = fill_missing_districts(df_year)
    df_year = preprocess_price_df(df_year)
    df_year = add_time_from_brexit(df_year)
    df_year = join_income_data(df_year, year)
    df_year = join_prosperity_data(df_year, prosperity_df)
    # df_year.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)))
    df_year.to_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)))


def preprocess_price_all_years():
    """
    A function that successively calls preprocess_price_once for each of the years.
    :return: None.
    """
    prosperity_df = get_prosperity_df()
    for yr in range(1999, 2019):
        preprocess_price_once(yr, prosperity_df)


def full_preprocessing_year(year):
    """
    A function that calls on preprocess_price_once to perform all of the general preprocessing and also begins some of
    the model preprocessing, converting certain columns to binary.
    :param year: The year to preprocess.
    :return: None.
    """
    prosperity_df = get_prosperity_df()
    preprocess_price_once(year, prosperity_df)
    drop_unnecessary_columns(year)
    convert_columns_to_lowercase(year)
    convert_to_binary(year, ['old_new', 'duration'], ['Y', 'F'])


def full_preprocessing_all_years():
    """
    A function that successively calls full_preprocessing_year for each of the years.
    :return: None.
    """
    for year in range(1999, 2019):
        full_preprocessing_year(year)


def partition_indices_all_years(num_parts=20):
    """
    A function that partitions the indices of the data across all years into a given (default 20) number of parts.
    :param num_parts: The number of parts to split the data in to.
    :return: None.
    """
    # total_rows = 0
    # index_starts = {}
    # for yr in range(1999, 2019):
    #     print(yr)
    #     if binary:
    #         df_yr = pd.read_csv(os.path.join(MODEL_BIN_DATA_PATH_A, 'm_b-preprocessed-{}.csv'.format(yr)),
    #                             index_col='id')
    #     else:
    #         df_yr = pd.read_csv(os.path.join(MODEL_DIS_DATA_PATH_A, 'm_d-preprocessed-{}.csv'.format(yr)),
    #                             index_col='id')
    #     index_starts[yr] = total_rows
    #     total_rows += df_yr.shape[0]
    # print(total_rows)
    # index_starts[2019] = total_rows

    # todo: delete these next 2 rows
    total_rows = 20028776
    index_starts = {1999: 0, 2000: 1194146, 2001: 2322765, 2002: 3567902, 2003: 4918920, 2004: 6153699, 2005: 7384947,
                    2006: 8445792, 2007: 9771172, 2008: 11042854, 2009: 11692141, 2010: 12317095, 2011: 12980037,
                    2012: 13640810, 2013: 14309142, 2014: 15115297, 2015: 16086668, 2016: 17076843, 2017: 18076516,
                    2018: 19066197, 2019: 20028776}

    shuffled_indices = [i for i in range(total_rows)]
    np.random.shuffle(shuffled_indices)
    partitions = []
    for i in range(num_parts):
        partition = shuffled_indices[round(i * (total_rows / num_parts)): round((i + 1) * (total_rows / num_parts))]
        partition = sorted(partition)
        partitions.append(partition)

    indices_by_yr_prts = []
    for i in range(num_parts):
        indices_by_year = {yr: [] for yr in range(1999, 2019)}
        year = 1999
        start_index = 0
        for j in range(len(partitions[i])):
            if not partitions[i][j] <= min(total_rows, index_starts[year + 1]):
                yr_slice = partitions[i][start_index: j]
                yr_slice = [k - index_starts[year] for k in yr_slice]
                indices_by_year[year] = yr_slice
                start_index = j
                year += 1
        yr_slice = partitions[i][start_index:]
        yr_slice = [k - index_starts[year] for k in yr_slice]
        indices_by_year[year] = yr_slice
        indices_by_yr_prts.append(indices_by_year)
    indices_parts_fname = 'indices_parts_fname.p'
    indices_parts_file = open(indices_parts_fname, 'wb')
    pickle.dump(indices_by_yr_prts, indices_parts_file)
    indices_parts_file.close()


def separate_years(binary=False, num_parts=20, year_1=1999, year_2=2019):
    """
    A function that separates each year into a the different parts based on the partition indices.
    :param binary: Whether this data has been processed such that the property_type column was converted into binary
    columns or into a discrete column.
    :param num_parts: The number of parts the data was partitioned into.
    :param year_1: The first year to begin the separation.
    :param year_2: The last year (plus 1) to do the separation for.
    :return: None.
    """
    indices_parts_fname = 'indices_parts_fname.p'
    indices_parts_file = open(indices_parts_fname, 'rb')
    indices_by_yr_prts = pickle.load(indices_parts_file)

    for yr in range(year_1, year_2):
        if binary:
            df_yr = pd.read_csv(os.path.join(MODEL_BIN_DATA_PATH_A, 'm_b-preprocessed-{}.csv'.format(yr)),
                                index_col='id')
        else:
            df_yr = pd.read_csv(os.path.join(MODEL_DIS_DATA_PATH_A, 'm_d-preprocessed-{}.csv'.format(yr)),
                                index_col='id')

        for j in range(num_parts):
            print('starting part {} {}'.format(j, yr))
            df_par_j = df_yr.loc[indices_by_yr_prts[j][yr]]
            df_par_j.dropna(inplace=True)
            if binary:
                df_par_j.to_csv(os.path.join(MODEL_BIN_COMB_A, 'm_b-preprocessed-part-{}-{}.csv'.format(j, yr)))
            else:
                df_par_j.to_csv(os.path.join(MODEL_DIS_COMB_A, 'm_d-preprocessed-part-{}-{}.csv'.format(j, yr)))


def combine_years(binary=False, year_1=1999, year_2=2019, part_1=0, part_2=20):
    """
    A function to combine the parts from all the years (in the range between year_1 and year_2) into a single file per
    part.
    :param binary: Whether this data has been processed such that the property_type column was converted into binary
    columns or into a discrete column.
    :param year_1: The first year to begin the combination.
    :param year_2: The last year (plus 1) to do combination separation for.
    :param part_1: The first part (number).
    :param part_2: The last part (number).
    :return: None.
    """
    for p in range(part_1, part_2):
        df_par_p = None
        print('starting part: ', p)
        for yr in range(year_1, year_2):
            print('now combining year: {} in part: {}'.format(yr, p))
            if binary:
                df_yr = pd.read_csv(os.path.join(MODEL_BIN_COMB_A, 'm_b-preprocessed-part-{}-{}.csv'.format(p, yr)),
                                    index_col='id')
            else:
                df_yr = pd.read_csv(os.path.join(MODEL_DIS_COMB_A, 'm_d-preprocessed-part-{}-{}.csv'.format(p, yr)),
                                    index_col='id')
            if df_par_p is None:
                df_par_p = df_yr
            else:
                df_par_p = pd.concat([df_par_p, df_yr])
        if binary:
            df_par_p.to_csv(os.path.join(MODEL_BIN_COMB_A, 'm_b-preprocessed-part-{}.csv'.format(p)))
        else:
            df_par_p.to_csv(os.path.join(MODEL_DIS_COMB_A, 'm_d-preprocessed-part-{}.csv'.format(p)))


# partition_indices_all_years()
# separate_years()
# combine_years()

# partition_indices_all_years()
# separate_years(binary=True)
# combine_years(binary=True)


# for yr in range(1999, 2019):
#     print('starting preprocessing', yr)
#     preprocess_price_once(yr, get_prosperity_df())
#     print('dropping unnecessary columns', yr)
#     drop_unnecessary_columns(yr)
#     print('converting to lowercase', yr)
#     convert_columns_to_lowercase(yr)
#     print('converting old_new and duration to binary', yr)
#     convert_to_binary(yr, ['old_new', 'duration'], ['Y', 'F'])
#     from Code.Models.model_preprocessing import model_preprocess_yr
#     print('starting model preprocessing', yr)
#     df = model_preprocess_yr(yr, binary=True)
#     # np.random.shuffle(df)
#     for i in range(10):
#         df_i = df.iloc[i * (len(df) // 10): (i + 1) * (len(df) // 10)]
#         df_i.to_csv(os.path.join(MODEL_BIN_DATA_PATH_A, 'm_b-preprocessed-city-{}-{}.csv'.format(yr, i)))
