import numpy as np
from sklearn.utils.validation import check_array


class IntArrayPredictor:

    # Always predicts Yellow
    def predict(self, X):

        X = check_array(X, accept_sparse=True)
        result = np.array([2, 4, 8, 16, 32, 64])

        return result
