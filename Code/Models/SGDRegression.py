from Code.Models.model_helpers import *


class SGDRegression:
    """
    A stochastic mini-batch gradient descent model.
    """

    def __init__(self, learning_rate=0.00000000001):
        """
        The initialization method.
        :param learning_rate: The learning rate to train with.
        """
        self.theta = None
        self.learning_rate = learning_rate
        self.errors = []

    def train(self, X, y, num_iters=10, batch_size=50000, w_batch=True):
        """
        The training method.
        :param X: The training data matrix.
        :param y: The training labels.
        :param num_iters: The number of iterations to train each data point.
        :param batch_size: The size of each mini-batch to train.
        :param w_batch: Whether to use batches when training or not.
        :return: None.
        """
        if self.theta is None:
            self.theta = np.zeros((X.shape[1], 1))
        for i in range(num_iters):
            if w_batch:
                batches = create_mini_batches(X, y, min(X.shape[0], batch_size), shuffle_data=True)
                for batch in batches:
                    batch_X, batch_y = batch
                    preds = self.predict(batch_X)
                    self.theta -= (1 / batch_X.shape[0]) * self.learning_rate * self._grad_function(batch_X, batch_y, preds)
                    self.errors.append(self._cost_func(batch_X, batch_y))
            else:
                preds = np.dot(X, self.theta)
                self.theta -= (1 / X.shape[0]) * self.learning_rate * self._grad_function(X, y, preds)

    def predict(self, X, max_batch_size=50000):
        """
        The prediction method.
        :param X: The test data to predict.
        :param max_batch_size: The maximal number of data points to predict per batch.
        :return: A predicted labels vector corresponding to predictions for each data point in X.
        """
        if X.shape[0] > max_batch_size:
            preds = []
            batches = create_mini_batches_X_only(X, max_batch_size)
            for batch in batches:
                batch_preds = np.dot(batch, self.theta)
                preds.append(batch_preds)
            return np.array([preds[i][j] for i in range(len(preds)) for j in range(len(preds[i]))])
        return np.dot(X, self.theta)

    def score(self, X, y):
        """
        The scoring method, using the average of the absolute error (L1 norm).
        :param X: The data matrix to score.
        :param y: The true labels.
        :return: The average (absolute) error.
        """
        total_err = 0
        for i in range(X.shape[0]):
            pred = np.dot(X[i], self.theta)
            total_err += np.abs(pred - y[i])
        return total_err / y.shape[0]

    def _cost_func(self, X, y):
        """
        The cost function for the SGD algorithm.
        :param X: The data matrix.
        :param y: The labels vector.
        :return: The cost.
        """
        pred = self.predict(X)
        return (np.dot((pred - y).T, (pred - y)) / y.shape[0])[0]

    @staticmethod
    def _grad_function(X, y, preds):
        """
        A static method to compute the gradient.
        :param X: The data matrix.
        :param y: The labels vector.
        :param preds: The predictions vector.
        :return: The result of (X.T * (preds-y)).
        """
        return np.dot(X.T, (preds - y))

    def most_important_features(self, df_keys, num_importances=5):
        """
        A method that returns the features with the largest absolute valued weights.
        :param df_keys: A list of names corresponding to the indices of theta.
        :param num_importances: The number of most important features to return.
        :return: The most important features, sorted from most to least important.
        """
        features_list = list(self.theta)
        indices = sorted(range(len(features_list)), key=lambda i: features_list[i], reverse=True)[:num_importances]
        most_important_keys = [df_keys[i] for i in indices]
        return most_important_keys
