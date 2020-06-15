import matplotlib.pyplot as plt
import numpy as np
import math
import time
import random
from PIL import Image
from numba import jit
from matplotlib import pyplot as plt
from matplotlib import colors

def plot1(steps):
    start_time1 = time.time()
    x=np.linspace(100,10000,steps)
    y=np.linspace(100,10000,steps)
    plt.plot(x,y)
    end_time1 = time.time()
    totaltime1 = end_time1 - start_time1
    plt.clf()
    return(totaltime1)

def plot2(steps):
    start_time2 = time.time()
    x=np.linspace(100,10000,steps)
    y=np.linspace(100,10000,steps)
    for i in range(steps):
        plt.plot(x[i],y[i])
    end_time2 = time.time()
    totaltime2 = end_time2 - start_time2
    plt.clf()
    return(totaltime2)




time1=[]
time2=[]
x=[]
for j in range(1,500):
    x.append(j)
    a = plot1(j)
    b = plot2(j)
    time1.append(a)
    time2.append(b)
    print(j)
print(time1,time2,x)

plt.legend()
plt.title("Plotting vs time")
plt.xlabel("Size of plotting vector")
plt.ylabel("Time")

first, = plt.plot(x,time1,label='Plotting whole vector')
second, = plt.plot(x,time2,label='Plotting points')

print(first)
plt.legend()
plt.savefig('efficiency-400.png', dpi = 400)
plt.show()
