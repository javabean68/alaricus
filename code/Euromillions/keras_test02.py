# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Activation

import input_utilities as input
import numpy as np




class NeuralNetwork(object):
    def run(self):
        # fix random seed for reproducibility
        seed = 7
        np.random.seed(seed)
        
        
        look_back=6  
        (X_train, y_train), (X_test, y_test) = input.prepareData(look_back)
        
        print('test size {0}'.format(len(y_test)))
        
        
        print('Build model...') 
        batch_size=1
        model = Sequential() 
        
        model.add(LSTM(10, batch_input_shape=(batch_size, look_back, 50), stateful=True, return_sequences=True))
        model.add(LSTM(10, batch_input_shape=(batch_size, look_back, 50), stateful=True, return_sequences=True))
        model.add(LSTM(10, batch_input_shape=(batch_size, look_back, 50), stateful=True, return_sequences=True))
       
        
        model.add(LSTM(5, batch_input_shape=(batch_size, look_back, 50), stateful=True, return_sequences=True))
        model.add(LSTM(10, batch_input_shape=(batch_size, look_back, 50), stateful=True))
        
        model.add(Dense(50))
        model.add(Activation('softmax')) 
         
        epochs = 100
        
        
        
        model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['top_k_categorical_accuracy'])
        print("Model built.")
        
        
        
        training = True
        if training:
            print("Training model...")    
            
            
            for i in range(epochs):
                print(str(i + 1) + '/' + str(epochs))
                model.fit(X_train, y_train, batch_size=batch_size, validation_split=0.0, nb_epoch=1, verbose=1, shuffle=False)
                model.reset_states()
            print("model trained")    
            
           
        
        
        return input.get_prediction(model, batch_size, look_back) 
