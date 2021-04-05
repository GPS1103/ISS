"""
General idea: solve recursively from n = 0 to N where N = number of iterations derived from time / Tp
If spare time is found, try going from N to 0 to see how much memory its gonna hog
Starting conditions (can be changed later):

h(0) = h0
h(n+1) = 1/A*(-1*Beta*math.sqrt(h(n))+Qd(n))*Tp+h(n)

where:
A = area of the bottom of the container
Beta = runoff coefficient, for explanation see page 12 of ISS lab 1 presentation
Qd = flow input
Q0 = flow output
Tp = sampling time
h = liquid level inside of container
"""

import math

#main

#parameters

#Area in m^2
A = 10
#runoff coefficient, in m^(5/2)/s
Beta = 0.005
#Flow in in m^3/s, our input variable
Qd = 0.05
#Liquid height during steps, h(0) is the starting condition, in m
h = [5]
from pprint import pprint
print(len(h))
#Sampling time/step time
Tp = 0.1
#in hours
SimulationLength = 1

#constraints
hMax = 20               #maximum length of container in meters

#1: calculate number of iterations

#2:loop
def run(A, Beta, Qd, H, Tp, SimulationLength, hMax):
    print(A, Beta, Qd, H, Tp, SimulationLength, hMax)
    iterations = int(3600 * SimulationLength / Tp)
    #h=[H]
    for n in range(iterations + 1):
        #print("Value: ", n)  #yay, works, 36k iterations
    #     #skip step n = 0
        # if (n == 0):
        #     continue
        # print(h[n-1])
        #hNext = (1/A*(-1*Beta*math.sqrt(h[n-1])+Qd)*Tp+h[n-1])
    #     if hNext > hMax:
    #         print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n*Tp, ' s.')
    #         break
    #         #raise ValueError('Try setting different parameters')
    #     h.append(hNext)
        #print(hNext)
    #     if (hNext != result):
    #         result = round(hNext, 2)
    #         print(round(hNext, 2))

print('WaterContainer1.py loaded!')