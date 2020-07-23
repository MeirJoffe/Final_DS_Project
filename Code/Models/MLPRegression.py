from sklearn.neural_network import MLPRegressor
from Code.Models.model_helpers import *


class MLPRegression:
    """
    A multilayer perceptron regression model.
    """

    def __init__(self):
        self.model = MLPRegressor(hidden_layer_sizes=(100,), warm_start=True, learning_rate=0.0001)
        # self.model = MLPRegressor(hidden_layer_sizes=(100, 100), warm_start=True)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

    def score(self, X, y):
        preds = self.model.predict(X)
        return np.sum(np.abs(y.flatten() - preds)) / y.shape[0]
