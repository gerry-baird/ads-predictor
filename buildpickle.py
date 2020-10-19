import json
import pickle
import numpy as np
from pathlib import Path

from custompredictors.stringpredictor.StringPredictor import StringPredictor


def stringPredictorPickle():

    # Create the predictor
    stringPredictor = StringPredictor()

    # Quick Test
    param = np.array([[4]])
    val = stringPredictor.predict(param)
    print(f"Test Prediction for 6: {val}")

    with Path(__file__).resolve().parent.joinpath('string_predictor_conf.json').open(mode='r') as fd:
        conf = json.load(fd)
    with Path(__file__).resolve().parent.joinpath('string-predictor-archive-v002.pkl').open(mode='wb') as fd:
        pickle.dump(
            obj={
                'model': stringPredictor,
                'model_config': conf
            },
            file=fd
        )


if __name__ == '__main__':
    stringPredictorPickle()
