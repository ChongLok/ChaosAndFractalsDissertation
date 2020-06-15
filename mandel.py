import matplotlib.pyplot as plt
import numpy as np
import math
import time
from PIL import Image
from numba import jit

def mandel(x0,xn,y0,yn,z0,xres,yres):
    #start_time = time.time()
    res = [xres, yres]
    mandelplot=Image.new('RGB', ((res[0]), (res[1])))
    pixels=mandelplot.load()
    Re=np.linspace(x0,xn,res[0])
    Im=np.linspace(y0,yn,res[1])
    xcounter=0
    ycounter=0
    maxiteration=255
    for i in Re:
        for j in Im:
            c = complex(i,j)
            z = z0
            n=0
            while n < maxiteration:
                if abs(z)>2:
                    r=255-n
                    g=r
                    b=255
                    pixels[xcounter,ycounter]=(r,g,b)
                    break
                z=z*z+c
                n+=1
            ycounter += 1
        xcounter+=1
        ycounter=0
        print(xcounter)

    mandelplot.show()
    #mandelplot.save('mandelbrottest.png')

    #end_time = time.time()
    #totaltime = end_time - start_time
    #print("Total execution time: {}".format(totaltime))
    #return (totaltime)

#mandel(-1.79,-1.744,-0.023,0.023,0,500,500)
mandel(-1.5,1.5,-1.5,1.5,0,100,100)

# stepsize=np.arange(start=100,stop=1000,step=2)
# totaltimevec=[]
# for i in stepsize:
#     totaltime = mandel(-2,2,-2,2,0,i,i)
#     totaltimevec.append(totaltime)
#
# plt.title("Steps against time for Mandelbrot set")
# plt.xlabel("Points plotted")
# plt.ylabel("Time")
# plt.plot(stepsize*stepsize,totaltimevec)
# plt.savefig('feigentime-400.png', dpi = 400)
# plt.show()