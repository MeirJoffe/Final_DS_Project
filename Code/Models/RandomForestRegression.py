from sklearn.ensemble import RandomForestRegressor
from Code.Models.model_helpers import *


class RandomForestRegression:
    """
    A random forest regression model.
    """

    def __init__(self):
        self.model = RandomForestRegressor(warm_start=True)

    def train(self, X, y, batch_size=100000):
        batches = create_mini_batches(X, y, batch_size)
        for batch in batches:
            batch_X, batch_y = batch
            self.model.fit(batch_X, batch_y)

    def predict(self, X, max_batch_size=10000):
        if X.shape[0] > max_batch_size:
            preds = []
            batches = create_mini_batches_X_only(X, max_batch_size)
            for batch in batches:
                batch_preds = self.model.predict(batch)
                preds.append(batch_preds)
            return np.array([preds[i][j] for i in range(len(preds)) for j in range(len(preds[i]))])
        return self.model.predict(X)

    def score(self, X, y, batch_size=10000):
        total_errs = []
        batches = create_mini_batches(X, y, batch_size)
        for batch in batches:
            batch_X, batch_y = batch
            batch_preds = self.predict(batch_X)
            total_errs.append(np.sum(np.abs(batch_y - batch_preds)))
        return sum(total_errs) / y.shape[0]
