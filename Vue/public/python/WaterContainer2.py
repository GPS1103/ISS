"""
General idea: solve with iterations from n = 0 to N where N = number of iterations derived from time / Tp
If spare time is found, try going from N to 0 to see how much memory its gonna hog
Starting conditions (can be changed later):

V(0)=V0
V(n+1)=(Qd1(n)+Qd2(n)-Q0(n))*Tp+V(n)
c(0)=c0
c(n+1)=(Qd1(n)*(cd1(n)-c(n))+Qd2(n)*(cd2(n)-c(n)))*Tp/V(n)+c(n)

where:
c   = concentration of ingredient
Qd = inflow of # ingredient
Qo  = outflow of solution
V   = volume of solution
"""

import time
#import matplotlib.pyplot as plt


def runWaterContainer2(v, c, QD1, QD2, QO, cd1, cd2, Tp, simulationLength):
    cMax = 1
    c=c/100
    cd1 = cd1/100
    cd2 = cd2/100
    print(v, c, QD1, QD2, QO, cd1, cd2, Tp, simulationLength)
    iterations = int((3600 * simulationLength) / Tp)
    V = [v]
    c = [c]
    print(iterations)
    tic = time.time()
    # 2:loop
    for n in range(iterations + 1):
        # all of unchanging constants have been swapped for direct indexes
        VNext = (QD1 + QD2 - QO) * Tp + V[n]
        # if VNext > vMax:
        # print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
        # return [V, c]
        if VNext < 0:
            print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            for i in range(len(c)):
                c[i] = c[i]*100
            return [V, c]
        cNext = (QD1 * (cd1 - c[n]) + QD2 * (cd2 - c[n])) * Tp / V[n] + c[n]
        if cNext > cMax:
            print('Container too concentrated! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            for i in range(len(c)):
                c[i] = c[i]*100
            return [V, c]
        if cNext < 0:
            print('Container at negative concentration! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            for i in range(len(c)):
                c[i] = c[i]*100
            return [V, c]
        V.append(VNext)
        c.append(cNext)
        if n == iterations - 1:
            toc = time.time()
            print("Run script: ", toc - tic)
            print('finisz')
            """
            plt.plot(V)
            plt.plot(c)
            plt.ylabel('V[m^3] and c[1]')
            plt.axis([0, iterations, 0, max(V)])
            plt.show()
            """
            for i in range(len(c)):
                c[i] = c[i]*100
            return [V, c]


# runWaterContainer2(10, 0.2, 1, 5, 6.003, 0.5, 0.89, 1, 0.5)
# runWaterContainer2(10, 0.4, 2, 2, 3.99, 0.2, 0.3, 1, 0.5)
"""
    wersja powyżej ma 1 arguemnt mniej (nie sprawdza vNext > vMax bo to latwo zepsuc
    ponizej spodziewa sie jeszcze vMax
"""


# def runWaterContainer2(v, C, QD1, QD2, QO, cd1, cd2, Tp, simulationLength, vMax):
#     cMax = 1
#     print(v, C, QD1, QD2, QO, cd1, cd2, Tp, simulationLength)
#     iterations = int((3600 * simulationLength) / Tp)
#     V = [v]
#     c = [C]
#     print(iterations)
#     tic = time.time()
#     # 2:loop
#     for n in range(iterations + 1):
#         # all of unchanging constants have been swapped for direct indexes
#         VNext = (QD1 + QD2 - QO) * Tp + V[n]
#         # if VNext > vMax:
#         # print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
#         # return [V, c]
#         if VNext < 0:
#             print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
#             return [V, c]
#         if VNext > vMax:
#             print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
#             return [V, c]
#         cNext = (QD1 * (cd1 - c[n]) + QD2 * (cd2 - c[n])) * Tp / V[n] + c[n]
#         if cNext > cMax:
#             print('Container too concentrated! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
#             return [V, c]
#         if cNext < 0:
#             print('Container at negative concentration! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
#             return [V, c]
#         V.append(VNext)
#         c.append(cNext)
#         if n == iterations - 1:
#             toc = time.time()
#             print("Run script: ", toc - tic)
#             print('finisz')
#             return [V, c]


print('WaterContainer2.py loaded!')
# runWaterContainer2(10, 0.2, 5, 5, 7, 0.5, 0.89, 1, 0.5, 100000000)
# runWaterContainer2(10, 0.4, 2, 2, 3.99, 0.2, 0.3, 1, 0.5)
# runWaterContainer2(10, 0.4, 2, 2, 3.99, 0.2, 0.3, 1, 0.5, 250)
