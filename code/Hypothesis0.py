# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import thinkplot
import thinkstats2

def read_statistics(year):
    draws = pd.read_csv('./euromillions-past-draws-archive' + str(year) +'.txt', skiprows=2, usecols=[1,2,3,4,5],  sep = '\t', names=['1','2','3','4','5'])
    
    return draws.iloc[::-1]    
    



class DrawsTest(thinkstats2.HypothesisTest):
    def MakeModel(self):
        self.numbers = [i + 1 for i in range(50)]
        self.matrix = np.asarray(pd.concat([read_statistics(y) for y in [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]])) 
        print('Matrix rows', self.matrix.shape[0])
        
    def RunModel(self):
        hist = thinkstats2.Hist()
        
        draw = np.random.choice(self.numbers, 5, replace=False)
        for i in range(self.matrix.shape[0]):
            guessed = np.intersect1d(draw, self.matrix[i,:])
            hist.Incr(len(guessed))
        return hist
            
    def TestStatistic(self, data):
        #how many times guess 3 Numbers right
       return data.Freq(3)

observed = thinkstats2.Hist({0:20, 1:10, 2:5, 3:12, 4:3, 5:0})
ht = DrawsTest(observed)
print('actual', ht.actual)
print('pvalue', ht.PValue())

ht.PlotCdf()
thinkplot.Show(xlabel='test statistic', ylabel='CDF')
        