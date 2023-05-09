import os
import unittest
import pandas as pd
import sys
import configparser

sys.path.insert(1, os.path.join(os.getcwd(), "src"))

print(os.getcwd())

from train import Trainer



class TestMultiModel(unittest.TestCase):

    def setUp(self) -> None:
        self.trainer = Trainer(os.getcwd()+"/data")
    
    def test_training(self):
        f1 = self.trainer.fit()
        self.assertTrue(f1 is not None)

if __name__ == "__main__":
    unittest.main()
