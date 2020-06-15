import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import groupby
def graph(a, x1,x2, n):

    X = np.linspace(0, 1, 10000) # linearly spaced numbers
    y = a * X * (1 - X)
    plt.plot(X, y)
    y = X
    plt.plot(X, y,color='black')

    counter = 0
    xdata = [x1]
    while n > counter:
        x1 = a * x1 * (1 - x1)
        xdata.append(x1)
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


    plt.plot(xplot[-20:], yplot[-20:],color='lightgreen')



    counter = 0
    xdata = [x2]
    while n > counter:
        x2 = a * x2 * (1 - x2)
        xdata.append(x2)
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


    plt.plot(xplot[-20:], yplot[-20:],color='lightblue')



    plt.title("Cobweb Plot(3.8*x*(1-x)")
    plt.xlabel("x")
    plt.ylabel("3.8*x*(1-x)")


    plt.savefig('cobwebchaos38at03and030001last-400dpi.png', dpi = 400)
    plt.show()
    return



graph(3.8, 0.3, 0.30001, 200)