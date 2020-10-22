import numpy as np

from StringPredictor import StringPredictor

sp = StringPredictor()
param = np.array([[4]])

res_matrix = sp.predict(param)
print(f'res_matrix type: {type(res_matrix)}')
print(f"res_matrix: {res_matrix}")

res: np.ndarray = res_matrix[0]  # one input -> one output
print(f'res type: {type(res)}')
print(f"res data: {res}")
