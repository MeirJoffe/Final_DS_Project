from sklearn.neural_network import MLPRegressor
from Code.Models.model_helpers import *


class MLPRegression:
    """
    A multilayer perceptron regression model.
    """

    def __init__(self):
        """
        The initialization method.
        """
        self.model = MLPRegressor(hidden_layer_sizes=(100, 100), warm_start=True)

    def train(self, X, y):
        """
        The training method.
        :param X: The training data matrix.
        :param y: The training labels.
        :return: None.
        """
        self.model.fit(X, y)

    def predict(self, X):
        """
        The prediction method.
        :param X: The test data to predict.
        :return: A predicted labels vector corresponding to predictions for each data point in X.
        """
        return self.model.predict(X)

    def score(self, X, y):
        """
        The scoring method, using the average of the absolute error (L1 norm).
        :param X: The data matrix to score.
        :param y: The true labels.
        :return: The average (absolute) error.
        """
        preds = self.model.predict(X)
        return np.sum(np.abs(y.flatten() - preds)) / y.shape[0]
