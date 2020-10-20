import numpy as np
from sklearn.utils.validation import check_array


class FloatPredictor:

    # Always predicts Yellow
    def predict(self, X):

        X = check_array(X, accept_sparse=True)

        # Multiply the first element in X
        # by 3 and return this in an numpy array
        calc = X[0] * 3
        result = np.array([calc], dtype=np.float)

        # Make the result one dimensional
        result.shape = (1,)

        return result
