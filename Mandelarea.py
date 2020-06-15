import matplotlib.pyplot as plt
import numpy as np
import math
import time
import random
from PIL import Image
from numba import jit

@jit
def mandelarea(x0,xn,y0,yn,z0,xres,yres,maxiteration):
    Re=np.linspace(x0,xn,xres)
    Im=np.linspace(y0,yn,yres)
    count=0
    for i in range(xres):
        for j in range(yres):
            c = complex(Re[i],Im[j])
            z = z0
            for n in range(maxiteration):
                if abs(z)>2:
                    count += 1
                    break
                z=z*z+c
        print(i)
    converged=(xres*yres)-count
    points=abs(xres*yres)
    pixelarea=(abs(x0-xn)*abs(y0-yn))/points
    area=pixelarea*converged
    return(area,points,converged)

# Scales yres to the correct resolution so that the image does not become distorted
def scaleres(x0,xn,y0,yn,xdim):
    scalefactor = abs(np.int(xdim/(xn-x0)))
    xres = xdim
    yres = abs(np.int((yn-y0)*scalefactor))
    return(xres,yres)


x=0
y=-0
dx=2
dy=2
xdim=200000

y0=y+dy
yn=y-dy
x0=x-dx
xn=x+dx

xres, yres = scaleres(x0, xn, y0, yn, xdim)
points, area, converged = mandelarea(x0, xn, y0, yn, 0, xres, yres, 50000)
print(points,area)


# Points vs Area
# x=np.linspace(100,10000,51)
# pointsvector=[]
# areavector=[]
# convergedvector=[]
# for i in range(51):
#     xdim=np.int(x[i])
#     xres, yres = scaleres(x0, xn, y0, yn, xdim)
#     points, area, converged = mandelarea(x0, xn, y0, yn, 0, xres, yres, 2000)
#     pointsvector.append(points)
#     areavector.append(area)
#     convergedvector.append(converged)
#     print(pointsvector,areavector,convergedvector)
# plt.plot(areavector,pointsvector)
# plt.title("Area of Mandelbrot Set")
# plt.xlabel("Points calculated")
# plt.ylabel("Area")
# plt.savefig('mandelarea-400.png', dpi = 400)
#
#
# plt.show()
