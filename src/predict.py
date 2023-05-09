import pickle
import numpy as np
import pandas as pd

from sklearn import tree



class ModelPrediction:
    
    def __init__(self, path_dataset):
        with open("./src/model.pkl", "rb") as f:
            self.model = pickle.load(f)
        df_test = pd.read_csv("./data/test.csv")
        
    def predict(self, X):
        return self.model.predict(X)

def main():

	trainer =  ModelPrediction("./data")
	predictions = trainer.predict([[0,0,93,60,0,0,35.3,0.263,25]])
	print(predictions)

if __name__ == '__main__':
	main()
