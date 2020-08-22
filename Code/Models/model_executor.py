from Code.constants import *
from Code.Models.model_helpers import *
from Code.Models.RandomForestRegression import *
from Code.Models.SGDRegression import *
from Code.Models.MLPRegression import *
import warnings
warnings.filterwarnings('ignore')
import pickle


def train_test_model_by_year(model, binary=False, year_1=1999, year_2=2018, add_intercept=False, w_bootstrap=False):
    """
    A function that trains and tests a given model on the data for given years.
    :param model: The model to train.
    :param binary: Whether the property_type column has been converted to 4 binary columns or 1 discrete column.
    :param year_1: The first year to apply the model to.
    :param year_2: The last year to apply the model to.
    :param add_intercept: Whether to add a 1's column to the matrix to represent the intercept (gradient descent only).
    :param w_bootstrap: A boolean whether to compare the results with the precalculated bootstrap.
    :return: The errors for each year in the range between year_1 and year_2.
    """
    errs_by_year = []

    for year in range(year_1, year_2 + 1):
        df_yr_tr, y_tr, df_yr_ts, y_ts, keys_lst = model_get_preprocessed_train_test_by_year(year, binary, add_intercept)

        yr_model = model()
        yr_model.train(df_yr_tr, y_tr)

        res = yr_model.score(df_yr_ts, y_ts)
        if model != MLPRegression:
            print(yr_model.most_important_features(keys_lst))
        errs_by_year.append(res)

        if w_bootstrap:
            bootstrap_fname = '{}\\bootstrap_{}_{}.p'.format(BOOTSTRAP_PATH, 'bin' if binary else 'dis', year)
            bootstrap_file = open(bootstrap_fname, 'rb')
            bootstrap_vals = pickle.load(bootstrap_file)
            bootstrap_file.close()

            for i in range(len(yr_model.theta)):
                if not bootstrap_vals[i][0] <= yr_model.theta[i][0] <= bootstrap_vals[i][1]:
                    print(i, keys_lst[i], bootstrap_vals[i][0], yr_model.theta[i][0], bootstrap_vals[i][1])

    return errs_by_year


def train_test_model_all_years(model, binary=False, num_parts=20, add_intercept=False, w_bootstrap=False):
    """
    A function that trains and tests a given model on the data across all years.
    :param model: The model to train.
    :param binary: Whether the property_type column has been converted to 4 binary columns or 1 discrete column.
    :param num_parts: The number of parts the data is spread across.
    :param add_intercept: Whether to add a 1's column to the matrix to represent the intercept (gradient descent only).
    :param w_bootstrap: A boolean whether to compare the results with the precalculated bootstrap.
    :return: None.
    """
    shuffled_parts = [i for i in range(num_parts)]
    np.random.shuffle(shuffled_parts)
    train_parts = shuffled_parts[: round(len(shuffled_parts) * 0.8)]
    test_parts = shuffled_parts[round(len(shuffled_parts) * 0.8):]

    p_model = model()
    for part in train_parts:
        df, y, keys_lst = model_get_preprocessed_all_years(part, binary, add_intercept)

        p_model.train(df, y)

    errs = []
    for part in test_parts:
        df, y, keys_lst = model_get_preprocessed_all_years(part, binary, add_intercept)

        res = p_model.score(df, y)
        errs.append((res, y.shape[0]))
        if model != MLPRegression:
            print(p_model.most_important_features(keys_lst))

        if w_bootstrap:
            bootstrap_fname = '{}\\bootstrap_{}_all.p'.format(BOOTSTRAP_PATH, 'bin' if binary else 'dis')
            bootstrap_file = open(bootstrap_fname, 'rb')
            bootstrap_vals = pickle.load(bootstrap_file)
            bootstrap_file.close()

            for i in range(len(p_model.theta)):
                if not bootstrap_vals[i][0] <= p_model.theta[i][0] <= bootstrap_vals[i][1]:
                    print(i, keys_lst[i], bootstrap_vals[i][0], p_model.theta[i][0], bootstrap_vals[i][1])

    return sum([i[0] * i[1] for i in errs]) / sum([i[1] for i in errs])


########## To use to train and test models by year
# print(train_test_model_by_year(SGDRegression, add_intercept=True, w_bootstrap=True))
# print(train_test_model_by_year(SGDRegression, binary=True, add_intercept=True, w_bootstrap=True))
# print(train_test_model_by_year(RandomForestRegression))
# print(train_test_model_by_year(RandomForestRegression, binary=True))
# print(train_test_model_by_year(MLPRegression))
# print(train_test_model_by_year(MLPRegression, binary=True))


########## To use to calculate bootstrap parts
# binary=True
# # num_parts=20
# # shuffled_parts = [i for i in range(num_parts)]
# # np.random.shuffle(shuffled_parts)
# # train_parts = shuffled_parts[: round(len(shuffled_parts) * 0.8)]
# # test_parts = shuffled_parts[round(len(shuffled_parts) * 0.8):]
# # train_parts_file_name = 'train_parts_bootstrap_{}_all.p'.format('bin' if binary else 'dis')
# # train_parts_file = open(train_parts_file_name, 'wb')
# # pickle.dump(train_parts, train_parts_file)
# # train_parts_file.close()
#
# train_parts_fname = 'train_parts_bootstrap_{}_all.p'.format('bin' if binary else 'dis')
# train_parts_file = open(train_parts_fname, 'rb')
# train_parts = pickle.load(train_parts_file)
# train_parts_file.close()
# bootstrap_all_years(SGDRegression, train_parts, binary=binary, start_index=18)


########## To use to combine bootstrap parts after training
# binary=True
# n_iters = 20
# acc = 0.9
# all_parts = []
# to_save = []
# for i in range(n_iters):
#     fname = 'bootstrap_{}_all_{}.p'.format('bin' if binary else 'dis', i)
#     file = open(fname, 'rb')
#     parts = pickle.load(file)
#     file.close()
#     all_parts.append(parts)
#
# for k in range(len(all_parts[0])):
#     k_th_values = []
#     for l in range(len(all_parts)):
#         k_th_values.append(all_parts[l][k])
#     k_th_values = sorted(k_th_values)
#     to_save.append([k_th_values[round(n_iters * ((1 - acc) / 2)) - 1][0],
#                     k_th_values[round(n_iters * (1 - ((1 - acc) / 2)))][0]])
# file_name = 'bootstrap_{}_all.p'.format('bin' if binary else 'dis')
# file = open(file_name, 'wb')
# pickle.dump(to_save, file)
# file.close()



########## To use to train and test models all years
# print(train_test_model_all_years(SGDRegression, add_intercept=True, w_bootstrap=True))
# print(train_test_model_all_years(SGDRegression, binary=True, add_intercept=True, w_bootstrap=True))
# print(train_test_model_all_years(RandomForestRegression))
# print(train_test_model_all_years(RandomForestRegression, binary=True))
# print(train_test_model_all_years(MLPRegression))
# print(train_test_model_all_years(MLPRegression, binary=True))
