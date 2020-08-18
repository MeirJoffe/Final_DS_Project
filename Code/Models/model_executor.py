from Code.constants import *
from Code.Models.model_helpers import *
from Code.Models.RandomForestRegression import *
from Code.Models.SGDRegression import *
from Code.Models.MLPRegression import *
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
import pickle


def train_test_model_by_year(model, binary=False, year_1=1999, year_2=2018, add_intercept=False, w_bootstrap=False):
    errs_by_year = []
    # file_name_base = 'years.p'

    for year in range(year_1, year_2 + 1):
        print(year)
        df_yr_tr, y_tr, df_yr_ts, y_ts, keys_lst = model_get_preprocessed_train_test_by_year(year, binary, add_intercept)

        yr_model = model()
        print('training {}'.format(year))
        yr_model.train(df_yr_tr, y_tr)

        print('predicting {}'.format(year))
        res = yr_model.score(df_yr_ts, y_ts)
        print(year, res)
        if model != MLPRegression:
            print(yr_model.most_important_features(keys_lst))
        errs_by_year.append(res)

        if w_bootstrap:
            # print('computing bootstrap')
            # bootstrap(model, df_yr_tr, year, binary=binary)
            print('calculating bootstrap {}'.format(year))
            bootstrap_fname = 'bootstrap_{}_{}.p'.format('bin' if binary else 'dis', year)
            bootstrap_file = open(bootstrap_fname, 'rb')
            bootstrap_vals = pickle.load(bootstrap_file)
            bootstrap_file.close()

            cnt = 0
            for i in range(len(yr_model.theta)):
                # vals = [bootstrap_vals[i][0], yr_model.theta[i], bootstrap_vals[i][1]]
                # print(i, bootstrap_vals[i][0], yr_model.theta[i], bootstrap_vals[i][1], max(vals) == bootstrap_vals[i][1], min(vals) == bootstrap_vals[i][0])
                if not bootstrap_vals[i][0] <= yr_model.theta[i][0] <= bootstrap_vals[i][1]:
                    print(i, keys_lst[i], bootstrap_vals[i][0], yr_model.theta[i][0], bootstrap_vals[i][1])
                    cnt += 1
            print(cnt)

        # file_name = file_name_base + '_{}_{}'.format(year, 'b' if binary else 'd')
        # file = open(file_name, 'wb')
        # pickle.dump(errs_by_year, file)
        # file.close()

    print(errs_by_year)
    return errs_by_year


def train_test_model_all_years(model, binary=False, num_parts=20, add_intercept=False, w_bootstrap=False):
    # errs_by_year = []
    # file_name_base = 'years.p'

    # shuffled_parts = [i for i in range(num_parts)]
    # np.random.shuffle(shuffled_parts)
    # train_parts = shuffled_parts[: round(len(shuffled_parts) * 0.8)]
    # test_parts = shuffled_parts[round(len(shuffled_parts) * 0.8):]

    # to delete once finished
    train_parts_fname = 'train_parts_bootstrap_{}_all.p'.format('bin' if binary else 'dis')
    train_parts_file = open(train_parts_fname, 'rb')
    train_parts = pickle.load(train_parts_file)
    train_parts_file.close()
    test_parts = [i for i in range(20) if i not in train_parts]
    print(train_parts, test_parts)

    # print('computing bootstrap')
    # bootstrap_all_years(model, train_parts, binary=binary)

    print('starting training')
    p_model = model()
    for part in train_parts:
        df, y, keys_lst = model_get_preprocessed_all_years(part, binary, add_intercept)

        print('training {}'.format(part))
        p_model.train(df, y)

        # to delete once finished
        train_file_name = 'train_bootstrap_{}_all.p'.format('bin' if binary else 'dis')
        train_file = open(train_file_name, 'wb')
        pickle.dump(p_model.theta, train_file)
        train_file.close()

    errs = []
    for part in test_parts:
        df, y, keys_lst = model_get_preprocessed_all_years(part, binary, add_intercept)

        print('predicting {}'.format(part))
        res = p_model.score(df, y)
        print("score: {}".format(res))
        errs.append((res, y.shape[0]))
        if model != MLPRegression:
            print(p_model.most_important_features(keys_lst))
        # errs_by_year.append(res)

        if w_bootstrap:
            print('calculating bootstrap')
            bootstrap_fname = 'bootstrap_{}_all.p'.format('bin' if binary else 'dis')
            bootstrap_file = open(bootstrap_fname, 'rb')
            bootstrap_vals = pickle.load(bootstrap_file)
            bootstrap_file.close()

            cnt = 0
            for i in range(len(p_model.theta)):
                # vals = [bootstrap_vals[i][0], yr_model.theta[i], bootstrap_vals[i][1]]
                # print(i, bootstrap_vals[i][0], yr_model.theta[i], bootstrap_vals[i][1], max(vals) == bootstrap_vals[i][1], min(vals) == bootstrap_vals[i][0])
                if not bootstrap_vals[i][0] <= p_model.theta[i][0] <= bootstrap_vals[i][1]:
                    print(i, keys_lst[i], bootstrap_vals[i][0], p_model.theta[i][0], bootstrap_vals[i][1])
                    cnt += 1
            print(cnt)

        # file_name = file_name_base + '_{}_{}'.format(year, 'b' if binary else 'd')
        # file = open(file_name, 'wb')
        # pickle.dump(errs_by_year, file)
        # file.close()
    print(sum([i[0] * i[1] for i in errs]) / sum([i[1] for i in errs]))

    # print(errs_by_year)
    # return errs_by_year


########## To use to train and test models by year
# train_test_model_by_year(SGDRegression, add_intercept=True, w_bootstrap=True)
# train_test_model_by_year(SGDRegression, binary=True, add_intercept=True, w_bootstrap=True)
# train_test_model_by_year(RandomForestRegression)
# train_test_model_by_year(RandomForestRegression, binary=True)
# train_test_model_by_year(MLPRegression)
# train_test_model_by_year(MLPRegression, binary=True)





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
# train_test_model_all_years(SGDRegression, add_intercept=True, w_bootstrap=True)
train_test_model_all_years(SGDRegression, binary=True, add_intercept=True, w_bootstrap=True)

# train_test_model_all_years(RandomForestRegression)
# train_test_model_all_years(RandomForestRegression, binary=True)
# train_test_model_all_years(MLPRegression)
# train_test_model_all_years(MLPRegression, binary=True)


########## Probably should be deleted
# df_yr_tr = get_model_dis_train_df(year)
# bootstrap(SGDRegression, df_yr_tr, year, binary=binary)
# for yr in range(1999, 2019):
#     df_yr_tr = get_model_bin_train_df(yr)
#     bootstrap(SGDRegression, df_yr_tr, yr, binary=binary)

# indices_fname = 'bootstrap_{}_{}.p'.format('bin' if binary else 'dis', year)
# indices_file = open(indices_fname, 'rb')
# ind = pickle.load(indices_file)
# print(ind)
# print(len(ind), len(ind[0]))
# diffs = 0
# all_diffs = []
# for i in range(len(ind)):
#     diffs += ind[i][1] - ind[i][0]
#     all_diffs.append(ind[i][1] - ind[i][0])
# print(diffs, max(all_diffs), min(all_diffs))
