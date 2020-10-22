import numpy as np

from FloatPredictor import FloatPredictor

fp = FloatPredictor()
param = np.array([[4], [8], [12]])

res_matrix = fp.predict(param)

print(f'res_matrix type: {type(res_matrix)}')
print(f"res_matrix: {res_matrix}")

res: np.ndarray = res_matrix[0]  # one input -> one output
print(f'res type: {type(res)}')
print(f"res data: {res}")
