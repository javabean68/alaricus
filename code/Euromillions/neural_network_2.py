# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation



import dataset as ds
import numpy as np
from display import *
from keras import backend as K
import download

def my_loss(y_true, y_pred):
    return (1 - K.sum(y_true * y_pred, axis =-1))

from sklearn.model_selection import train_test_split

class NeuralNetwork(object):
    def create(self, input_dim):
        # fix random seed for reproducibility
        seed = 42
        np.random.seed(seed) 
        
        model = Sequential()
        model.add(Dense(51*7, kernel_initializer='random_uniform',
                bias_initializer='zeros', activation='sigmoid', input_dim=input_dim))
        
        

        
        
        
        model.add(Activation('softmax')) 
        model.compile(optimizer='adam',
              loss='hinge',
              metrics=['accuracy'])
        
        return model

    def run(self):

        X, Y = ds.create_dataset(n_last_rows=5);     
        
        X = ds.normalize_data(X, num=51)
        Y = ds.normalize_data(Y, num=51)   
        
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0, random_state=42)      
        
        
        nw = NeuralNetwork()
        
        model = nw.create(X_train.shape[1])
        print(model.summary())
        
        
        # Train the model, iterating on the data in batches of 16 samples
        model.fit(X_train, y_train, epochs=1000, batch_size=32)
        
        
        score = model.evaluate(X_test, y_test, batch_size=32)
        print(score)
        
        last_row = ds.get_last_row(n_last_rows=5)
        #print(last_row)
        last_row = ds.normalize_data(last_row, num=51)
        last_row = np.reshape(np.ravel(last_row), (1, 51 * 7 * 5)) 
        
        
        
        y_proba = model.predict(last_row)
        
        
        predictions = list()
        for i in range(0,7):
            v = y_proba[0, i * 51 : (i+1) * 51]            
            #print(1000 * v)
            display(10000 * np.reshape(v, (1, 51))) 
            predictions.append(v.argmax(axis=-1))
            print(v.argmax(axis=-1))
        return predictions;
            
