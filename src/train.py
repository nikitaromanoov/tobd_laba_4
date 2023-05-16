import logging
import os
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import sys
import traceback



from sklearn import tree
from sklearn.metrics import f1_score
import pickle
import configparser

import redis
import os

from ansible_vault import Vault

SHOW_LOG = True

config = configparser.ConfigParser()
config.read("config.ini")


class Trainer():

    def __init__(self, path_dataset) -> None:
    
        self.model = tree.DecisionTreeClassifier(max_depth = int( config["parameters"]["max_depth"]))

        df_train = pd.read_csv(path_dataset+"/train.csv")
        df_test = pd.read_csv(path_dataset+"/test.csv")
        
        df_train_x = df_train.drop(columns=["Outcome"])
        self.train_x = [[df_train_x[j][i] for j in df_train_x.columns] for i in range(len(df_train_x))]
        self.train_y = list(df_train["Outcome"])
        
        df_test_x = df_test.drop(columns=["Outcome"])
        self.test_x = [[df_test_x[j][i] for j in df_test_x.columns] for i in range(len(df_test_x))]
        self.test_y = list(df_test["Outcome"])

        
    def fit(self):
        logging.info("Training...")
        
        self.model.fit(self.train_x, self.train_y)
        X_train, X_val, y_train, y_val = self.train_x[20:], self.train_x[:20], self.train_y[20:], self.train_y[:20]
        self.model.fit(X_train, y_train)

        return self.f1_score_function(X_val, y_val)

    def predict (self, X):
        return self.model.predict(X)
        
    def f1_score_function(self, X, y):
        return f1_score(y, self.predict(X))

    def save_model(self, path):

        with open(path, "wb") as file:
            pickle.dump(self.model,file)
    
def ansible():
    print(os.environ.get("ANSIBLE"))
    print(type(os.environ.get("ANSIBLE")))
    print(os.environ.get("ANSIBLE_CD"))
    print(type(os.environ.get("ANSIBLE_CD")))
    print(os.environ.get("ANSIBLE")[0])
    vault = Vault(os.environ.get("ANSIBLE"))
    data = vault.load(open("password.txt").read()).split(" ")
    
    REDIS_ADDRESS = data[2]
    REDIS_PORT = data[3]
    REDIS_USER = data[0]
    REDIS_PASSWORD = data[1]
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
    
    trainer = Trainer("./data")
    f1 = trainer.fit()
    f1 = redis_f("f1-score", f1)
    print(f1)
    logging.info(f"Valid f1: {f1}")
    trainer.save_model("./src/model.pkl")

if __name__ == "__main__":

    
    main()
