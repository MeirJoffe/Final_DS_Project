from Code.constants import *
from matplotlib import pyplot as plt
plt.style.use('ggplot')


def get_real_estate_df(year):
    return pd.read_csv(os.path.join(PREPROCESSED_PRICE_DATA_PATH, 'preprocessed-{}.csv'.format(year)), index_col='id')


def plot_average_price_over_time():
    avg_prices = []
    for yr in range(1999, 2019):
        print('getting year: ', yr)
        df_yr = get_real_estate_df(yr)
        avg_prices.append(df_yr['price'].mean())
    plt.plot(np.arange(1999, 2019), avg_prices)
    plt.show()


plot_average_price_over_time()
