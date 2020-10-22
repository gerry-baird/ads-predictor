import numpy as np
from sklearn.utils.validation import check_array


class FloatPredictor:

    def predict(self, X):
        """ A reference implementation of a predicting function.
        Parameters
        ----------
        X : {array-like, sparse matrix}, shape (n_samples, n_features)
            The training input samples.
        Returns
        -------
        y : ndarray, shape (n_samples,)
            Returns an array of ones.
        """
        X = check_array(X, accept_sparse=True)
        #check_is_fitted(self, 'is_fitted_')

        samples = X.shape[0]  # The number of rows

        # broadcast a simple multiplication
        res = X * 1.1
        res.shape = (samples, )

        return res
