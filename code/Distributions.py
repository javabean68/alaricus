# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import thinkplot
import thinkstats2

def read_statistics(year):
    draws = pd.read_csv('./euromillions-past-draws-archive/euromillions-past-draws-archive' + str(year) +'.txt', skiprows=2, usecols=[1,2,3,4,5],  sep = '\t', names=['1','2','3','4','5'])
    return draws.iloc[::-1]    
    


#df = read_statistics(2016);
                    
df = pd.concat([read_statistics(y) for y in [2012, 2013, 2014, 2015, 2016, 2017]])
                    



sample_pdf = thinkstats2.EstimatedPdf(df['1'])
thinkplot.Pdf(sample_pdf, label='sample KDE')

mean1 = df['5'].mean()
std1 = df['5'].std()

normal1 = thinkstats2.NormalPdf(mean1, std1)
thinkplot.Pdf(normal1, label="normal1", color="red")

print(mean1)
print(std1)

"""
Correlation
"""
print( 'Spearman Correlation (%d,%d)->%f '% (1,2,df['1'].corr(df['2'], 'spearman') ) )
print( 'Spearman Correlation (%d,%d)->%f '% (1,3,df['1'].corr(df['3'], 'spearman') ) )
print( 'Spearman Correlation (%d,%d)->%f '% (1,4,df['1'].corr(df['4'], 'spearman') ) )
print( 'Spearman Correlation (%d,%d)->%f '% (1,5,df['1'].corr(df['5'], 'spearman') ) )


print( 'Spearman Correlation (%d,%d)->%f '% (4,5,df['4'].corr(df['5']) ) )

df['1'] = thinkstats2.Jitter(df['1'], 0.5)
df['2'] = thinkstats2.Jitter(df['2'], 0.5)
#thinkplot.Scatter(df['1'], df['2'], alpha=0.2)
#thinkplot.Show(xlabel='1', ylabel='2', axis=[1,50,1,50])

#thinkplot.HexBin(df['4'].values, df['5'].values)

"""
Correlation
"""


sample_pdf = thinkstats2.EstimatedPdf(df['2'])
thinkplot.Pdf(sample_pdf, label='sample KDE')

sample_pdf = thinkstats2.EstimatedPdf(df['3'])
thinkplot.Pdf(sample_pdf, label='sample KDE')

sample_pdf = thinkstats2.EstimatedPdf(df['4'])
thinkplot.Pdf(sample_pdf, label='sample KDE')

sample_pdf = thinkstats2.EstimatedPdf(df['5'])
thinkplot.Pdf(sample_pdf, label='sample KDE')


df_tot = pd.concat([df[i] for i in '12345'])

sample_pdf = thinkstats2.EstimatedPdf(df_tot)
thinkplot.Pdf(sample_pdf, label='sample KDE')

pmf = thinkstats2.Pmf(df_tot);
thinkplot.Hist(pmf)

cdf = thinkstats2.Cdf(df_tot, label='actual')
#thinkplot.Cdf(cdf) 
