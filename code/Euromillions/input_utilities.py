# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_statistics(lastYear, initialYear):
    draws = pd.read_csv('../euromillions-past-draws-archive/euromillions-past-draws-archive' + str(lastYear) +'.txt', skiprows=2, usecols=[1,2,3,4,5],  sep = '\t')
        
    for year in range(lastYear, initialYear, -1):
        
        draws = draws.append(pd.read_csv('../euromillions-past-draws-archive/euromillions-past-draws-archive' + str(year) +'.txt', skiprows=2, usecols=[1,2,3,4,5],  sep = '\t'))
        
    #return draws.iloc[::-1].values  
    return draws.values 
    
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:i + look_back]
        dataX.append(a)
        dataY.append(dataset[i + look_back])
        
    return np.array(dataX), np.array(dataY)

def extract_last(dataset, look_back=1):
    last_records_to_encode = dataset[-look_back:] #(1,5)
    result = np.ndarray((look_back,50))
    for i, v in enumerate(last_records_to_encode):
        result[i] = convert_to_binary(v)                 
    return result
    
def convert_to_binary(listOfNum):
    """ 1-listOfNum num to 0-based bool array """
    tmp = np.zeros(50)
    for i in listOfNum:
        tmp[i-1] = 1
    return tmp  

    
def get_first(n, arr):
    result = []
    for v in arr:
        idx = np.argpartition(v, -n)[-n:] + 1
        
        result.append(idx[idx.argsort()])
    return result 

def plot(accuracies):
    plt.plot(accuracies)    
    
    plt.title("Model accuracy")
    
    plt.ylabel("accuracy")
    plt.xlabel("epoch")
    
    plt.legend(["top_k_categorical_accuracy"], loc="upper left")
    plt.show

def prepareData(look_back=6):
    test_size=0
    

    X, Y =  create_dataset(read_statistics(2017, 2015), look_back)

    RX = np.reshape(np.zeros(X.ravel().shape[0] * 10), (X.shape[0], look_back, 50)) 
    
    RY = np.reshape(np.zeros(Y.ravel().shape[0] * 10), (Y.shape[0], 50)) 
    
    for i in range(0,len(X)-1):
        converted = []
        for a in X[i]: 
            
            v = np.reshape(a, (1, 5))            
            c = convert_to_binary(v)
            c = np.reshape(c, (1, 50))
            converted.append(c)
        
        RX[i] = converted        
        RY[i] = convert_to_binary(Y[i])
        
    ntrn = round(len(RX) * (1 - test_size))

    
    X_train, y_train =RX[0:ntrn], RY[0:ntrn]
    X_test, y_test = RX[ntrn:], RY[ntrn:]

    return (X_train, y_train), (X_test, y_test)

def get_prediction(model, batch_size, look_back):
    X_last = extract_last(read_statistics(2017, 2015), look_back)
    
    X_last = X_last.reshape(batch_size, X_last.shape[0], X_last.shape[1])
    
    last_predicted = model.predict(X_last, batch_size=batch_size) 
    print(get_first(5, last_predicted))
    return get_first(5, last_predicted)
    

   