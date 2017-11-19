'''

Created on 09.11.2017


@author: sfs

'''
import numpy as np

from matplotlib import pylab

from pylab import *


nums = np.arange(51)

probs = np.random.randint(low = 0, high = 10, size= (1, 51))

cdict = {'red': ((0.0, 0.0, 0.0),

(0.5, 1.0, 0.7),

(1.0, 1.0, 1.0)),

'green': ((0.0, 0.0, 0.0),

(0.5, 1.0, 0.0),

(1.0, 1.0, 1.0)),

'blue': ((0.0, 0.0, 0.0),

(0.5, 1.0, 0.0),

(1.0, 0.5, 1.0))}

def display(probs):
    my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)
    
    pcolor(probs,cmap=my_cmap)
    
    colorbar()
    
    
    # without the line below, the figure won't show
    
    pylab.show()
    
display(probs)