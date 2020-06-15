import matplotlib.pyplot as plt
import numpy as np
import math
from itertools import groupby
import time


def feigenbaum(a, b, h, n, x0):
    start_time = time.time()

    xplotconverged=[] #Final plotting vector for converged values of x
    xplotdiverged=[] #Final plotting vector for diverged values of x
    aplotconverged=[] #Final plotting vector of A for converged values of x
    aplotdiverged=[] #Final plotting vector of A for diverged values of x

    while a < b: #iterating all values of a less than number
        xdata=[]
        x = x0 #initial value of x at start of iteration (x0)
        xloop = 0
        count = n-500
        xconvergedvalues=[] #Current converged values of x for a given A value
        xdivergedvalues=[] #Current diverged values of x for a given A value

        while xloop < n: #iterating x
            #x = a * x * (1 - x) # 0 < x < 4
            #x = a * x * x * (1 - x) # 4 < x < 7
            #x = a * x * x * (1 - x)
            x=x*x+a*x-2*x
            xloop += 1
            xdata.append(x)



        for q, p in groupby(sorted(xdata)): #Finding all converged values of x and saving to xconvergedvalues
            if len(list(p)) > 1:
                xconvergedvalues.append(q)

        if len(xconvergedvalues) > 0:
            xplotconverged = xplotconverged + xconvergedvalues
            aplotconverged = aplotconverged + [a]*len(xconvergedvalues)


        if len(xconvergedvalues) == 0:
            while count < n:
                xdivergedvalues.append(xdata[count])
                count += 1
            xplotdiverged = xplotdiverged + xdivergedvalues
            aplotdiverged = aplotdiverged + [a]*len(xdivergedvalues)

        print("Value of A: ", a, "\nConverged Values: ", xconvergedvalues, "\nDiverged Values: ", sorted(xdivergedvalues))
        a += h

    end_time = time.time()
    totaltime=end_time-start_time
    print("Total execution time: {}".format(totaltime))

    plt.plot(aplotconverged, xplotconverged, color='blue', marker=',', linestyle='None')
    plt.plot(aplotdiverged, xplotdiverged, color='red', marker=',', linestyle='None')

    #axes = plt.gca()
    #axes.set_ylim([0.497, 0.503])

    plt.title("Feigenbaum Plot")
    plt.xlabel("Value of A")
    plt.ylabel("Converged values of x")
    #
    # #plt.savefig('feigen3to4-400.png', dpi = 400)
    # #plt.savefig('feigen3to4-600.png', dpi = 600)
    # #plt.savefig('feigen3to4-800.png', dpi = 800)
    #
    # #plt.savefig('feigen34to36792-400.png', dpi = 400)
    # #plt.savefig('feigen384to3858-400.png', dpi = 400)
    #
    # #plt.savefig('feigensine2to2326-400.png', dpi = 400)
    # #plt.savefig('feigenlogisticx52to65-400.png', dpi = 400)
    #
    plt.show()
    return(totaltime)

# stepsize=np.linspace(0.01,0.001,100)
# totaltimevec=[]
# for i in stepsize:
#     totaltime = feigenbaum(1, 4, i, 1000, 0.5)
#     totaltimevec.append(totaltime)
#
# plt.title("Steps against time for Feigenbaum diagram")
# plt.xlabel("Number of steps")
# plt.ylabel("Time")
# plt.plot(4/stepsize,totaltimevec)
# plt.savefig('feigentime-400.png', dpi = 400)
# plt.show()

totaltime = feigenbaum(0,4,0.01,1000,0.5)
print("Total execution time: {}".format(totaltime))