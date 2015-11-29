#!/home/caiy/anaconda/bin/python

import numpy as np
import pandas as pd
from pylab import *
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
from matplotlib.patches import Rectangle

from sys import argv
import sys, getopt
import os

 
def set_pub():
    rc('font', weight='bold')    # bold fonts are easier to see
    rc('ytick', labelsize=15)     # tick labels bigger
    rc('xtick', labelsize=15)
    #rc('lines', lw=1, color='k') # thicker black lines (no budget for color!)
    #rc('grid', c='0.5', ls='-', lw=0.5)  # solid gray grid lines
    rcParams['figure.figsize']=8,8
    rc('savefig', dpi=300)       # higher res outputs

set_pub()

script, seed = argv
print seed
print str(seed)
df=pd.DataFrame(np.random.randn(13,5), columns=list('ABCDE'))
xs =df['A']
ys =df['B']
#colors=df['C']**2
area=np.pi*(13*df['D'])**2
N =len(xs)
hs=df['E']

#cmap=plt.cm.hot

ax =figure(facecolor='#589A5F').add_subplot(111,aspect='equal')
for x,y,h in zip(xs,ys,hs):
    #print x,y,h
    #ax.add_artist(Rectangle(xy=(x,y),color=np.random.rand(4,1),alpha=0.5,width=h,height=h))
    ax.add_artist(Rectangle(xy=(x,(1-x)),color=np.random.rand(4,1),alpha=0.5,width=h,height=h))
   # ax.add_artist(Circle(xy=(x,y),color=np.random.rand(4,1), radius=10,alpha=0.2)
ax.set_axis_bgcolor('#589A5F')
#plt.show()

savefig("rectangle_scatter"+str(seed)+".png",  figsize=(8, 8), dpi=300, facecolor='black',transparent=True, edgecolor='none', orientation='portrait', papertype=None, format=None,   bbox_inches=None, pad_inches=0.1, frameon=None)

