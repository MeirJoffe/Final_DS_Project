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
    """
    A function that performs most of the preprocessing for the prosperity dataframe.
    :param prosp_df: The prosperity dataframe.
    :return: The preprocessed dataframe.
    """
    prosp_df['LocalAuthority'] = prosp_df['LocalAuthority'].str.lower().str.strip().str.replace('.', '')
    prosp_df['Region'] = prosp_df['Region'].str.lower().str.strip()
    for i in range(len(prosp_df)):
        if prosp_df['LocalAuthority'][i] in district_changes:
            prosp_df['LocalAuthority'][i] = district_changes[prosp_df['LocalAuthority'][i]]
        if prosp_df['Region'][i] == 'east':
            prosp_df['Region'][i] = 'east of england'

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
    prosp_df.rename({'LocalAuthority': 'district'}, axis=1, inplace=True)
    prosp_df.set_index('district', inplace=True)

    prosp_df = add_new_prosp_row(prosp_df, 'city of london', 'london')
    prosp_df = add_new_prosp_row(prosp_df, 'isles of scilly', 'south west')
    return prosp_df


def add_new_prosp_row(prosp_df, local_authority, region):
    """
    A function that adds a new row to the prosperity dataframe.
    :param prosp_df: The prosperity dataframe to add to.
    :param local_authority: The local authority of the new row.
    :param region: The region of the new row.
    :return: The prosperity dataframe after adding the new row.
    """
    region_df = prosp_df[prosp_df['Region'] == region]
    col_order = list(prosp_df.keys())
    new_entry = region_df[list(col_order)[-43:]].mean()
    new_entry[col_order[0]] = region
    new_entry['district'] = local_authority
    new_entry = pd.DataFrame(new_entry).T
    new_entry.set_index('district', inplace=True)
    prosp_df = prosp_df.append(new_entry)
    prosp_df = prosp_df[col_order]
    return prosp_df


def create_district_region_map(df):
    """
    A function that populates the district region map (called reg_dist_map in constants.py).
    :param df: The dataframe to use to populate it.
    :return: None.
    """
    regions = np.unique(list(df['Region']))
    for reg in regions:
        reg_df = df[df['Region'] == reg]
        loc_auths = list(reg_df['LocalAuthority'])
        loc_auths = [i.lower().strip() for i in loc_auths]
        for j in range(len(loc_auths)):
            if loc_auths[j] in district_changes:
                loc_auths[j] = district_changes[loc_auths[j]]
        loc_auths = np.unique(loc_auths)
        reg_dist_map[reg] = set(loc_auths)
