from Code.constants import *


def get_duplicates_list(df):
    """
    A function that returns the items in the column that appear more than once.
    :param df: The dataframe whose column should be inspected.
    :return: A list containing the items appearing multiple times.
    """
    u, c = np.unique(list(df['Description']), return_counts=True)
    return list(u[c > 1])


def duplicate_row(df, new_name, existing_name, mean_med_str):
    exist_df = df[df['Description'] == existing_name]
    df = df.append(pd.DataFrame([[new_name, 0, exist_df[mean_med_str].values[0], 0]], columns=df.keys()),
                   ignore_index=True)
    return df


def split_wolverhampton_walsall(df, mean_med_str):
    if 'wolverhampton and walsall' in set(df['Description'].values):
        df = duplicate_row(df, 'walsall', 'wolverhampton and walsall', mean_med_str)
        df = duplicate_row(df, 'wolverhampton', 'wolverhampton and walsall', mean_med_str)
        df = df[df['Description'] != 'wolverhampton and walsall']
    return df


def get_year_df(year, mean_med_str):
    df_year = pd.read_csv(os.path.join(INCOME_DATA_PATH + '\\{}'.format(mean_med_str),
                                         '{}_income_{}.csv'.format(mean_med_str, year)))
    df_year[mean_med_str].fillna('x', inplace=True)
    df_year = df_year[df_year[mean_med_str] != 'x']
    df_year.reset_index(inplace=True, drop=True)

    df_year['Description'] = df_year['Description'].str.lower().str.strip()
    for i in range(len(df_year)):
        df_year['Description'][i] = df_year['Description'][i].replace(' ua', '').replace(' mc', '').split('/')[0].strip()
        if df_year['Description'][i] in district_changes:
            df_year['Description'][i] = district_changes[df_year['Description'][i]]
        df_year[mean_med_str][i] = locale.atoi(df_year[mean_med_str][i])

    df_districts = set(df_year.index)
    for region in regions_of_england:
        if region not in df_districts:
            df_year = duplicate_row(df_year, region, 'england', mean_med_str)

    df_year = split_wolverhampton_walsall(df_year, mean_med_str)

    for district in dist_reg_map:
        if district not in df_districts:
            df_year = duplicate_row(df_year, district, dist_reg_map[district], mean_med_str)

    duplicates_list = get_duplicates_list(df_year)

    for i in duplicates_list:
        i_df = df_year[df_year['Description'] == i]
        df_year = df_year[df_year['Description'] != i]
        df_year = df_year.append(pd.DataFrame([[i, 0, int(i_df[mean_med_str].mean().round()), np.nan]],
                                              columns=df_year.keys()), ignore_index=True)

    df_year.rename({'Description': 'district'}, axis=1, inplace=True)
    df_year.set_index('district', inplace=True)
    return df_year


def add_fix_change_pct(df, df_prev, mean_med_str):
    for i in list(df.index):
        if i in list(df_prev.index):
            df.loc[i]['change'] = np.round(100 - (df.loc[i][mean_med_str] / (df_prev.loc[i][mean_med_str] / 100)), 1)


def get_mean_and_median_years():
    mean_years = []
    median_years = []
    for i in range(1999, 2019):
        mean_years.append(get_year_df(i, 'Mean'))
        median_years.append(get_year_df(i, 'Median'))
    return mean_years, median_years

