from Code.constants import *


def get_duplicates_list(df):
    """
    A function that returns the items in the column that appear more than once.
    :param df: The dataframe whose column should be inspected.
    :return: A list containing the items appearing multiple times.
    """
    u, c = np.unique(list(df['LocalAuthority']), return_counts=True)
    return list(u[c > 1])


def preprocess_prosperity_df(prosp_df):
    for i in range(len(prosp_df)):
        prosp_df['LocalAuthority'][i] = prosp_df['LocalAuthority'][i].lower().strip()
        if prosp_df['LocalAuthority'][i] in district_changes:
            prosp_df['LocalAuthority'][i] = district_changes[prosp_df['LocalAuthority'][i]]
    prop_dups = get_duplicates_list(prosp_df)
    prosp_df.drop('Areacode', axis=1, inplace=True)
    columns_order = list(prosp_df.keys())
    for i in prop_dups:
        i_df = prosp_df[prosp_df['LocalAuthority'] == i]
        i_df = i_df[columns_order]
        i_df_values = i_df[list(i_df.keys())[2:]].mean()
        i_df_values[list(i_df.keys())[0]] = i_df[list(i_df.keys())[0]].values[0]
        i_df_values[list(i_df.keys())[1]] = i_df[list(i_df.keys())[1]].values[0]
        prosp_df = prosp_df[prosp_df['LocalAuthority'] != i]
        prosp_df = prosp_df.append(pd.DataFrame(i_df_values).T, ignore_index=True)
    prosp_df = prosp_df[columns_order]
    prosp_df.set_index('LocalAuthority', inplace=True)
    return prosp_df


def add_new_row(prosp_df, local_authority, region):
    region_df = prosp_df[prosp_df['Region'] == region]
    col_order = list(prosp_df.keys())
    new_entry = region_df[list(col_order)[1:]].mean()
    new_entry[col_order[0]] = region
    prosp_df.loc[local_authority] = new_entry
    prosp_df = prosp_df[col_order]
    return prosp_df


def create_district_region_map(df):
    regions = np.unique(list(df['Region']))
    for reg in regions:
        reg_df = df[df['Region'] == reg]
        loc_auths = list(reg_df['LocalAuthority'])
        loc_auths = [i.lower().strip() for i in loc_auths]
        for j in range(len(loc_auths)):
            if loc_auths[j] in district_changes:
                loc_auths[j] = district_changes[loc_auths[j]]
        loc_auths = np.unique(loc_auths)
        dist_reg_map[reg] = set(loc_auths)


# print(prosperity_df.index)
# print(get_duplicates_list(prosperity_df))
# print(preprocess_prosperity_df(prosperity_df).iloc[-8:])
# print(add_new_row(preprocess_prosperity_df(prosperity_df), 'londinium', 'North East'))
# create_district_region_map(prosperity_df)
