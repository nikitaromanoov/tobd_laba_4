import os
import unittest
import pandas as pd
import sys
import configparser

sys.path.insert(1, os.path.join(os.getcwd(), "src"))

print(os.getcwd())

from predict import ModelPrediction



class TestMultiModel(unittest.TestCase):

    def setUp(self) -> None:
        self.predict = ModelPrediction("./data/src/model.pkl")
    
    def test_training(self):
        predictions = self.predict.predict([[0,0,93,60,0,0,35.3,0.263,25], [0,0,2,3,4,5,3,7,15]])
        print(predictions)
        #self.assertTrue(f1 is not None)

if __name__ == "__main__":
    unittest.main()
