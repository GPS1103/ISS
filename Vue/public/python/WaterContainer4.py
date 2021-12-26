"""
General idea: solve recursively from n = 0 to N where N = number of iterations derived from time / Tp
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

#import PIDController as PID_Controller
import time
#import matplotlib.pyplot as plt


# def runWaterContainer4(v, C, QD1, QD2, QO, cd1, cd2, Tp, SimulationLength, target_c, P1, I1, D1, maxInput, vMax):
#     tic = time.time()
#     iterations = int(3600 * SimulationLength / Tp)
#     V = [v]
#     c = [C]
#     Qd1 = []
#     e1 = []
#     u1 = []
#     PID_conc = PID_Controller.PIDController(P1, I1, D1, Tp)
#     for n in range(iterations + 1):
#         e1.append(target_c - c[n])
#         if n == 0:
#             de1 = 0
#         else:
#             de1 = e1[n] - e1[n - 1]
#         if n < 1:
#             dde1 = 0
#         else:
#             dde1 = e1[n] - 2 * e1[n - 1] + e1[n - 2]

#         tmp_u1 = PID_conc.calc_delta_u(de1, e1[n], dde1)
#         if n != 0:
#             tmp_u1 += u1[n - 1]

#         if tmp_u1 > maxInput:
#             u1.append(maxInput)

#         if tmp_u1 < 0:
#             u1.append(0)
#         else:
#             u1.append(tmp_u1)

#         Qd1.append(u1[n])
#         # all of unchanging constants have been swapped for direct indexes
#         VNext = (Qd1[n] + QD2 - QO) * Tp + V[n]
#         if VNext < 0:
#             print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
#             return [V, c]
#         if VNext > vMax:
#             print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
#             return [V, c]
#         cNext = (Qd1[n] * (cd1 - c[n]) + QD2 * (cd2 - c[n])) * Tp / V[n] + c[n]
#         if cNext > 1:
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


# runWaterContainer4(10, 0.1, 1, 1, 1.001, 0.5, 0.1, 1, 0.5, 0.25, 3, 30, 0.1, 5, 100000)


def runWaterContainer4(v, C, QD2, cd1, cd2, target_c, P1, I1, D1, maxInput, vMax, P2, I2, D2, Tp, SimulationLength):
    C=C/100
    cd1=cd1/100
    cd2=cd2/100
    target_c=target_c/100
    tic = time.time()
    iterations = int(3600 * SimulationLength / Tp)
    V = [v]
    c = [C]
    Qd1 = []
    Qo = []
    e1 = [target_c - c[0]]
    u1 = []
    e2 = []
    PID_conc = PIDController(P1, I1, D1, Tp)
    PID_out = PIDController(P2, I2, D2, Tp)
    for n in range(iterations + 1):
        e1.append(target_c - c[n])
        if n == 0:
            de1 = 0
        else:
            de1 = e1[n] - e1[n - 1]
        if n < 1:
            dde1 = 0
        else:
            dde1 = e1[n] - 2 * e1[n - 1] + e1[n - 2]

        tmp_u1 = PID_conc.calc_delta_u(de1, e1[n], dde1)
        if n != 0:
            tmp_u1 += u1[n - 1]

        if tmp_u1 > maxInput:
            u1.append(maxInput)

        if tmp_u1 < 0:
            u1.append(0)
        else:
            u1.append(tmp_u1)

        Qd1.append(u1[n])

        e2.append(V[n] - V[0])
        de2 = e2[n] - e2[n - 1]
        if n < 1:
            dde2 = 0
        else:
            dde2 = e2[n] - 2 * e2[n - 1] + e2[n - 2]

        u2_tmp = PID_out.calc_delta_u(de2, e2[n], dde2)
        if n != 0:
            u2_tmp += Qo[n - 1]

        if u2_tmp < 0:
            u2_tmp = 0
        if u2_tmp > 2*maxInput:
            u2_tmp = 2*maxInput
        Qo.append(u2_tmp)

        VNext = (Qd1[n] + QD2 - Qo[n]) * Tp + V[n]
        if VNext < 0:
            print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            # plt.plot(V)
            # plt.plot(c)
            # plt.ylabel('V[m^3] and c[1]')
            # plt.axis([0, n, 0, max(V)])
            # plt.show()
            for i in range(len(c)):
                c[i] = c[i]*100
            return [V, c]
        if VNext > vMax:
            print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            # plt.plot(V)
            # plt.plot(c)
            # plt.ylabel('V[m^3] and c[1]')
            # plt.axis([0, n, 0, max(V)])
            # plt.show()
            for i in range(len(c)):
                c[i] = c[i]*100
            return [V, c]
        if VNext < 0:
            print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            # plt.plot(V)
            # plt.plot(c)
            # plt.ylabel('V[m^3] and c[1]')
            # plt.axis([0, n, 0, max(V)])
            # plt.show()
            for i in range(len(c)):
                c[i] = c[i]*100
            return [V, c]
        V.append(VNext)
        cNext = (Qd1[n] * (cd1 - c[n]) + QD2 * (cd2 - c[n])) * Tp / V[n + 1]
        if n != 0:
            cNext += c[n]
        if cNext > 1:
            print('Container too concentrated! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            # plt.plot(V)
            # plt.plot(c)
            # plt.ylabel('V[m^3] and c[1]')
            # plt.axis([0, n, 0, max(V)])
            # plt.show()
            for i in range(len(c)):
                c[i] = c[i]*100
            return [V, c]
        if cNext < 0:
            print('Container at negative concentration! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            # plt.plot(V)
            # plt.plot(c)
            # plt.ylabel('V[m^3] and c[1]')
            # plt.axis([0, n, 0, max(V)])
            # plt.show()
            for i in range(len(c)):
                c[i] = c[i]*100
            return [V, c]
        c.append(cNext)
        if n == iterations - 1:
            toc = time.time()
            print("Run script: ", toc - tic)
            print('finisz')
            # plt.plot(V)
            # plt.plot(c)
            # plt.ylabel('V[m^3] and c[1]')
            # plt.axis([0, n, 0, max(V)])
            # plt.show()
            for i in range(len(c)):
                c[i] = c[i]*100
            return [V, c]

print('WaterContainer4.py loaded!')
# runWaterContainer4(10, 0, 0, 5, 5, 1, 0, 1, 0.1, 0.25, 3, 10, 0.2, 7, 1000000, 0.9, 10, 0)
