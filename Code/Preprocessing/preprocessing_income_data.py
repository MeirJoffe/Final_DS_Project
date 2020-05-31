from Code.constants import *


def convert_2018_to_csv(filename):
    df = pd.read_excel(filename, 'All', header=[4])
    df_mean = df[['Description', 'Code', 'Mean', 'change']]
    df_median = df[['Description', 'Code', 'Mean', 'change']]
    df_mean.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2018.csv')
    df_median.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2018.csv')


def split_1999_2017(filename):
    df_mean = pd.read_excel(filename, 'FTE Mean', header=[4])
    df_median = pd.read_excel(filename, 'FTE Median', header=[4])
    df_mean_1999 = df_mean[['Description', 'Code', 'Mean', 'change']]
    df_mean_2000 = df_mean[['Description', 'Code', 'Mean.1', 'change.1']]
    df_mean_2001 = df_mean[['Description', 'Code', 'Mean.2', 'change.2']]
    df_mean_2002 = df_mean[['Description', 'Code', 'Mean.3', 'change.3']]
    df_mean_2003 = df_mean[['Description', 'Code', 'Mean.4', 'change.4']]
    df_mean_2004 = df_mean[['Description.1', 'Code.1', 'Mean.6', 'change.6']]
    df_mean_2005 = df_mean[['Description.1', 'Code.1', 'Mean.7', 'change.7']]
    df_mean_2006 = df_mean[['Description.2', 'Code.2', 'Mean.9', 'change.9']]
    df_mean_2007 = df_mean[['Description.2', 'Code.2', 'Mean.10', 'change.10']]
    df_mean_2008 = df_mean[['Description.3', 'Code.3', 'Mean.11', 'change.11']]
    df_mean_2009 = df_mean[['Description.3', 'Code.3', 'Mean.12', 'change.12']]
    df_mean_2010 = df_mean[['Description.3', 'Code.3', 'Mean.13', 'change.13']]
    df_mean_2011 = df_mean[['Description.4', 'Code.4', 'Mean.15', 'change.15']]
    df_mean_2012 = df_mean[['Description.5', 'Code.5', 'Mean.16', 'change.16']]
    df_mean_2013 = df_mean[['Description.5', 'Code.5', 'Mean.17', 'change.17']]
    df_mean_2014 = df_mean[['Description.5', 'Code.5', 'Mean.18', 'change.18']]
    df_mean_2015 = df_mean[['Description.5', 'Code.5', 'Mean.19', 'change.19']]
    df_mean_2016 = df_mean[['Description.5', 'Code.5', 'Mean.20', 'change.20']]
    df_mean_2017 = df_mean[['Description.5', 'Code.5', 'Mean.21', 'change.21']]

    df_mean_2000.rename({'Mean.1': 'Mean', 'change.1': 'change'}, axis=1, inplace=True)
    df_mean_2001.rename({'Mean.2': 'Mean', 'change.2': 'change'}, axis=1, inplace=True)
    df_mean_2002.rename({'Mean.3': 'Mean', 'change.3': 'change'}, axis=1, inplace=True)
    df_mean_2003.rename({'Mean.4': 'Mean', 'change.4': 'change'}, axis=1, inplace=True)
    df_mean_2004.rename({'Description.1': 'Description', 'Code.1': 'Code', 'Mean.6': 'Mean', 'change.6': 'change'},
                        axis=1, inplace=True)
    df_mean_2005.rename({'Description.1': 'Description', 'Code.1': 'Code', 'Mean.7': 'Mean', 'change.7': 'change'},
                        axis=1, inplace=True)
    df_mean_2006.rename({'Description.2': 'Description', 'Code.2': 'Code', 'Mean.9': 'Mean', 'change.9': 'change'},
                        axis=1, inplace=True)
    df_mean_2007.rename({'Description.2': 'Description', 'Code.2': 'Code', 'Mean.10': 'Mean', 'change.10': 'change'},
                        axis=1, inplace=True)
    df_mean_2008.rename({'Description.3': 'Description', 'Code.3': 'Code', 'Mean.11': 'Mean', 'change.11': 'change'},
                        axis=1, inplace=True)
    df_mean_2009.rename({'Description.3': 'Description', 'Code.3': 'Code', 'Mean.12': 'Mean', 'change.12': 'change'},
                        axis=1, inplace=True)
    df_mean_2010.rename({'Description.3': 'Description', 'Code.3': 'Code', 'Mean.13': 'Mean', 'change.13': 'change'},
                        axis=1, inplace=True)
    df_mean_2011.rename({'Description.4': 'Description', 'Code.4': 'Code', 'Mean.15': 'Mean', 'change.15': 'change'},
                        axis=1, inplace=True)
    df_mean_2012.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Mean.16': 'Mean', 'change.16': 'change'},
                        axis=1, inplace=True)
    df_mean_2013.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Mean.17': 'Mean', 'change.17': 'change'},
                        axis=1, inplace=True)
    df_mean_2014.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Mean.18': 'Mean', 'change.18': 'change'},
                        axis=1, inplace=True)
    df_mean_2015.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Mean.19': 'Mean', 'change.19': 'change'},
                        axis=1, inplace=True)
    df_mean_2016.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Mean.20': 'Mean', 'change.20': 'change'},
                        axis=1, inplace=True)
    df_mean_2017.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Mean.21': 'Mean', 'change.21': 'change'},
                        axis=1, inplace=True)

    df_median_1999 = df_median[['Description', 'Code', 'Median', 'change']]
    df_median_2000 = df_median[['Description', 'Code', 'Median.1', 'change.1']]
    df_median_2001 = df_median[['Description', 'Code', 'Median.2', 'change.2']]
    df_median_2002 = df_median[['Description', 'Code', 'Median.3', 'change.3']]
    df_median_2003 = df_median[['Description', 'Code', 'Median.4', 'change.4']]
    df_median_2004 = df_median[['Description.1', 'Code.1', 'Median.6', 'change.6']]
    df_median_2005 = df_median[['Description.1', 'Code.1', 'Median.7', 'change.7']]
    df_median_2006 = df_median[['Description.2', 'Code.2', 'Median.9', 'change.9']]
    df_median_2007 = df_median[['Description.2', 'Code.2', 'Median.10', 'change.10']]
    df_median_2008 = df_median[['Description.3', 'Code.3', 'Median.11', 'change.11']]
    df_median_2009 = df_median[['Description.3', 'Code.3', 'Median.12', 'change.12']]
    df_median_2010 = df_median[['Description.3', 'Code.3', 'Median.13', 'change.13']]
    df_median_2011 = df_median[['Description.4', 'Code.4', 'Median.15', 'change.15']]
    df_median_2012 = df_median[['Description.5', 'Code.5', 'Median.16', 'change.16']]
    df_median_2013 = df_median[['Description.5', 'Code.5', 'Median.17', 'change.17']]
    df_median_2014 = df_median[['Description.5', 'Code.5', 'Median.18', 'change.18']]
    df_median_2015 = df_median[['Description.5', 'Code.5', 'Median.19', 'change.19']]
    df_median_2016 = df_median[['Description.5', 'Code.5', 'Median.20', 'change.20']]
    df_median_2017 = df_median[['Description.5', 'Code.5', 'Median.21', 'change.21']]

    df_median_2000.rename({'Median.1': 'Median', 'change.1': 'change'}, axis=1, inplace=True)
    df_median_2001.rename({'Median.2': 'Median', 'change.2': 'change'}, axis=1, inplace=True)
    df_median_2002.rename({'Median.3': 'Median', 'change.3': 'change'}, axis=1, inplace=True)
    df_median_2003.rename({'Median.4': 'Median', 'change.4': 'change'}, axis=1, inplace=True)
    df_median_2004.rename({'Description.1': 'Description', 'Code.1': 'Code', 'Median.6': 'Median',
                           'change.6': 'change'}, axis=1, inplace=True)
    df_median_2005.rename({'Description.1': 'Description', 'Code.1': 'Code', 'Median.7': 'Median',
                           'change.7': 'change'}, axis=1, inplace=True)
    df_median_2006.rename({'Description.2': 'Description', 'Code.2': 'Code', 'Median.9': 'Median',
                           'change.9': 'change'}, axis=1, inplace=True)
    df_median_2007.rename({'Description.2': 'Description', 'Code.2': 'Code', 'Median.10': 'Median',
                           'change.10': 'change'}, axis=1, inplace=True)
    df_median_2008.rename({'Description.3': 'Description', 'Code.3': 'Code', 'Median.11': 'Median',
                           'change.11': 'change'}, axis=1, inplace=True)
    df_median_2009.rename({'Description.3': 'Description', 'Code.3': 'Code', 'Median.12': 'Median',
                           'change.12': 'change'}, axis=1, inplace=True)
    df_median_2010.rename({'Description.3': 'Description', 'Code.3': 'Code', 'Median.13': 'Median',
                           'change.13': 'change'}, axis=1, inplace=True)
    df_median_2011.rename({'Description.4': 'Description', 'Code.4': 'Code', 'Median.15': 'Median',
                           'change.15': 'change'}, axis=1, inplace=True)
    df_median_2012.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Median.16': 'Median',
                           'change.16': 'change'}, axis=1, inplace=True)
    df_median_2013.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Median.17': 'Median',
                           'change.17': 'change'}, axis=1, inplace=True)
    df_median_2014.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Median.18': 'Median',
                           'change.18': 'change'}, axis=1, inplace=True)
    df_median_2015.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Median.19': 'Median',
                           'change.19': 'change'}, axis=1, inplace=True)
    df_median_2016.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Median.20': 'Median',
                           'change.20': 'change'}, axis=1, inplace=True)
    df_median_2017.rename({'Description.5': 'Description', 'Code.5': 'Code', 'Median.21': 'Median',
                           'change.21': 'change'}, axis=1, inplace=True)

    df_mean_1999.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_1999.csv', index=False)
    df_mean_2000.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2000.csv', index=False)
    df_mean_2001.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2001.csv', index=False)
    df_mean_2002.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2002.csv', index=False)
    df_mean_2003.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2003.csv', index=False)
    df_mean_2004.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2004.csv', index=False)
    df_mean_2005.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2005.csv', index=False)
    df_mean_2006.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2006.csv', index=False)
    df_mean_2007.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2007.csv', index=False)
    df_mean_2008.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2008.csv', index=False)
    df_mean_2009.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2009.csv', index=False)
    df_mean_2010.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2010.csv', index=False)
    df_mean_2011.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2011.csv', index=False)
    df_mean_2012.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2012.csv', index=False)
    df_mean_2013.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2013.csv', index=False)
    df_mean_2014.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2014.csv', index=False)
    df_mean_2015.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2015.csv', index=False)
    df_mean_2016.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2016.csv', index=False)
    df_mean_2017.to_csv(MEAN_INCOME_DATA_PATH + '\\mean_income_2017.csv', index=False)

    df_median_1999.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_1999.csv', index=False)
    df_median_2000.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2000.csv', index=False)
    df_median_2001.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2001.csv', index=False)
    df_median_2002.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2002.csv', index=False)
    df_median_2003.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2003.csv', index=False)
    df_median_2004.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2004.csv', index=False)
    df_median_2005.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2005.csv', index=False)
    df_median_2006.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2006.csv', index=False)
    df_median_2007.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2007.csv', index=False)
    df_median_2008.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2008.csv', index=False)
    df_median_2009.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2009.csv', index=False)
    df_median_2010.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2010.csv', index=False)
    df_median_2011.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2011.csv', index=False)
    df_median_2012.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2012.csv', index=False)
    df_median_2013.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2013.csv', index=False)
    df_median_2014.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2014.csv', index=False)
    df_median_2015.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2015.csv', index=False)
    df_median_2016.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2016.csv', index=False)
    df_median_2017.to_csv(MEDIAN_INCOME_DATA_PATH + '\\median_income_2017.csv', index=False)


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

    df_districts = set(df_year['Description'].values)
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


def get_mean_and_median_years():
    mean_years = []
    median_years = []
    for i in range(1999, 2019):
        mean_years.append(get_year_df(i, 'Mean'))
        median_years.append(get_year_df(i, 'Median'))
    return mean_years, median_years


# filename_1999_2017 = os.path.join(INCOME_DATA_PATH, 'gaewlamedianandmeantimeseries199920166901.xls')
# split_1999_2017(filename_1999_2017)
# filename_2018 = os.path.join(INCOME_DATA_PATH, 'PROV - Home Travel To Work Area Table 12.7a   Annual pay - Gross 2018.xls')
# convert_2018_to_csv(filename_2018)

