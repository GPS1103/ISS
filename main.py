"""
General idea: solve recursively from n = 0 to N where N = number of iterations
derived from time / Tp
If spare time is found, try going from N to 0 to see how much memory its gonna
hog
Starting conditions (can be changed later):

h(0) = h0
h(n+1) = 1/A*(-1*Beta*math.sqrt(h(n))+Qd(n))*Tp+h(n)

where:
A = area of the bottom of the container
Beta = runoff coefficient, for explanation see page 12 of ISS lab 1
presentation
Qd = flow input
Q0 = flow output
Tp = sampling time
h = liquid level inside of container
"""

import math

# main

# parameters
# Area in m^2
A = 10
# runoff coefficient, in m^(5/2)/s
Beta = 0.005
# Flow in in m^3/s, our input variable
Qd = 0.05
# Liquid height during steps, h(0) is the starting condition, in m
h = [5]
# Sampling time/step time
Tp = 0.1
# in hours
SimulationLength = 1

# constraints
hMax = 20  # maximum length of container in meters

# 1: calculate number of iterations
iterations = int(3600 * SimulationLength / Tp)

f = open("dump.txt", "w")
f.write("water level over time:\n")

# 2:loop
f.write(str(h[0]))
f.write("\n")
for n in range(iterations + 1):
    # print("Value: ", n)  #yay, works, 36k iterations
    # skip step n = 0
    if (n == 0):
        continue
    hNext = 1/A*(-1*Beta*math.sqrt(h[n-1])+Qd)*Tp+h[n-1]
    if hNext > hMax:
        print('Container overflowed! Happened at iteration = ',
              n, ' equal to time =', n*Tp, ' s.')
        f.write("Error, overfilled!\n")
        f.close()
        break
        # raise ValueError('Try setting different parameters')
    h.append(hNext)
    print(hNext)
    f.write(str(hNext))
    f.write("\n")
f.close()
