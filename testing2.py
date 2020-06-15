import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.zeros(10000)
y=np.zeros(10000)
z=np.zeros(10000)
for i in range (10000):
    x[i],y[i],z[i]=np.random.randint(-1000,1001),np.random.randint(-1000,1001),np.random.randint(-1000,1001)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x,y,z, c='r',marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()