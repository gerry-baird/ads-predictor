import numpy as np

from StringPredictor import StringPredictor

sp = StringPredictor()
param = np.array([[4]])

val = sp.predict(param)
print(f"StringPredictor.Predict() returning type {type(val)}")
print(f"Returned: {val}")

first_element = val[0]
print(f"First element is {type(first_element)}")


print(f"Values Returned: {val}")
