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

import time

def runWaterContainer4_1(v, C, QD1, QD2, QO, cd1, cd2, Tp, SimulationLength, target_c, P1, I1, D1, maxInput, vMax):
    tic = time.time()
    iterations = int(3600 * SimulationLength / Tp)
    V = [v]
    c = [C]
    Qd1 = [QD1]
    Qd2 = [QD2]
    Qo = [QO]
    e1 = [target_c - c[0]]
    de1 = [0]
    dde1 = [0]
    u1 = [0]
    e2 = [0]
    de2 = [0]
    dde2 = [0]
    u2 = [0]
    u2_unconstrained = [0]
    PID_conc = PIDController(P1, I1, D1, Tp)
    PID_flow = PIDController(P1, I1, D1, Tp)
    for n in range(iterations + 1):
        # skip step n = 0
        if n == 0:
            continue
        e1.append(target_c - c[n - 1])
        de1.append(e1[n - 1] - e1[n - 2])

        if n < 2:
            dde1.append(de1[n])
        else:
            dde1.append(e1[n - 1] - 2 * e1[n - 2] + e1[n - 3])

        tmp_u1 = PID_conc.calc_delta_u(de1[n], e1[n], dde1[n]) + u1[n - 1]
        u1.append(tmp_u1)

        # u1 is x2, x2 - y2 = e2, y2 is V[0]
        e2.append(u1[n] - u1[n - 1])
        de2.append(e2[n] - e2[n - 1])

        if n < 2:
            dde2.append(de2[n])
        else:
            dde2.append(e2[n] - 2 * e2[n - 1] + e2[n - 2])

        tmp_u2 = PID_flow.calc_delta_u(de2[n], e2[n], dde2[n]) + u2[n - 1]
        if tmp_u2 < 0:
            tmp_u2 = 0
        u2.append(tmp_u2)

        u2_unconstrained.append(u2[n])
        if u2[n] > maxInput:
            u2[n] = maxInput
        if u2[n] <= 0:
            u2[n] = 0
        Qd1.append(u2[n])
        Qo.append(Qo[0])

        VNext = (Qd1[n] + Qd2[0] - Qo[n]) * Tp + V[n - 1]
        if VNext > vMax:
            print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            return [V, c]
        if VNext < 0:
            print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            return [V, c]

        cNext = (Qd1[n - 1] * (cd1 - c[n - 1]) + Qd2[0] * (cd2 - c[n - 1])) * Tp / V[n - 1] + c[n - 1]
        if cNext > 1:
            print('Container too concentrated! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            return [V, c]
        if cNext < 0:
            print('Container has negative concentration! Happened at iteration = ', n, ' equal to time =', n * Tp,
                  ' s.')
            return [V, c]

        V.append(VNext)
        c.append(cNext)

        if n == iterations:
            toc = time.time()
            print("Run script: ", toc - tic)
            print('finisz')
            return [V, c]


def runWaterContainer4(v, C, QD1, QD2, QO, cd1, cd2, target_c, P1, I1, D1, maxInput, vMax, P2, I2, D2, Tp, SimulationLength):
    tic = time.time()
    iterations = int(3600 * SimulationLength / Tp)
    C = C/100
    V = [v]
    c = [C]
    Qd1 = [QD1]
    Qd2 = [QD2]
    Qo = [QO]
    e1 = [target_c - c[0]]
    de1 = [0]
    dde1 = [0]
    u1 = [0]
    e2 = [0]
    de2 = [0]
    dde2 = [0]
    u2 = [0]
    e3 = [0]
    de3 = [0]
    dde3 = [0]
    u3 = [0]
    PID_conc = PIDController(P1, I1, D1, Tp)
    PID_flow = PIDController(P1, I1, D1, Tp)
    PID_out = PIDController(P2, I2, D2, Tp)
    for n in range(iterations + 1):
        # skip step n = 0
        if n == 0:
            continue
        e1.append(target_c - c[n - 1])
        de1.append(e1[n - 1] - e1[n - 2])

        if n < 2:
            dde1.append(de1[n])
        else:
            dde1.append(e1[n - 1] - 2 * e1[n - 2] + e1[n - 3])

        tmp_u1 = PID_conc.calc_delta_u(de1[n], e1[n], dde1[n]) + u1[n - 1]
        u1.append(tmp_u1)

        # u1 is x2, x2 - y2 = e2, y2 is V[0]
        e2.append(u1[n] - u1[n - 1])
        de2.append(e2[n] - e2[n - 1])

        if n < 2:
            dde2.append(de2[n])
        else:
            dde2.append(e2[n] - 2 * e2[n - 1] + e2[n - 2])

        tmp_u2 = PID_flow.calc_delta_u(de2[n], e2[n], dde2[n]) + u2[n - 1]
        if tmp_u2 < 0:
            tmp_u2 = 0
        u2.append(tmp_u2)
        if u2[n] > maxInput:
            u2[n] = maxInput
        if u2[n] <= 0:
            u2[n] = 0
        Qd1.append(u2[n])

        e3.append(V[n - 1] - V[0])
        de3.append(e3[n] - e3[n - 1])
        if n < 2:
            dde3.append(de3[n])
        else:
            dde3.append(e3[n] - 2 * e3[n - 1] + e3[n - 2])

        u3_tmp = PID_out.calc_delta_u(de3[n], e3[n], dde3[n]) + Qo[n - 1]
        if u3_tmp < 0:
            u3_tmp = 0
        u3.append(u3_tmp)
        Qo.append(u3_tmp)

        VNext = (Qd1[n] + Qd2[0] - Qo[n]) * Tp + V[n - 1]
        if VNext > vMax:
            print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            return [V, c]
        if VNext < 0:
            print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            return [V, c]
        cNext = (Qd1[n - 1] * (cd1 - c[n - 1]) + Qd2[0] * (cd2 - c[n - 1])) * Tp / V[n - 1] + c[n - 1]
        if cNext > 1:
            print('Container too concentrated! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            return [V, c]
        V.append(VNext)
        c.append(cNext)
        if n == iterations:
            toc = time.time()
            print("Run script: ", toc - tic)
            print('finisz')
            return [V, c]

# runWaterContainer4(10, 0.1, 1, 1, 1.001, 0.5, 0.1, 1, 0.5, 0.25, 3, 30, 0.1, 5, 1000)
# runWaterContainer4(10, 0.1, 1, 1, 1.001, 0.5, 0.1, 1, 0.5, 0.25, 3, 30, 0.1, 5, 1000, 1, 10, 0.1)
print('WaterContainer4.py loaded!')