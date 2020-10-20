import numpy as np

from FloatPredictor import FloatPredictor

fp = FloatPredictor()
param = np.array([[4]])

val = fp.predict(param)
print(f"FloatPredictor.Predict() returning type {type(val)}")


first_element = val[0]
print(f"First element is {type(first_element)}")

print(f"Values Returned: {val}")
