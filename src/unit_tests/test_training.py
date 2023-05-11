import os
import unittest
import pandas as pd
import sys
import configparser

sys.path.insert(1, os.path.join(os.getcwd(), "src"))

print(os.getcwd())

from train import Trainer
import redis
import os


def redis_f(name, value):
        
        r = redis.Redis(host=os.environ.get("REDIS_ADDRESS"),
                        port=int(os.environ.get("REDIS_PORT")),
                        username=os.environ.get("REDIS_USER"),
                        password=os.environ.get("REDIS_PASSWORD"),
                        decode_responses=True)

        r.set(name, value)

        return r.get(name)  


class TestMultiModel(unittest.TestCase):

    def setUp(self) -> None:
        self.trainer = Trainer(os.getcwd()+"/data")
    
    def test_training(self):
        f1 = self.trainer.fit()
        f1 = redis_f("f1_score", f1)
        self.assertTrue(f1 is not None)

if __name__ == "__main__":
    unittest.main()
