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
from ansible_vault import Vault


def ansible():

    vault = Vault(os.environ.get("ANSIBLE"))
    data = vault.load(open("redis.credit").read()).split(" ")
    
    REDIS_ADDRESS = data[2]
    REDIS_PORT = data[1]
    REDIS_USER = data[3]
    REDIS_PASSWORD = data[0]
    return REDIS_ADDRESS, REDIS_PORT, REDIS_USER, REDIS_PASSWORD  
    
    

def redis_f(name, value):
        REDIS_ADDRESS, REDIS_PORT, REDIS_USER, REDIS_PASSWORD = ansible()
        r = redis.Redis(host=REDIS_ADDRESS,
                        port=REDIS_PORT,
                        username=REDIS_USER,
                        password=REDIS_PASSWORD,
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
