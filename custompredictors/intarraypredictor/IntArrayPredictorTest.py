import numpy as np

from IntArrayPredictor import IntArrayPredictor

iap = IntArrayPredictor()
param = np.array([[4]])

val = iap.predict(param)
print(f"IntArrayPredictor.Predict() returning type {type(val)}")

first_element = val[0]
print(f"First element is {type(first_element)}")

print(f"Values Returned: {val}")
