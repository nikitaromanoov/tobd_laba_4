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
from ansible_vault import Vault

from kafka import KafkaProducer


def  t_kafka(inp):
    with open("redis.credit") as f:
        data = vault.load(f.read()).split(" ")
    producer = KafkaProducer(bootstrap_servers=f"{data[4]}:{data[5]}", api_version=(0, 10, 2))
    producer.send("kafka-pred", bytearray(str(inp), "utf-8"))
    producer.close()

def ansible():

    vault = Vault(os.environ.get("ANSIBLE"))
    with open("redis.credit") as f:
        data = vault.load(f.read()).split(" ")
    
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
        self.predict = ModelPrediction("./data/src/model.pkl")
    
    def test_training(self):
        predictions = self.predict.predict([[0,0,93,60,0,0,35.3,0.263,25], [0,0,2,3,4,5,3,7,15]])
        predictions = redis_f("prediction", str(predictions) )
        t_kafka(predictions)
        print(predictions)

if __name__ == "__main__":
    unittest.main()
