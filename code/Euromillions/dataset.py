'''
Created on 31.10.2017

@author: sfs
'''


import numpy as np
from math import ceil
import input_utilities

def n_tot_rows_ceiled(n_tot_rows, n_last_rows):
    if(n_tot_rows%n_last_rows):
        return n_last_rows * ceil(n_tot_rows/n_last_rows)
    else:
        return n_tot_rows


def set_data(data, n_tot_rows, n_last_rows, n_elem_row):
    data = np.reshape(np.ravel(data), (n_tot_rows * n_elem_row, 1))    
        
    iterations = n_tot_rows  - n_last_rows
    print(iterations)    
    
    X = np.empty((iterations, n_elem_row * n_last_rows), int)
    Y = np.empty((iterations, n_elem_row), int)
    
    for i in range(0, iterations):        
        y = data[i * n_elem_row : (i + 1) * n_elem_row]        
        x = data[(i + 1) * n_elem_row : (i + 1 + n_last_rows) * n_elem_row]
        
        x = np.reshape(x, (1, n_last_rows * n_elem_row))
        y = np.reshape(y, (1, n_elem_row))
        
        X[i , :] = x
        Y[i , :] = y
        
    return X, Y



def normalize_data(data, num):
    ''' np.utils.to_categorical is used to convert array of labeled data(from 0 to nb_classes-1) to one-hot vector.'''
    from keras.utils import to_categorical
    shape = data.shape
    data = to_categorical(data, num_classes=num)
    return np.reshape(data, (shape[0], shape[1] * 51))

def create_dataset(n_last_rows):
    XY = input_utilities.read_statistics(2017, 2015);
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + str(XY.shape[0]))
    return set_data(XY, XY.shape[0], n_last_rows, n_elem_row=7)

def get_last_row(n_last_rows):
    XY = input_utilities.read_statistics(2017, 2015);
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>' + str(XY.shape[0]))
    return get_last_rows(XY, XY.shape[0], n_last_rows, n_elem_row=7)

def get_last_rows(data, n_tot_rows, n_last_rows, n_elem_row):
    data = np.reshape(np.ravel(data), (n_tot_rows * n_elem_row, 1))    
    i = 0
    x = data[(i) * n_elem_row : (i + n_last_rows) * n_elem_row]
    return x