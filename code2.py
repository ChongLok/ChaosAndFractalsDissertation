import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import groupby
import time

def logistic(a0,an,x0,steps,maxiteration):
    n=np.zeros((steps,maxiteration))
    a=np.linspace(a0,an,steps)
    for i in range(steps):
        A=a[i]
        x=0.5
        for j in range(maxiteration):
            n[i,j]=x*A*(1-x)
    return(a,n)

x,n=logistic(0,4,0.5,200,200)

for i in range(200):
    plt.scatter(np.linspace(0,4,200),n[i,:])
plt.show()