from Code.constants import *
from Code.Models.model_helpers import *
from Code.Models.RandomForestRegression import *
from Code.Models.SGDRegression import *
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')


def train_test_model_by_year(model, binary=False, year_1=1999, year_2=2018, add_intercept=False):
    errs_by_year = []

    for year in range(year_1, year_2 + 1):
        print(year)
        df_yr_tr, y_tr, df_yr_ts, y_ts = model_get_preprocessed_train_test(year, binary, add_intercept)

        yr_model = model()
        print('training')
        yr_model.train(df_yr_tr, y_tr)

        print('predicting')
        res = yr_model.score(df_yr_ts, y_ts)
        print(year, res)
        errs_by_year.append(res)

    print(errs_by_year)
    return errs_by_year


# train_test_model_by_year(RandomForestRegression())
# train_test_model_by_year(RandomForestRegression(), binary=True)
# train_test_model_by_year(SGDRegression())
# train_test_model_by_year(SGDRegression(), binary=True)

