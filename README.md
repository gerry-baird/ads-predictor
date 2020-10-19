# ads-predictor

These simple predictors can be integrated into OPS and can form the basis for more complex predictors.

The custompredictors folder contains examples. 

setup.py is just to package the predictors and upload then.

## OPS Predictor
Run buildpickle.py to pickle the predictors and package them with an OPS deployment configuration. The pkl files can then be deployed as models to OPS.

For each type of predictor there is a corresponding predictor_conf.json file. You can see which conf file is used for which predictor by looking at the code in buildpickle, but the naming convention used for th conf files shouldmake this clear too.


## Useful Commands

```
rm -r dist
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*
```

## Update OPS
So that OPS can run the pickled predictors it needs access to the library or code. Add the following to requirements-ml.txt in OPS to download the library. Obviously you'll need to point it at the version you've created.

```
--extra-index-url https://test.pypi.org/simple/
ops-custom-predictors-gerry.baird==0.0.2
```
