import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import groupby
def graph(a, x, n):

    X = np.linspace(0, 1, 10000) # linearly spaced numbers
    y = a * X * (1 - X)
    plt.plot(X, y)
    y = X
    plt.plot(X, y,color='black')

    counter = 0
    xdata = [x]
    while n > counter:
        x = a * x * (1 - x)
        xdata.append(x)
        counter += 1

    xplot = []
    counter = 0
    while (len(xdata) - 1) > counter:
        xplot.append(xdata[counter])
        xplot.append(xdata[counter])
        counter += 1

    yplot = [0]
    counter = 0
    while (len(xdata) - 2) > counter:
        yplot.append(xdata[counter+1])
        yplot.append(xdata[counter+1])
        counter += 1
    yplot.append(xdata[len(xdata)-1])

    return(xplot,yplot)

steps = 100
xp=np.linspace(0,1,steps)
for i in range(steps):
    print(xp[i])
    x,y=graph(3.6, xp[i], 50)
    plt.plot(x,y)
    plt.draw()
    plt.pause(0.0000001)
    plt.clf()
