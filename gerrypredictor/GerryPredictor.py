import numpy as np
from sklearn.utils.validation import check_array


class GerryPredictor:

    def predict(self, X):

        X = check_array(X, accept_sparse=True)

        # Multiply the first element in X
        # by 3 and return this in an numpy array
        calc = X[0] * 3
        result = np.array([calc])
        return result

    def predictString(self, X):

        X = check_array(X, accept_sparse=True)

        result = np.array(['Yellow'])
        return result
