import matplotlib.pyplot as plt
import numpy as np
import math
import time
from PIL import Image



def julia(x0,xn,y0,yn,c,xres,yres,maxiteration):
    start_time = time.time()
    res = [xres, yres]
    juliaplot=Image.new('RGB', ((res[0]), (res[1])))
    pixels=juliaplot.load()
    Re=np.linspace(x0,xn,res[0])
    Im=np.linspace(y0,yn,res[1])
    xcounter=0
    ycounter=0
    for i in Re:
        for j in Im:
            z = complex(i,j)
            n=0
            while n < maxiteration:
                if abs(z)>2:
                    r=maxiteration-n
                    g=r
                    b=maxiteration
                    pixels[xcounter,ycounter]=(r,g,b)
                    break
                z=z*z+c
                n+=1
            ycounter += 1
        xcounter+=1
        ycounter=0
        print(xcounter)

    juliaplot.show()

    end_time = time.time()
    print("Total execution time: {}".format(end_time - start_time))

    juliaplot.save('juliatest3.png')
julia(1.3,-1.3,1.3,-1.3,complex(-0.75,0.1),2000,2000,255)

