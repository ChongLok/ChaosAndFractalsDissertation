import numpy as np
import math

def feigeniterator(A,x0,steps):
    x=x0
    for i in range(steps+1):
        print(np.round(x,decimals=5),i)
        x=A*x*(1-x)
    return()

def mandeliterator(z0,c,steps):
    z=z0
    zdata=[]
    j=0
    for i in range(steps+1):
        print(np.round(abs(z),decimals=5),i)
        zdata.append(np.round(abs(z),decimals=5))
        z=z*z+c
        if len(np.unique(zdata[:-1]))==len(np.unique(zdata)):
            zdata=[]
            period=i-j
            j = i
            print("repeated value with period:",period-1)
    return()

mandeliterator(0,complex(-1.35,0.23),110)