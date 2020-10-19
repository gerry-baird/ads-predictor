# ads-predictor

This simple predictor can be integrated into OPS to return a float.

The gerrypredictor.GerryPredictor class can be published and then baked into the OPS runtime as an ML provider by updating the requirements-ml.txt in OPS and rebuilding the image. 

setup.py is just to package the predictor and upload it.

## OPS Predictor
Run buildpickle.py to pickle the predictor and package it with an OPS deployment configuration. The pkl file can then be deployed as a model to OPS.


## Useful Commands

```
rm -r dist
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*
```

## Update OPS
So that OPS can run the pickled model it needs access to the library or code. Add the following to requirements-ml.txt in OPS to download the library. Obviously you'll need to point it at the version you've created.

```
--extra-index-url https://test.pypi.org/simple/
gerrypredictor-gerry.baird==0.0.14
```
