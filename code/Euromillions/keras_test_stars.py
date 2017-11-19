# Create your first MLP in Keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Activation, Dropout
from keras.callbacks import ModelCheckpoint
import input_utilities as input
import numpy as np
from pathlib import Path

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)


look_back=6  
(X_train, y_train), (X_test, y_test) = input.prepareData(look_back)

print('test size {0}'.format(len(y_test)))

# build the model: 3 LSTMs 
print('Build model...') 
batch_size=1
model = Sequential() 

model.add(LSTM(10, batch_input_shape=(batch_size, look_back, 50), stateful=True, return_sequences=True))
model.add(LSTM(5, batch_input_shape=(batch_size, look_back, 50), stateful=True, return_sequences=True))
model.add(LSTM(10, batch_input_shape=(batch_size, look_back, 50), stateful=True))
model.add(Dropout(0.2))
model.add(Dense(50))
model.add(Dense(25))
model.add(Dense(50))
model.add(Activation('softmax')) 
 
epochs = 70

filepath="./weights.best.hdf5"
# load weights
try:
    my_file = Path(filepath)
    if my_file.is_file():
        # file exists
        print("Loading weights...")
        model.load_weights(filepath)
except OSError:
    print ("Oops!  That was no valid file!")

model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['top_k_categorical_accuracy'])
print("Model built.")

# checkpoint
checkpoint = ModelCheckpoint(filepath, monitor= 'val_top_k_categorical_accuracy' , verbose=2, save_best_only=True, mode= 'max' )
callbacks_list = [checkpoint]

training = False
if training:
    print("Training model...")    
    accuracies = []
    
    for i in range(epochs):
        print(str(i + 1) + '/' + str(epochs))
        history = model.fit(X_train, y_train, batch_size=batch_size, validation_split=0.01, callbacks=callbacks_list, nb_epoch=1, verbose=2, shuffle=False) #, validation_split=0.33)
        accuracies.append(history.history['val_top_k_categorical_accuracy'])
        model.reset_states()
    print("model trained")    
    
    input.plot(accuracies)

predicted = model.predict(X_test, batch_size=batch_size)  

categorical_predicted_labels = input.get_first(5, predicted)
categorical_y_test_labels = input.get_first(5, y_test)

i = 0
for prediction, test in zip(categorical_predicted_labels, categorical_y_test_labels):    
    treffer = len(np.intersect1d(test, prediction)) 
    if treffer > 4:
        print(*(prediction.tolist()), sep=' ')
        print(*(test.tolist()), sep=' ')
        print(treffer)
        i = i + 1
        
print(i)

input.print_prediction(model, batch_size, look_back)

#11, 14, 29, 48, 50
#10, 19, 39, 45, 49

#17. 20. 28. 45. 48. 

                                 

