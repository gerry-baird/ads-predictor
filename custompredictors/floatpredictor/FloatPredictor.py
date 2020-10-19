import numpy as np
from sklearn.utils.validation import check_array


class FloatPredictor:

    # Always predicts Yellow
    def predict(self, X):

        X = check_array(X, accept_sparse=True)

        # Multiply the first element in X
        # by 3 and return this in an numpy array
        input = X[0]
        result = np.array([input * 3])

        #result = np.array([2, 4, 8, 16, 32, 64])

        return result
