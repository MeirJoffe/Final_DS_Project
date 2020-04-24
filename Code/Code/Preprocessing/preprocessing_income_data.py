import pandas as pd
import numpy as np
import os
import re
from Code.constants import *
import locale
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )


def get_duplicates_list(df):
    u, c = np.unique(list(df['Description']), return_counts=True)
    return list(u[c > 1])


def get_year_df(year, mean_med_str):
    mean_year = pd.read_csv(os.path.join(INCOME_DATA_PATH + '\\{}'.format(mean_med_str),
                                         '{}_income_{}.csv'.format(mean_med_str, year)))
    mean_year[mean_med_str].fillna('x', inplace=True)
    mean_year = mean_year[mean_year[mean_med_str] != 'x']
    mean_year.reset_index(inplace=True, drop=True)

    for i in range(len(mean_year)):
        mean_year['Description'][i] = mean_year['Description'][i].lower().strip().replace(' ua', '').replace(' mc', '')
        if mean_year['Description'][i] in district_changes:
            mean_year['Description'][i] = district_changes[mean_year['Description'][i]]
        mean_year[mean_med_str][i] = locale.atoi(mean_year[mean_med_str][i])

    duplicates_list = get_duplicates_list(mean_year)

    for i in duplicates_list:
        i_df = mean_year[mean_year['Description'] == i]
        mean_year = mean_year[mean_year['Description'] != i]
        mean_year = mean_year.append(
            pd.DataFrame([[i, 0, i_df[mean_med_str].mean().round(), np.nan]], columns=mean_year.keys()), ignore_index=True)

    return mean_year


def get_mean_and_median_years():
    mean_years = []
    median_years = []
    for i in range(1999, 2019):
        print(i)
        mean_years.append(get_year_df(i, 'Mean'))
        median_years.append(get_year_df(i, 'Median'))
    return mean_years, median_years
