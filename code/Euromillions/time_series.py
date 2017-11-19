# -*- coding: utf-8 -*-
from random import gauss
from random import seed
from pandas import Series
from pandas.tools.plotting import autocorrelation_plot
from matplotlib import pyplot
from download import DataDownloader
# seed random number generator
seed(1)
# create white noise series
downloader = DataDownloader(2016)
series = downloader.download_data()['4']
# summary stats
print(series.describe())
# line plot
series.plot()
pyplot.show()
# histogram plot
series.hist()
pyplot.show()
# autocorrelation
autocorrelation_plot(series)
pyplot.show()
