import matplotlib.pyplot as plt
import numpy as np
import math
import time
import random
from PIL import Image
from numba import jit

@jit
def julia(x0,xn,y0,yn,c0,xres,yres,maxiteration):
    Re=np.linspace(x0,xn,xres)
    Im=np.linspace(y0,yn,yres)
    narray=np.zeros((xres,yres))
    for i in range(xres):
        for j in range(yres):
            z = complex(Re[i],Im[j])
            c = c0
            for n in range(maxiteration):
                if abs(z)>2:
                    narray[i,j]=n
                    break
                z=z*z+c
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

def juliaplot(x0,xn,y0,yn,z0,xres,yres,maxiteration):
    Re,Im,narray = julia(x0,xn,y0,yn,z0,xres,yres,maxiteration)
    rarray,garray,barray=randrgb(maxiteration)
    juliaplot = Image.new('RGB', (xres, yres))
    pixels = juliaplot.load()
    for i in range(xres):
        for j in range(yres):
            n=np.int(narray[i,j])
            r=np.int(rarray[n])
            g=np.int(garray[n])
            b=np.int(barray[n])
            pixels[i, j] = (r, g, b)
        print(i)
    return(Re,Im,juliaplot)

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




# # Minibrot Set
# x=-1.180666267
# y=0.2546776795
# dx=0.000000004
# dy=0.0000000035
# xdim=1000

# # zoom3
# x=0.3515290137
# y=-0.0844108699
# dx= 0.000000001
# dy=-0.000000001
# xdim=500

# # zoom4
# x=-0.180471021
# y=-0.666387233
# dx= 0.001
# dy=-0.001
# xdim=500

# #comparejulia1
# x=-0.745508128
# y=0.138382865
# dx= 0.0000001
# dy= 0.0000001
# xdim=500

# # Minibrot Set
# x=-1.180666267
# y=0.2546776795
# dx=0.000000004
# dy=0.0000000035
# xdim=500

# x=-0.12
# y=-0.75
# dx=1.2
# dy=1.2
# xdim=500

# # Minibrot Set
# x=-1.180666267
# y=0.2546776795
# dx=0.000000004
# dy=0.0000000035
# xdim=500

# # Seahorse Valley
# y=0
# x=-0.75
# dx=1.25
# dy=1.5
# xdim=2000


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
#
#
# y0=y+dy
# yn=y-dy
# x0=x-dx
# xn=x+dx
#
#
# xres,yres=scaleres(x0,xn,y0,yn,xdim)
#
#
# Re,Im,graph = juliaplot(x0,xn,y0,yn,complex(x,y),xres,yres,10000)
# #Re,Im,graph = juliaplot(-2.0,0.5,-1.25,1.25,0,1000,1000,2000)
# graph.show()
# graph.save('Juliargb-0.217721255+0.536584429idelta0.001.png')

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
    Re, Im, graph = juliaplot(x0, xn, y0, yn, complex(0.167,-0.686), xres, yres, 1000)

    end_time = time.time()

    totaltime = end_time - start_time
    timevec.append(totaltime)
    points=xres*yres
    pointsvec.append(points)


plt.title("Time complexity for Julia set")
plt.xlabel("Pixels Plotted")
plt.ylabel("Time")
plt.plot(pointsvec[1:],timevec[1:])
plt.savefig('newjuliatime.png', dpi = 400)

plt.show()