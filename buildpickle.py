import json
import pickle
import numpy as np
from pathlib import Path

from gerrypredictor.GerryPredictor import GerryPredictor


def buildpickle():

    # Create the predictor
    gerryPredictor = GerryPredictor()

    # Quick Test
    param = np.array([[4]])
    val = gerryPredictor.predict(param)
    print(f"Test Prediction for 6: {val}")

    with Path(__file__).resolve().parent.joinpath('deployment_conf.json').open(mode='r') as fd:
        conf = json.load(fd)
    with Path(__file__).resolve().parent.joinpath('gerry-predictor-archive-v014.pkl').open(mode='wb') as fd:
        pickle.dump(
            obj={
                'model': gerryPredictor,
                'model_config': conf
            },
            file=fd
        )


if __name__ == '__main__':
    buildpickle()
