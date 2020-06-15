import matplotlib.pyplot as plt
import numpy as np
import math
import time
import random
from PIL import Image
from numba import jit

def mandel(z0,c,steps):
    z=np.zeros(steps+1,dtype=complex)
    z[0]=z0
    for i in range(steps):
        z[i+1]=z[i]*z[i]+c
    return(z)



c=complex(-0.12,0.75)
z0=complex(0,0)
z=mandel(z0,c,1000)

plt.figure(figsize=(6,6))

plt.plot(z.real,z.imag)
plt.plot(z.real,z.imag,'ro')

plt.title("Argand Diagram")
plt.xlabel("Real")
plt.ylabel("Imaginary")

# plt.axis('scaled')

#plt.savefig('argandjulia'+str(c.real)+'+'+str(c.imag)+'i-400.png', dpi = 400)
plt.savefig('argandmandel'+str(c.real)+'+'+str(c.imag)+'i-400.png', dpi = 400)
plt.show()