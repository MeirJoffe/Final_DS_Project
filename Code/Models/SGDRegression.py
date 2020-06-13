from Code.Models.model_helpers import *


class SGDRegression:
    """
    A stochastic mini-batch gradient descent model.
    """

    def __init__(self, learning_rate=0.00000000001):
        self.theta = None
        self.learning_rate = learning_rate
        self.errors = []

    def train(self, X, y, num_iters=10, batch_size=50000):
        if self.theta is None:
            self.theta = np.zeros((X.shape[1], 1))
        for i in range(num_iters):
            batches = create_mini_batches(X, y, batch_size)
            for batch in batches:
                batch_X, batch_y = batch
                preds = self.predict(batch_X)
                self.theta -= (1 / batch_X.shape[0]) * self.learning_rate * self._grad_function(batch_X, batch_y, preds)
                self.errors.append(self._cost_func(batch_X, batch_y))

    def predict(self, X, max_batch_size=50000):
        if X.shape[0] > max_batch_size:
            preds = []
            batches = create_mini_batches_X_only(X, max_batch_size)
            for batch in batches:
                batch_preds = np.dot(batch, self.theta)
                preds.append(batch_preds)
            return np.array([preds[i][j] for i in range(len(preds)) for j in range(len(preds[i]))])
        return np.dot(X, self.theta)

    def score(self, X, y, batch_size=50000):
        total_errs = []
        batches = create_mini_batches(X, y, batch_size)
        for batch in batches:
            batch_X, batch_y = batch
            batch_preds = self.predict(batch_X)
            total_errs.append(np.sum(np.abs(batch_y - batch_preds)))
        return sum(total_errs) / y.shape[0]

    def _cost_func(self, X, y):
        pred = self.predict(X)
        return (np.dot((pred - y).T, (pred - y)) / y.shape[0])[0]

    @staticmethod
    def _grad_function(X, y, preds):
        return np.dot(X.T, (preds - y))
