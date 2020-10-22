import numpy as np
from sklearn.utils.validation import check_array


class StringPredictor:

    # Always predicts Yellow
    def predict(self, X):

        X = check_array(X, accept_sparse=True)

        result = np.array(['Red', 'White', 'Blue'])
        return result
