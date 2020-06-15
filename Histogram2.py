import matplotlib.pyplot as plt
import numpy as np
import math
import time
import random
from PIL import Image
from numba import jit
from matplotlib import pyplot as plt
from matplotlib import colors

def histogram(x0,xn,A,steps,decimal,maxiteration):
    xvec=np.linspace(x0,xn,steps)
    n=np.zeros(steps)
    for i in range(steps):
        print(i)
        xdata = []
        x=np.round(xvec[i],decimals=decimal)
        xdata.append(x)
        for j in range(maxiteration-1):
            x=A*x*(1-x)
            x=np.round(x,decimals=decimal)
            xdata.append(x)
            if len(np.unique(xdata))==len(np.unique(xdata[:-1])): #Testing for repeated value in vector
                n[i] = j
                break
    return(n,xvec)


y,x=histogram(0.6,0.7,3.2,1001,10,1000)
print(x)
print(y)
plt.title("Speed of Convergence for Logistic Operator at A=3.2")
plt.xlabel("Initial Value")
plt.ylabel("Number of iterations to reach 10 dp accuracy")
plt.plot(x,y)
#plt.savefig('histconvlogistic355-400dpi.png', dpi = 400)
plt.show()