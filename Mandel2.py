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
            c = complex(Re[i],Im[j])
            z = z0
            for n in range(maxiteration):
                if abs(z)>2:
                    narray[i,j]=n
                    break
                z=(z*c-1)**2-1
        print(i)
    print(narray)
    return(Re,Im,narray)

@jit
def randrgb(maxiteration):
    np.random.seed(2)
    rarray = np.zeros(maxiteration)
    garray = np.zeros(maxiteration)
    barray = np.zeros(maxiteration)
    for i in range(1,maxiteration):
        rarray[i] = np.random.randint(0, 255)
        garray[i] = np.random.randint(0, 255)
        barray[i] = np.random.randint(0, 255)
    # rarray=np.linspace(255,0,20)
    # garray=np.linspace(0,0,20)
    # barray=np.linspace(0,255,20)
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
# dy=0.04
# xdim=1000

# # Seahorse Valley
# y=0
# x=-0.75
# dx=1.25
# dy=1.5
# xdim=2000

# # Minibrot Set
# x=-1.180666267
# y=0.2546776795
# dx=0.000000004
# dy=0.0000000035
# xdim=500

# # zoom3
# x=0.3515290137
# y=-0.0844108699
# dx= 0.000000001
# dy=-0.000000001
# xdim=500

# # zoom4
# x=-0.180471021
# y=-0.666387233
# dx= 0.0001
# dy=-0.0001
# xdim=500

# # mandelfeigen
# x=0
# y=-0
# dx=2
# dy=2
# xdim=10000

# # 3 Period Bulb
# x=-0.1
# y=0.9
# dx=0.26
# dy=0.26
# xdim=1000

# # 4 Period Bulb
# x=0.31
# y=0.59
# dx=0.12
# dy=0.12
# xdim=1000

# #comparemandel1
# x=-0.745508128
# y=0.138382865
# dx= 0.00000001
# dy= 0.00000001
# xdim=500

# #Relationship between M and J set 1
# x=-0.023243358
# y=0.764099709
# dx=0.0005
# dy=0.0005
# xdim=2000

# #Relationship between M and J set 2
# x=-0.744382065
# y=0.121243871
# dx=0.001
# dy=0.001
# xdim=2000

# #Relationship between M and J set 3
# x=0.217721255
# y=0.536584429
# dx=0.001
# dy=0.001
# xdim=2000

# x=-1
# y=0
# dx=1.5
# dy=1.5
# xdim=10000
#
#
# y0=y+dy
# yn=y-dy
# x0=x-dx
# xn=x+dx
#
# xres,yres=scaleres(x0,xn,y0,yn,xdim)
#
# # xres,yres=dpiconverter(x0,xn,y0,yn,10000)
#
# Re,Im,graph = mandelplot(x0,xn,y0,yn,-1,xres,yres,1000)
# #Re,Im,graph = mandelplot(x-d,x+d,y-d,y+d,0,1000,1000,1000)
# #Re,Im,graph = mandelplot(-2.0,0.5,-1.25,1.25,0,1000,1000,2000)
# graph.show()
# #graph.save('mandelseahorsergb.png')








#Time complexity graph

x=0
y=0
dx=2
dy=2
y0=y+dy
yn=y-dy
x0=x-dx
xn=x+dx

steps=50
x=np.linspace(1000,5000,steps)
timevec=[]
pointsvec=[]
for i in range(steps):
    start_time = time.time()

    xres,yres=scaleres(x0,xn,y0,yn,np.int(x[i]))
    Re, Im, graph = mandelplot(x0, xn, y0, yn, 0, xres, yres, 1000)

    end_time = time.time()

    totaltime = end_time - start_time
    timevec.append(totaltime)
    points=xres*yres
    pointsvec.append(points)


plt.title("Time complexity for Mandelbrot set")
plt.xlabel("Pixels Plotted")
plt.ylabel("Time")
plt.plot(pointsvec[1:],timevec[1:])
plt.savefig('newmandeltime.png', dpi = 400)

plt.show()
