import numpy as np
from gerrypredictor.GerryPredictor import GerryPredictor

gp = GerryPredictor()
param = np.array([[4]])

val = gp.predict(param)
print(f"GerryPredictor.PredictFloat() returning type {type(val)}")
print(f"Returned: {val}")

val = gp.predictString(param)
print(f"GerryPredictor.PredictString() returning type {type(val)}")
print(f"Returned: {val}")
