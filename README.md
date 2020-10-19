# ads-predictor

This simple predictor can be integrated into OPS to return a float.

The GerryPredictor class can be published and then baked into the OPS runtime as an ML provider by updating the requirements-ml.txt in OPS and rebuilding the image. 

Other code is just to package the predictor and upload it.


```
rm -r dist
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*
```

