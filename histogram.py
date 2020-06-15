import matplotlib.pyplot as plt
import numpy as np
import math
import time
import random
from PIL import Image
from numba import jit
from matplotlib import pyplot as plt
from matplotlib import colors
A = 2.9 # A value for logistic operator

a = 0 # x start value
b = 1 # x end value
h = 0.001 # x step size
limit = 0.01 # convergence limit
xplot = []
yplot = []

while a <= b:
    counter = 0
    x = a
    delta = 10000000
    while delta > limit:
        xn = x
        x = A * x * (1 - x)
        delta = abs(xn - x)
        counter += 1
        print(counter)
    xplot.append(a)
    yplot.append(counter)

    a = a + h

plt.plot(xplot,yplot)
print(xplot)
print(yplot)
plt.show()