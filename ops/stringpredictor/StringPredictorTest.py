import numpy as np

from StringPredictor import StringPredictor

sp = StringPredictor()
param = np.array([[4]])

val = sp.predict(param)
print(f"GerryPredictor.PredictFloat() returning type {type(val)}")
print(f"Returned: {val}")
