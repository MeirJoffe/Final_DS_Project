import pandas as pd
import numpy as np
import os
import re
from Code.constants import *


prosperity_df = pd.read_csv(os.path.join(PROSPERITY_DATA_PATH, '2016UKProsperityScores.csv'), header=[1])


def get_duplicates_list(df):
    """
    A function that returns the items in the column that appear more than once.
    :param df: The dataframe whose column should be inspected.
    :return: A list containing the items appearing multiple times.
    """
    u, c = np.unique(list(df['LocalAuthority']), return_counts=True)
    return list(u[c > 1])


def preprocess_prosperity_df(prosperity_df):
    for i in range(len(prosperity_df)):
        prosperity_df['LocalAuthority'][i] = prosperity_df['LocalAuthority'][i].lower().strip()
        if prosperity_df['LocalAuthority'][i] in district_changes:
            prosperity_df['LocalAuthority'][i] = district_changes[prosperity_df['LocalAuthority'][i]]
    prop_dups = get_duplicates_list(prosperity_df)
    prosperity_df.drop('Areacode', axis=1, inplace=True)
    columns_order = list(prosperity_df.keys())
    for i in prop_dups:
      i_df = prosperity_df[prosperity_df['LocalAuthority'] == i]
      i_df = i_df[columns_order]
      i_df_values = i_df[list(i_df.keys())[2:]].mean()
      i_df_values[list(i_df.keys())[0]] = i_df[list(i_df.keys())[0]].values[0]
      i_df_values[list(i_df.keys())[1]] = i_df[list(i_df.keys())[1]].values[0]
      prosperity_df = prosperity_df[prosperity_df['LocalAuthority'] != i]
      prosperity_df = prosperity_df.append(pd.DataFrame(i_df_values).T, ignore_index=True)
    prosperity_df = prosperity_df[columns_order]
    prosperity_df.set_index('LocalAuthority', inplace=True)
    return prosperity_df


# print(prosperity_df.index)
# print(get_duplicates_list(prosperity_df))
print(preprocess_prosperity_df(prosperity_df).iloc[-8:])
