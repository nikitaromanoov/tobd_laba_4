import os
import unittest
import pandas as pd
import sys
import configparser

sys.path.insert(1, os.path.join(os.getcwd(), "src"))

print(os.getcwd())

from predict import ModelPrediction

import redis
import os


def redis_f(name, value):
        
        r = redis.Redis(host=os.environ.get("REDIS_ADDRESS"),
                        port=int(os.environ.get("REDIS_PORT")),
                        username=os.environ.get("REDIS_USER"),
                        password=os.environ.get("PASSWORD"),
                        decode_responses=True)

        r.set(name, value)

        return r.get(name)    

class TestMultiModel(unittest.TestCase):

    def setUp(self) -> None:
        self.predict = ModelPrediction("./data/src/model.pkl")
    
    def test_training(self):
        predictions = self.predict.predict([[0,0,93,60,0,0,35.3,0.263,25], [0,0,2,3,4,5,3,7,15]])
        predictions = redis_f("prediction", str(predictions) )
        print(predictions)

if __name__ == "__main__":
    unittest.main()
