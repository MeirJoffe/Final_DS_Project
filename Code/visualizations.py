from Code.constants import *
from matplotlib import pyplot as plt
from Code.Models.model_preprocessing import get_preprocessed_df
plt.style.use('ggplot')


def get_real_estate_df(year):
    # return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')
    return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH_A, 'preprocessed-{}.csv'.format(year)), index_col='id')


def plot_average_price_over_time():
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


# plot_average_price_over_time()

# plot_average_price_over_time_month()

# plot_average_price_by_region()

# plot_avg_num_sales_over_time()

# plot_avg_num_sales_over_time_month()

# plot_num_sales_by_region_over_time()

plot_top_counties_avg_price_over_time()

# plot_bottom_counties_avg_price_over_time()
