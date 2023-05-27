import pickle
import numpy as np
import pandas as pd

from sklearn import tree

import os
import redis
import json

from ansible_vault import Vault
from kafka import KafkaProducer


def  t_kafka(inp):
    vault = Vault(os.environ.get("ANSIBLE"))
    with open("redis.credit") as f:
        data = vault.load(f.read()).split(" ")
    producer = KafkaProducer(bootstrap_servers=f"{str(data[4])}:{str(data[5])}", api_version=(0, 10, 2))
    producer.send("kafka-pred", bytearray(str(inp), "utf-8"))
    producer.close()



class ModelPrediction:
    
    def __init__(self, path_dataset):
        with open("./src/model.pkl", "rb") as f:
            self.model = pickle.load(f)
        df_test = pd.read_csv("./data/test.csv")
        
    def predict(self, X):
        return self.model.predict(X)
        
        
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
        

def main():

	trainer =  ModelPrediction("./data")
	with open("./tests/test_0.json") as f:
	    d = json.load(f)
	    predictions = trainer.predict(d["X"])
	    predictions = redis_f("prediction 0", str(predictions) )
	    t_kafka(predictions)
	    print(predictions, d["y"])
	with open("./tests/test_1.json") as f:
	    d = json.load(f)
	    predictions = trainer.predict(d["X"])
	    predictions = redis_f("prediction 1", str(predictions) )
	    t_kafka(predictions)
	    print(predictions, d["y"])	


if __name__ == '__main__':
	main()
