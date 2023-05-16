import pickle
import numpy as np
import pandas as pd

from sklearn import tree

import os
import redis

from ansible_vault import Vault

class ModelPrediction:
    
    def __init__(self, path_dataset):
        with open("./src/model.pkl", "rb") as f:
            self.model = pickle.load(f)
        df_test = pd.read_csv("./data/test.csv")
        
    def predict(self, X):
        return self.model.predict(X)
        
        
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
        

def main():

	trainer =  ModelPrediction("./data")
	predictions = trainer.predict([[0,0,93,60,0,0,35.3,0.263,25]])
	predictions = redis_f("prediction", str(predictions) )
	
	print(predictions)

if __name__ == '__main__':
	main()
