'''
Created on 07.11.2017
pip3 --proxy=localhost:3128 install keras
@author: sfs
'''


from numpy import array
from numpy import argmax
from sklearn.utils.extmath import softmax

from keras.utils import to_categorical
# define example
data = [1, 3, 2, 0, 3, 2, 2, 1, 0, 1]
data = array(data)
print(data)
# one hot encode
encoded = to_categorical(data)
print(encoded)
# invert encoding
inverted = argmax(encoded[4])
print(inverted)

print(softmax(encoded))
