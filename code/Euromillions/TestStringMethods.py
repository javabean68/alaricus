# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 18:26:05 2017

@author: admin
"""

import unittest

import numpy as np


import dataset as ds

class TestStringMethods(unittest.TestCase):
    


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        
    def test_build_data(self):      
        n_tot_rows = 1235
        n_last_rows = 14
        n_elem_row = 5
         
        n_tot_rows = ds.n_tot_rows_ceiled(n_tot_rows, n_last_rows)
        print('>>> ' + str(n_tot_rows))    
        org_data = data = np.random.randint(low=1, high=51, size=(n_tot_rows, n_elem_row))
        print(org_data)
        #data = np.reshape(np.ravel(data), (n_tot_rows * n_elem_row, 1))    
            
            
        X, Y = ds.set_data(data, n_tot_rows, n_last_rows, n_elem_row)
                
        print(X.shape)
        print(Y.shape)
            
        
        print(X)
        print(Y)
        
        self.assertEqual(data.all(), data.all())
        
        groupped = np.empty((1, n_last_rows * n_elem_row))
        data = np.reshape(np.ravel(data), (n_tot_rows * n_elem_row, 1))  
        
        
        
        groupped = data[(0 + 1) * n_elem_row : (0 + 1) * n_elem_row + (n_elem_row * n_last_rows)]        
        self.assertSequenceEqual(list(X[0]), list(groupped))        
        self.assertSequenceEqual(list(Y[0]), list(org_data[0]))
        
        groupped = data[(512 + 1) * n_elem_row : (512 + 1) * n_elem_row + (n_elem_row * n_last_rows)]        
        self.assertSequenceEqual(list(X[512]), list(groupped))        
        self.assertSequenceEqual(list(Y[512]), list(org_data[512]))
        
        
        groupped = data[(1000 + 1) * n_elem_row : (1000 + 1) * n_elem_row + (n_elem_row * n_last_rows)]       
        self.assertSequenceEqual(list(X[1000]), list(groupped))        
        self.assertSequenceEqual(list(Y[1000]), list(org_data[1000]))
        
        try:
            groupped = data[(1000 + 1) * n_elem_row : (1000 + 1) * n_elem_row + (n_elem_row * n_last_rows)]       
            self.assertSequenceEqual(list(X[1003]), list(groupped))        
            self.fail()
        except : 
            print('OK')
            
 
    def test_normalize_data(self):      
        n_tot_rows = 3235
        n_last_rows = 210
        n_elem_row = 5
         
        n_tot_rows = ds.n_tot_rows_ceiled(n_tot_rows, n_last_rows)
        print('>>> ' + str(n_tot_rows))    
        org_data = data = np.random.randint(low=1, high=51, size=(n_tot_rows, n_elem_row))
        print(org_data)
        #data = np.reshape(np.ravel(data), (n_tot_rows * n_elem_row, 1))    
            
            
        X_org, Y_org = ds.set_data(data, n_tot_rows, n_last_rows, n_elem_row) 
        
        X = ds.normalize_data(X_org, num=51)
        
        print(X.shape)
        
        print(X_org[0])
        print(X[0])
        
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        
        Y = ds.normalize_data(Y_org, num=51)
        
        print(Y.shape)
        
        print(Y_org[0])
        print(Y[0])
        
        
    def test_create_dataset(self):
        X, Y = ds.create_dataset()
        
        X = ds.normalize_data(X, num=51)
        Y = ds.normalize_data(Y, num=51)
        
        print('test_create_dataset' + str(X.shape))
        print('test_create_dataset' + str(Y.shape))
        
        

            
 
        
        
        
        
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()