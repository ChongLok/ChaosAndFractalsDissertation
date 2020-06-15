import matplotlib.pyplot as plt
import numpy as np
import math
import time
import random
from PIL import Image
from numba import jit

@jit
def mandel(x0,xn,y0,yn,z0,xres,yres,maxiteration):
    Re=np.linspace(x0,xn,xres)
    Im=np.linspace(y0,yn,yres)
    narray=np.zeros((xres,yres))
    for i in range(xres):
        for j in range(yres):
            zdata = []
            c = complex(Re[i],Im[j])
            z = z0
            jo=0
            zdata=[]
            for n in range(maxiteration):
                zdata.append(np.round(abs(z), decimals=50))
                z = z * z + c
                if len(np.unique(zdata[:-1])) == len(np.unique(zdata)):
                    zdata = []
                    period = n - jo
                    jo = period
                    narray[i,j]=period
                    print("repeated value with period:", period - 1)
                    break
        print(i)
    print(narray)
    return(Re,Im,narray)

@jit
def randrgb(maxiteration):
    np.random.seed(2)
    rarray = np.zeros(maxiteration)
    garray = np.zeros(maxiteration)
    barray = np.zeros(maxiteration)
    for i in range(maxiteration):
        rarray[i] = np.random.randint(0, 255)
        garray[i] = np.random.randint(0, 255)
        barray[i] = np.random.randint(0, 255)
    # rarray=np.linspace(255,0,20)
    # garray=np.linspace(0,0,20)
    # barray=np.linspace(0,255,20)
    rarray[0]=0
    garray[0]=0
    barray[0]=0
    return(rarray,garray,barray)

def gradientcolor1(maxiteration):
    r0=255
    g0=255
    b0=255
    rn=0
    gn=0
    bn=255
    rarray=np.linspace(r0,rn,maxiteration)
    garray=np.linspace(g0,gn,maxiteration)
    barray=np.linspace(b0,bn,maxiteration)
    rarray[0]=0
    garray[0]=0
    barray[0]=0
    return(rarray,garray,barray)

def mandelplot(x0, xn, y0, yn, z0, xres, yres, maxiteration):
        Re, Im, narray = mandel(x0, xn, y0, yn, z0, xres, yres, maxiteration)
        rarray, garray, barray = randrgb(maxiteration)
        #rarray, garray, barray = gradientcolor1(maxiteration)
        mandelplot = Image.new('RGB', (xres, yres))
        pixels = mandelplot.load()
        for i in range(xres):
            for j in range(yres):
                n = np.int(narray[i, j])
                r = np.int(rarray[n])
                g = np.int(garray[n])
                b = np.int(barray[n])
                pixels[i, j] = (r, g, b)
            print(i)
        return (Re, Im, mandelplot)

def dpiconverter(x0,xn,y0,yn,dpi):
    xres=np.int(abs(x0-xn)*dpi)
    yres=np.int(abs(y0-yn)*dpi)
    return(xres,yres)

# Scales yres to the correct resolution so that the image does not become distorted
def scaleres(x0,xn,y0,yn,xdim):
    scalefactor = abs(np.int(xdim/(xn-x0)))
    xres = xdim
    yres = abs(np.int((yn-y0)*scalefactor))
    return(xres,yres)

    rarray[0]=0
    garray[0]=0
    barray[0]=0

# #Seahorse
# y=0.353229382
# x=-0.695110825
# dx=0.04
# dy=0.035
# xdim=1000

# # Seahorse Valley
# y=0
# x=-0.75
# dx=1.25
# dy=1.5
# xdim=2000

# # Minibrot Set
# x=0
# y=0
# dx=1
# dy=1
# xdim=100

# # zoom3
# x=0.3515290137
# y=-0.0844108699
# dx= 0.000000001
# dy=-0.000000001
# xdim=2500

# # zoom4
# x=-0.180471021
# y=-0.666387233
# dx= 0.0001
# dy=-0.0001
# xdim=2500

# zoom4
x=-0.180471021
y=-0
dx= 0.2
dy=-0.001
xdim=2500

y0=y+dy
yn=y-dy
x0=x-dx
xn=x+dx

xres,yres=scaleres(x0,xn,y0,yn,xdim)

# xres,yres=dpiconverter(x0,xn,y0,yn,10000)

Re,Im,graph = mandelplot(x0,xn,y0,yn,0,xres,yres,50)
#Re,Im,graph = mandelplot(x-d,x+d,y-d,y+d,0,1000,1000,1000)
#Re,Im,graph = mandelplot(-2.0,0.5,-1.25,1.25,0,1000,1000,2000)
graph.show()
#graph.save('mandelzoom3rgb.png')