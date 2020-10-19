import json
import pickle
import numpy as np
from pathlib import Path

from custompredictors.stringpredictor.StringPredictor import StringPredictor
from custompredictors.floatpredictor.FloatPredictor import FloatPredictor


def stringPredictorPickle(archive_version):

    # Create the predictor
    stringPredictor = StringPredictor()

    # Quick Test
    param = np.array([[4]])
    val = stringPredictor.predict(param)
    print(f"Test Prediction for 6: {val}")

    with Path(__file__).resolve().parent.joinpath('string_predictor_conf.json').open(mode='r') as fd:
        conf = json.load(fd)
    with Path(__file__).resolve().parent.joinpath(f'string-predictor-archive-{archive_version}.pkl').open(mode='wb') as fd:
        pickle.dump(
            obj={
                'model': stringPredictor,
                'model_config': conf
            },
            file=fd
        )


def floatPredictorPickle(archive_version):

    # Create the predictor
    floatPredictor = FloatPredictor()

    # Quick Test
    param = np.array([[4]])
    val = floatPredictor.predict(param)
    print(f"Test Prediction for 6: {val}")

    with Path(__file__).resolve().parent.joinpath('float_predictor_conf.json').open(mode='r') as fd:
        conf = json.load(fd)
    with Path(__file__).resolve().parent.joinpath(f'float-predictor-archive-{archive_version}.pkl').open(mode='wb') as fd:
        pickle.dump(
            obj={
                'model': floatPredictor,
                'model_config': conf
            },
            file=fd
        )


if __name__ == '__main__':
    archive_version = "006"
    stringPredictorPickle(archive_version)
    floatPredictorPickle(archive_version)
