import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import groupby
import time
from numba import jit

@jit

def logistic(A, x0, n):
    x = np.zeros(n)
    x[0]=x0
    for i in range(n):
        x[i+1] = A*x[i]*(1-x[i])
        #x[i+1] = A*x[i]*x[i]*(1-x[i])
        #x[i+1] = A*x[i]*x[i]*math.sin(math.pi*x[i])
        #x[i + 1] = x[i] * x[i] + A * x[i] - 2 * x[i]
        #x[i + 1] = (x[i] - A)*(x[i] * x[i] + A * A - 1) * (x[i] * x[i] + A * A - 4)
        #x[i+1]=x[i]+A
        #x[i+1]=x[i]*x[i]+A
        #x[i + 1] = A * x[i] * x[i] * x[i] * (1 - x[i])
    return(x)

@jit
def feigen(a, b, steps, x0, n):
    A = np.linspace(a, b, steps)
    x = np.zeros((steps, n))
    print(A)
    for i in range(steps):
        x[i,:] = logistic(A[i], x0, n)
    return(x,A)

def plottingdata(a, b, steps, x0, n):
    xconverged = []
    aconverged = []
    xdiverged = []
    adiverged = []
    x, A = feigen(a, b, steps, x0, n)
    numdivpoints = np.int(n * 0.01)
    numconpoints = np.int(100)

    for i in range(steps):
        uniquevalues = np.unique(x[i])
        if len(uniquevalues) == n:
            adiv = np.ones(numdivpoints) * A[i]
            xdiverged = np.concatenate((xdiverged, x[i][-numdivpoints:]))
            adiverged = np.concatenate((adiverged, adiv))

        if len(uniquevalues)!=n:
            xconverged = np.concatenate((xconverged, x[i][-numconpoints:]))
            acon = np.ones(numconpoints) * A[i]
            aconverged = np.concatenate((aconverged, acon))
    return(xconverged,aconverged,xdiverged,adiverged)

# start_time = time.time()
#
# xcon, acon, xdiv, adiv = plottingdata(1, 2.326, 50000, 0.5, 10000)
#
# plt.plot(acon, xcon, color='blue', marker=',', linestyle='None')
# plt.plot(adiv, xdiv, color='red', marker=',', linestyle='None')
#
# end_time = time.time()
# totaltime = end_time-start_time
#
# plt.title("Feigenbaum Plot (A*x*sin(pi*x)))")
# plt.xlabel("Value of A")
# plt.ylabel("Converged values of x")
# #plt.savefig('feigensine2to2326-400.png', dpi = 400)
# print("Total execution time: {}".format(totaltime))
# plt.show()



#Time complexity graph
steps=199
x=np.linspace(1000,10000,steps)
n=10000
timevec=[]
pointsvec=[]
for i in range(steps):
    start_time = time.time()

    xcon, acon, xdiv, adiv = plottingdata(1, 4, i, 0.5, n)
    plt.plot(acon, xcon, color='blue', marker=',', linestyle='None')
    plt.plot(adiv, xdiv, color='red', marker=',', linestyle='None')

    plt.title("Feigenbaum Plot")
    plt.xlabel("Value of A")
    plt.ylabel("Converged values of x")

    end_time = time.time()

    totaltime = end_time - start_time
    timevec.append(totaltime)
    points=x[i]*n
    pointsvec.append(points)
    plt.clf()

plt.title("Time complexity for Feigenbaum Diagram")
plt.xlabel("Number of Steps * Number of Iterations")
plt.ylabel("Time")
plt.plot(pointsvec[1:],timevec[1:])
plt.savefig('newfeigentime.png', dpi = 400)

plt.show()
