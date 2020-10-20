# ads-predictor

These simple predictors can be integrated into OPS and can form the basis for more complex predictors.

The custompredictors folder contains some examples along with their configuration files that are used by OPS

Note that setup.py is just to package the predictors ready for upload to PyPi library. 

### Steps to Deploy a Predictor
Here are the steps to deploy a predictor into OPS. This assumes you have some familiarity with PyPi library index and rebuilding OPS.

1. Update the predictor
2. Run the sibling test utility to confirm return values
3. Update setup.py to create a new version of your library, use your name, not mine in the name
4. Run setup.py to build the predictor library (see cmd below)
5. Upload the library to PyPi using twine (see cmd below)
6. Update requirements-ml.txt of your OPS build to install the new library. Instructions for this are in the OPS repo
7. Rebuild your OPS docker image and start it
8. Check the depliyment conf for the predictor version 
9. Update the version label at the bottom of buildpickle 
10. Run buildpickle to create pickle files for each predictor
11. Upload your pickled predictors into OPS

Here is a link to the [OPS repo](https://github.com/icp4a/automation-decision-services-extensions/tree/master/open-prediction-service/ml-service-implementations/ads-ml-service) 

## Useful CLI Commands

```
rm -r dist
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository testpypi dist/*
```

## Update OPS
So that OPS can run the pickled predictors it needs access to the library. Add the following to requirements-ml.txt in OPS to download the library. Obviously you'll need to point it at the version you've created.

```
--extra-index-url https://test.pypi.org/simple/
ops-custom-predictors-gerry.baird==0.0.2
```
