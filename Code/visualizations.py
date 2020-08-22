from Code.constants import *
from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use('ggplot')


def get_real_estate_df(year):
    """
    A function that returns the preprocessed data for a given year.
    :param year: The year to provide the data for.
    :return: A dataframe containing the data for the given year.
    """
    return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')


def plot_average_price_over_time():
    """
    A function that plots the average price (on a yearly basis) over time.
    :return: None.
    """
    avg_prices = []
    for yr in range(1999, 2019):
        df_yr = get_real_estate_df(yr)
        avg_prices.append(df_yr['price'].mean())

    plt.plot(np.arange(1999, 2019), avg_prices, c='b')
    plt.xlabel('Year')
    plt.ylabel('Sale Price')
    plt.title('Average Sale Price Over Time')
    plt.xticks(np.arange(1999, 2020), rotation='vertical')
    plt.show()


def plot_average_price_over_time_month():
    """
    A function that plots the average price (on a monthly basis) over time.
    :return: None.
    """
    avg_prices = []
    for yr in range(1999, 2019):
        df_yr = get_real_estate_df(yr)
        for mth in range(1, 13):
            df_mth = df_yr[df_yr['date'].str.contains('-{}-'.format(str(mth) if mth >= 10 else '0{}'.format(mth)))]
            avg_prices.append(df_mth['price'].mean())

    plt.plot(np.linspace(1999, 2019, num=240), avg_prices, '-b')
    plt.title('Average Sale Price By Month Over Time')
    plt.xlabel('Year')
    plt.ylabel('Sale Price')
    plt.xticks(np.arange(1999, 2020), rotation='vertical')
    plt.show()


def plot_average_price_by_region():
    avg_prices = []
    regional_avg = {i: [] for i in regions}
    for yr in range(1999, 2019):
        df_yr = get_real_estate_df(yr)
        avg_prices.append(df_yr['price'].mean())
        for reg in regions:
            df_reg = df_yr[df_yr['region'] == reg]
            regional_avg[reg].append(df_reg['price'].mean())

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'lime', 'orange', 'grey', 'pink', 'k']
    regions_incl_england_and_wales = [i for i in regions]
    regions_incl_england_and_wales.append('england and wales')
    for i, reg in enumerate(regions):
        plt.plot(np.arange(1999, 2019), regional_avg[reg], colors[i])
    plt.plot(np.arange(1999, 2019), avg_prices, colors[-1])
    plt.title('Average Sale Price Over Time By Region')
    plt.xlabel('Year')
    plt.ylabel('Sale Price')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.legend(regions_incl_england_and_wales, loc='center', bbox_to_anchor=(1.3, 0.5))
    plt.show()


def plot_avg_num_sales_over_time():
    """
    A function that plots the average number of sales (on a yearly basis) over time.
    :return: None.
    """
    num_sales = []
    for yr in range(1999, 2019):
        df_yr = get_real_estate_df(yr)
        num_sales.append(len(df_yr.index))

    plt.plot(np.arange(1999, 2019), num_sales, 'p-b')
    plt.title('Number of Sales Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Sales')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.show()


def plot_avg_num_sales_over_time_month():
    """
    A function that plots the average number of sales (on a monthly basis) over time.
    :return: None.
    """
    avg_sales_by_month = []
    for yr in range(1999, 2019):
        df_yr = get_real_estate_df(yr)
        for mth in range(1, 13):
            df_mth = df_yr[df_yr['date'].str.contains('-{}-'.format(str(mth) if mth >= 10 else '0{}'.format(mth)))]
            avg_sales_by_month.append(len(df_mth.index))

    plt.plot(np.linspace(1999, 2019, num=240), avg_sales_by_month, '-b')
    plt.title('Number of Sales By Month Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Sales')
    plt.xticks(np.arange(1999, 2020), rotation='vertical')
    plt.show()


def plot_num_sales_by_region_over_time():
    """
    A function that plots the average number of sales (on a yearly basis) over time by region.
    :return: None.
    """
    regional_sales = {i: [] for i in regions}
    for yr in range(1999, 2019):
        df_yr = get_real_estate_df(yr)
        for reg in regions:
            df_reg = df_yr[df_yr['region'] == reg]
            regional_sales[reg].append(len(df_reg.index))

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'lime', 'orange', 'grey', 'pink', 'k']
    regions_incl_england_and_wales = [i for i in regions]
    regions_incl_england_and_wales.append('england and wales')
    for i, reg in enumerate(regions):
        plt.plot(np.arange(1999, 2019), regional_sales[reg], colors[i])
    plt.title('Number of Sales Over Time By Region')
    plt.xlabel('Year')
    plt.ylabel('Number of Sales')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.legend(regions, loc='center', bbox_to_anchor=(1.3, 0.5))
    plt.show()


def plot_top_counties_avg_price_over_time():
    """
    A function that plots the average price (on a yearly basis) over time for the 10 counties with the highest average.
    :return: None.
    """
    avg_prices = []
    county_avg = {}
    for yr in range(1999, 2019):
    # for yr in range(2016, 2019):
        print('getting year: ', yr)
        df_yr = get_real_estate_df(yr)
        avg_prices.append(df_yr['price'].mean())
        for county in set(df_yr['county']):
            df_county = df_yr[df_yr['county'] == county]
            if county not in county_avg:
                county_avg[county] = [df_county['price'].mean()]
            else:
                county_avg[county].append(df_county['price'].mean())
    counties_avg = sorted({i: np.mean(county_avg[i]) for i in county_avg.keys() if len(county_avg[i]) == 20}.items(),
                          key=lambda kv: kv[1], reverse=True)
    # counties_avg = sorted({i: np.mean(county_avg[i]) for i in county_avg.keys() if len(county_avg[i]) == 3}.items(),
    #                       key=lambda kv: kv[1], reverse=True)

    top_10_avg = next(iter(zip(*(counties_avg[:10]))))
    top_10_incl_england_and_wales = [i for i in top_10_avg]
    top_10_incl_england_and_wales.append('england and wales')

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'lime', 'orange', 'grey', 'pink', 'k']
    for i, county in enumerate(top_10_avg):
        plt.plot(np.arange(1999, 2019), county_avg[county], colors[i])
        # plt.plot(np.arange(2016, 2019), county_avg[county], colors[i])
    plt.plot(np.arange(1999, 2019), avg_prices, colors[-1])
    # plt.plot(np.arange(2016, 2019), avg_prices, colors[-1])
    plt.title('Top 10 Counties Average Sale Price Over Time')
    plt.xlabel('Year')
    plt.ylabel('Average Price')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    # plt.xticks(np.arange(2016, 2019), rotation='vertical')
    plt.legend(top_10_incl_england_and_wales, loc='center', bbox_to_anchor=(1.4, 0.5))

    print(top_10_incl_england_and_wales)

    plt.show()

    top_10_avg1 = next(iter(zip(*(counties_avg[1:11]))))
    top_10_incl_england_and_wales1 = [i for i in top_10_avg1]
    top_10_incl_england_and_wales1.append('england and wales')

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'lime', 'orange', 'grey', 'pink', 'k']
    for i, county in enumerate(top_10_avg1):
        plt.plot(np.arange(1999, 2019), county_avg[county], colors[i])
        # plt.plot(np.arange(2016, 2019), county_avg[county], colors[i])
    plt.plot(np.arange(1999, 2019), avg_prices, colors[-1])
    # plt.plot(np.arange(2016, 2019), avg_prices, colors[-1])
    plt.title('Top 10 Counties Average Sale Price Over Time')
    plt.xlabel('Year')
    plt.ylabel('Average Price')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    # plt.xticks(np.arange(2016, 2019), rotation='vertical')
    plt.legend(top_10_incl_england_and_wales1, loc='center', bbox_to_anchor=(1.4, 0.5))

    print(top_10_incl_england_and_wales1)

    plt.show()


def plot_bottom_counties_avg_price_over_time():
    """
    A function that plots the average price (on a yearly basis) over time for the 10 counties with the lowest average.
    :return: None.
    """
    avg_prices = []
    county_avg = {}
    for yr in range(1999, 2019):
        df_yr = get_real_estate_df(yr)
        avg_prices.append(df_yr['price'].mean())
        for county in set(df_yr['county']):
            df_county = df_yr[df_yr['county'] == county]
            if county not in county_avg:
                county_avg[county] = [df_county['price'].mean()]
            else:
                county_avg[county].append(df_county['price'].mean())
    counties_avg = sorted({i: np.mean(county_avg[i]) for i in county_avg.keys() if len(county_avg[i]) == 20}.items(),
                          key=lambda kv: kv[1], reverse=True)
    bottom_10_avg = next(iter(zip(*(counties_avg[-10:]))))
    bottom_10_incl_england_and_wales = [i for i in bottom_10_avg]
    bottom_10_incl_england_and_wales.append('england and wales')

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'lime', 'orange', 'grey', 'pink', 'k']
    for i, county in enumerate(bottom_10_avg):
        plt.plot(np.arange(1999, 2019), county_avg[county], colors[i])
    plt.plot(np.arange(1999, 2019), avg_prices, colors[-1])
    plt.title('Bottom 10 Counties Average Sale Price Over Time')
    plt.xlabel('Year')
    plt.ylabel('Average Price')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.legend(bottom_10_incl_england_and_wales, loc='center', bbox_to_anchor=(1.4, 0.5))
    plt.show()


def plot_yearly_mean_std():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    plt.plot(np.arange(1999, 2019), results_df['Mean'][:20], 'b', label='mean')
    plt.plot(np.arange(1999, 2019), results_df['STD'][:20], 'r', label='std')
    plt.plot(np.arange(1999, 2019), [results_df['Mean']['All'] for i in range(20)], 'k', label='mean - all years')
    plt.plot(np.arange(1999, 2019), [results_df['STD']['All'] for i in range(20)], 'g', label='std - all years')
    plt.title('Mean & STD Prices by Year')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.legend()
    plt.show()


def plot_yearly_results_comparison():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.iloc[:20]
    plt.plot(np.arange(1999, 2019), results_df['SGD - Dis'], 'b', label='gradient descent discrete')
    plt.plot(np.arange(1999, 2019), results_df['SGD - Bin'], 'r', label='gradient descent binary')
    plt.plot(np.arange(1999, 2019), results_df['RF - Dis'], 'g', label='random forest discrete')
    plt.plot(np.arange(1999, 2019), results_df['RF - Bin'], 'orange', label='random forest binary')
    plt.plot(np.arange(1999, 2019), results_df['MLP - Dis'], 'm', label='multi-layer perceptron discrete')
    plt.plot(np.arange(1999, 2019), results_df['MLP - Bin'], 'y', label='multi-layer perceptron binary')
    plt.title('Comparison of Model Results by Year')
    plt.xlabel('Year')
    plt.ylabel('Mean Average Error')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.legend()
    plt.show()


def plot_yearly_results_comparison_discrete():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.iloc[:20]
    plt.plot(np.arange(1999, 2019), results_df['SGD - Dis'], 'b', label='gradient descent discrete')
    plt.plot(np.arange(1999, 2019), results_df['RF - Dis'], 'g', label='random forest discrete')
    plt.plot(np.arange(1999, 2019), results_df['MLP - Dis'], 'm', label='multi-layer perceptron discrete')
    plt.title('Comparison of Model Results by Year - Discrete')
    plt.xlabel('Year')
    plt.ylabel('Mean Average Error')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.legend()
    plt.show()


def plot_yearly_results_comparison_binary():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.iloc[:20]
    plt.plot(np.arange(1999, 2019), results_df['SGD - Bin'], 'r', label='gradient descent binary')
    plt.plot(np.arange(1999, 2019), results_df['RF - Bin'], 'orange', label='random forest binary')
    plt.plot(np.arange(1999, 2019), results_df['MLP - Bin'], 'y', label='multi-layer perceptron binary')
    plt.title('Comparison of Model Results by Year - Binary')
    plt.xlabel('Year')
    plt.ylabel('Mean Average Error')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.legend()
    plt.show()


def plot_yearly_results_comparison_sgd():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.iloc[:20]
    plt.plot(np.arange(1999, 2019), results_df['SGD - Dis'], 'b', label='gradient descent discrete')
    plt.plot(np.arange(1999, 2019), results_df['SGD - Bin'], 'r', label='gradient descent binary')
    plt.title('Comparison of SGD Model Results by Year')
    plt.xlabel('Year')
    plt.ylabel('Mean Average Error')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.legend()
    plt.show()


def plot_yearly_results_comparison_rf():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.iloc[:20]
    plt.plot(np.arange(1999, 2019), results_df['RF - Dis'], 'g', label='random forest discrete')
    plt.plot(np.arange(1999, 2019), results_df['RF - Bin'], 'orange', label='random forest binary')
    plt.title('Comparison of Random Forest Model Results by Year')
    plt.xlabel('Year')
    plt.ylabel('Mean Average Error')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.legend()
    plt.show()


def plot_yearly_results_comparison_mlp():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.iloc[:20]
    plt.plot(np.arange(1999, 2019), results_df['MLP - Dis'], 'm', label='multi-layer perceptron discrete')
    plt.plot(np.arange(1999, 2019), results_df['MLP - Bin'], 'y', label='multi-layer perceptron binary')
    plt.title('Comparison of Multi-Layer Perceptron Model Results by Year')
    plt.xlabel('Year')
    plt.ylabel('Mean Average Error')
    plt.xticks(np.arange(1999, 2019), rotation='vertical')
    plt.legend()
    plt.show()


def plot_all_years_results_comparison():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.loc['All']
    model_types = ['SGD - Dis', 'SGD - Bin', 'RF - Dis', 'RF - Bin', 'MLP - Dis', 'MLP - Bin']
    results_df = results_df.loc[model_types].T
    fig, ax = plt.subplots()
    res_bar = ax.bar(np.arange(len(results_df.keys())), results_df.values, color=['b', 'r', 'g', 'c', 'y', 'k'])
    for i in range(len(res_bar)):
        ax.text(i - 0.25, res_bar[i]._height + 800, round(res_bar[i]._height), fontsize=9)
    ax.set_xticks(np.arange(len(results_df.keys())))
    ax.set_xticklabels(model_types)
    ax.set_xlabel('Model Type')
    ax.set_ylabel('Errors')
    ax.set_title('All Years Results Comparison')
    plt.show()


def plot_all_years_dis_results_comparison():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.loc['All']
    model_types = ['SGD - Dis', 'RF - Dis', 'MLP - Dis']
    results_df = results_df.loc[model_types].T
    fig, ax = plt.subplots()
    res_bar = ax.bar(np.arange(len(results_df.keys())), results_df.values, color=['b', 'r', 'g', 'c', 'y', 'k'])
    for i in range(len(res_bar)):
        ax.text(i - 0.1, res_bar[i]._height + 800, round(res_bar[i]._height), fontsize=9)
    ax.set_xticks(np.arange(len(results_df.keys())))
    ax.set_xticklabels(model_types)
    ax.set_xlabel('Model Type')
    ax.set_ylabel('Errors')
    ax.set_title('All Years Results Comparison - Discrete')
    plt.show()


def plot_all_years_bin_results_comparison():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.loc['All']
    model_types = ['SGD - Bin', 'RF - Bin', 'MLP - Bin']
    results_df = results_df.loc[model_types].T
    fig, ax = plt.subplots()
    res_bar = ax.bar(np.arange(len(results_df.keys())), results_df.values, color=['b', 'r', 'g', 'c', 'y', 'k'])
    for i in range(len(res_bar)):
        ax.text(i - 0.1, res_bar[i]._height + 800, round(res_bar[i]._height), fontsize=9)
    ax.set_xticks(np.arange(len(results_df.keys())))
    ax.set_xticklabels(model_types)
    ax.set_xlabel('Model Type')
    ax.set_ylabel('Errors')
    ax.set_title('All Years Results Comparison - Binary')
    plt.show()


def plot_all_years_sgd_results_comparison():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.loc['All']
    model_types = ['SGD - Dis', 'SGD - Bin']
    results_df = results_df.loc[model_types].T
    fig, ax = plt.subplots()
    res_bar = ax.bar(np.arange(len(results_df.keys())), results_df.values, color=['b', 'r', 'g', 'c', 'y', 'k'])
    for i in range(len(res_bar)):
        ax.text(i - 0.1, res_bar[i]._height + 800, round(res_bar[i]._height), fontsize=9)
    ax.set_xticks(np.arange(len(results_df.keys())))
    ax.set_xticklabels(model_types)
    ax.set_xlabel('Model Type')
    ax.set_ylabel('Errors')
    ax.set_title('All Years Results Comparison - Gradient Descent')
    plt.show()


def plot_all_years_rf_results_comparison():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.loc['All']
    model_types = ['RF - Dis', 'RF - Bin']
    results_df = results_df.loc[model_types].T
    fig, ax = plt.subplots()
    res_bar = ax.bar(np.arange(len(results_df.keys())), results_df.values, color=['b', 'r', 'g', 'c', 'y', 'k'])
    for i in range(len(res_bar)):
        ax.text(i - 0.1, res_bar[i]._height + 800, round(res_bar[i]._height), fontsize=9)
    ax.set_xticks(np.arange(len(results_df.keys())))
    ax.set_xticklabels(model_types)
    ax.set_xlabel('Model Type')
    ax.set_ylabel('Errors')
    ax.set_title('All Years Results Comparison - Random Forest')
    plt.show()


def plot_all_years_mlp_results_comparison():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.loc['All']
    model_types = ['MLP - Dis', 'MLP - Bin']
    results_df = results_df.loc[model_types].T
    fig, ax = plt.subplots()
    res_bar = ax.bar(np.arange(len(results_df.keys())), results_df.values, color=['b', 'r', 'g', 'c', 'y', 'k'])
    for i in range(len(res_bar)):
        ax.text(i - 0.1, res_bar[i]._height + 800, round(res_bar[i]._height), fontsize=9)
    ax.set_xticks(np.arange(len(results_df.keys())))
    ax.set_xticklabels(model_types)
    ax.set_xlabel('Model Type')
    ax.set_ylabel('Errors')
    ax.set_title('All Years Results Comparison - Multi-Layer Perceptron')
    plt.show()


def plot_most_important_features_sgd_dis():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.iloc[:20]
    all_values = {i: results_df['Most Important Features - SGD Dis'][str(i)].split(', ') for i in range(1999, 2019)}
    features_set = {i for j in range(1999, 2019) for i in all_values[j]}
    colors = ['b', 'r', 'g', 'k', 'c', 'orange', 'y']
    fig, ax = plt.subplots()
    for feature in features_set:
        rankings = [all_values[i].index(feature) + 1 if feature in all_values[i] else 0 for i in range(1999, 2019)]
        ax.plot(np.arange(1999, 2019), rankings, c=colors.pop(), label=feature)
    plt.legend()
    ax.set_xlabel('Year')
    ax.set_ylabel('Ranking')
    ax.set_xticks(np.arange(1999, 2019))
    ax.set_xticklabels(np.arange(1999, 2019), rotation='vertical')
    ax.set_title('Most Important Features Over Time - SGD Discrete')
    plt.show()


def plot_most_important_features_sgd_bin():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.iloc[:20]
    all_values = {i: results_df['Most Important Features - SGD Bin'][str(i)].split(', ') for i in range(1999, 2019)}
    features_set = {i for j in range(1999, 2019) for i in all_values[j]}
    colors = ['b', 'r', 'g', 'k', 'c', 'orange', 'y']
    fig, ax = plt.subplots()
    for feature in features_set:
        rankings = [all_values[i].index(feature) + 1 if feature in all_values[i] else 0 for i in range(1999, 2019)]
        ax.plot(np.arange(1999, 2019), rankings, c=colors.pop(), label=feature)
    plt.legend()
    ax.set_xlabel('Year')
    ax.set_ylabel('Ranking')
    ax.set_xticks(np.arange(1999, 2019))
    ax.set_xticklabels(np.arange(1999, 2019), rotation='vertical')
    ax.set_title('Most Important Features Over Time - SGD Binary')
    plt.show()


def plot_most_important_features_rf_dis():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.iloc[:20]
    all_values = {i: results_df['Most Important Features - RF Dis'][str(i)].split(', ') for i in range(1999, 2019)}
    features_set = {i for j in range(1999, 2019) for i in all_values[j]}
    colors = ['b', 'r', 'g', 'k', 'c', 'orange', 'y']
    fig, ax = plt.subplots()
    for feature in features_set:
        rankings = [all_values[i].index(feature) + 1 if feature in all_values[i] else 0 for i in range(1999, 2019)]
        ax.plot(np.arange(1999, 2019), rankings, c=colors.pop(), label=feature)
    plt.legend()
    ax.set_xlabel('Year')
    ax.set_ylabel('Ranking')
    ax.set_xticks(np.arange(1999, 2019))
    ax.set_xticklabels(np.arange(1999, 2019), rotation='vertical')
    ax.set_title('Most Important Features Over Time - Random Forest Discrete')
    plt.show()


def plot_most_important_features_rf_bin():
    results_df = pd.read_csv(os.path.join(RESULTS_PATH, 'results.csv'), index_col='Year')
    results_df = results_df.iloc[:20]
    all_values = {i: results_df['Most Important Features - RF Bin'][str(i)].split(', ') for i in range(1999, 2019)}
    features_set = {i for j in range(1999, 2019) for i in all_values[j]}
    colors = ['b', 'r', 'g', 'k', 'c', 'orange', 'y']
    fig, ax = plt.subplots()
    for feature in features_set:
        rankings = [all_values[i].index(feature) + 1 if feature in all_values[i] else 0 for i in range(1999, 2019)]
        ax.plot(np.arange(1999, 2019), rankings, c=colors.pop(), label=feature)
    plt.legend()
    ax.set_xlabel('Year')
    ax.set_ylabel('Ranking')
    ax.set_xticks(np.arange(1999, 2019))
    ax.set_xticklabels(np.arange(1999, 2019), rotation='vertical')
    ax.set_title('Most Important Features Over Time - Random Forest Binary')
    plt.show()


# plot_average_price_over_time()

# plot_average_price_over_time_month()

# plot_average_price_by_region()

# plot_avg_num_sales_over_time()

# plot_avg_num_sales_over_time_month()

# plot_num_sales_by_region_over_time()

# plot_top_counties_avg_price_over_time()

# plot_bottom_counties_avg_price_over_time()

# plot_yearly_mean_std()

# plot_yearly_results_comparison()

# plot_yearly_results_comparison_discrete()

# plot_yearly_results_comparison_binary()

# plot_yearly_results_comparison_sgd()

# plot_yearly_results_comparison_rf()

# plot_yearly_results_comparison_mlp()

# plot_all_years_results_comparison()

# plot_all_years_dis_results_comparison()

# plot_all_years_bin_results_comparison()

# plot_all_years_sgd_results_comparison()

# plot_all_years_rf_results_comparison()

# plot_all_years_mlp_results_comparison()

# plot_most_important_features_sgd_dis()

# plot_most_important_features_sgd_bin()

# plot_most_important_features_rf_dis()

# plot_most_important_features_rf_bin()
