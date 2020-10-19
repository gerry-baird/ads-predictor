import numpy as np

from FloatPredictor import FloatPredictor

fp = FloatPredictor()
param = np.array([[4]])

val = fp.predict(param)
print(f"FloatPredictor.Predict() returning type {type(val)}")
print(f"Returned: {val}")
