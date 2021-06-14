"""
for normal PID with predefined values:
python script.py Area Beta Qd_start h_start Tp simLeng targeth hMax maxInput P_val I_val D_val
for ml version:
python script.py Area Beta Qd_start h_start Tp simLeng targeth hMax maxInput
to use ga version, swap line 87 and 89. mean and std parameters in norm(x) are the same for both
up to 6 places after the comma, so they're aproximated as the same value
"""

import math
import time

import pandas as pd
#import PIDController as PID_Controller
#import tensorflow as tf


def norm(x):
    # hardcoded values from data used to train currently used model
    stat = {'mean': [15.926381, 6.080413, 0.549178],
            'std': [3.693254, 2.660454, 0.274814]}
    # I don't get why I need to do it this way (dict -> dataframe -> func)
    # but it wouldn't work with (dataframe -> func) and I don't have time to fuck around
    stats = pd.DataFrame(stat)
    return (x - stats['mean']) / stats['std']


"""
# main
# Area in m^2
A = float(sys.argv[1])
# runoff coefficient, in m^(5/2)/s
Beta = float(sys.argv[2])
# Flow in in m^3/s, our input variable as Qd[0]=something non 0
Qd = [float(sys.argv[3])]
# Liquid height during steps, h(0) is the starting condition, in m
h = [float(sys.argv[4])]
# Sampling time/step time
Tp = float(sys.argv[5])
# in hours
SimulationLength = float(sys.argv[6])
# desired level
target_level = float(sys.argv[7])
# additional variables
e = [target_level - h[0]]
# for ml-regression based model:
model = tf.keras.models.load_model('saved models/version-ml-pid')
# for ga-based model:
# model = tf.keras.models.load_model('saved models/version-ga-pid')
# print(model.summary())
inpar = pd.DataFrame(norm([A, Beta, Tp]))
prd = model.predict(inpar.transpose())
# print(prd)
# just to be sure, no negative values
pid_val1 = prd.item(0) if prd.item(0) > 0 else 0
pid_val2 = prd.item(1) if prd.item(1) > 0 else 0
pid_val3 = prd.item(2) if prd.item(2) > 0 else 0
"""


def runWaterContainer3(A, Beta, Qd, H, hMax, target_level, maxInput, P1, I1, D1, Tp, SimulationLength):
    # 1: calculate number of iterations
    tic = time.time()
    iterations = int((3600 * SimulationLength) / Tp)
    h = [H]
    Qd = [Qd]
    e = [0]
    PID_controller = PIDController(P1, I1, D1, Tp)
    for n in range(iterations + 1):
        # skip step n = 0
        if n == 0:
            h.append(h[n])
            continue
        # calculate errors for the controller
        e.append(target_level - h[n])
        de = e[n] - e[n - 1]
        if n < 2:
            dde = de
        else:
            dde = e[n] - 2 * e[n - 1] + e[n - 2]
        # calculate the signal from PID, remember to sum it
        inpt = PID_controller.calc_delta_u(de, e[n], dde) + Qd[n - 1]
        if inpt <= 0:
            inpt = 0
        if inpt > maxInput:
            inpt = maxInput
        Qd.append(inpt)
        # calc next water lever
        hNext = 1 / A * (-1 * Beta * math.sqrt(h[n - 1]) + Qd[n - 1]) * Tp + h[n - 1]
        if hNext > hMax:
            print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            return h
        if hNext < 0:
            print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            return h
        h.append(hNext)
        if n == iterations:
            toc = time.time()
            print("Run script: ", toc - tic)
            print('finisz')
            return h


def runWaterContainer3_1(A, Beta, Qd, H, hMax, target_level, maxInput, version, Tp, SimulationLength):
    tic = time.time()
    iterations = int((3600 * SimulationLength) / Tp)
    h = [H]
    Qd = [Qd]
    e = [0]
    # ewentualnie mozna na sztywno zdefiniowac
    if version == 'ML-PID':
        # for ml-regression based model:
        model = tf.keras.models.load_model('saved models/version-ml-pid')
    else:
        # for ga-based model:
        model = tf.keras.models.load_model('saved models/version-ga-pid')
    inpar = pd.DataFrame(norm([A, Beta, Tp]))
    prd = model.predict(inpar.transpose())
    pid_val1 = prd.item(0) if prd.item(0) > 0 else 0
    pid_val2 = prd.item(1) if prd.item(1) > 0 else 0
    pid_val3 = prd.item(2) if prd.item(2) > 0 else 0
    PID_controller = PID_Controller.PIDController(pid_val1, pid_val2, pid_val3, Tp)
    for n in range(iterations + 1):
        # skip step n = 0
        if n == 0:
            h.append(h[n])
            continue
        # calculate errors for the controller
        e.append(target_level - h[n])
        de = e[n] - e[n - 1]
        if n < 2:
            dde = de
        else:
            dde = e[n] - 2 * e[n - 1] + e[n - 2]
        # calculate the signal from PID, remember to sum it
        inpt = PID_controller.calc_delta_u(de, e[n], dde) + Qd[n - 1]
        if inpt <= 0:
            inpt = 0
        if inpt > maxInput:
            inpt = maxInput
        Qd.append(inpt)
        # calc next water lever
        hNext = 1 / A * (-1 * Beta * math.sqrt(h[n - 1]) + Qd[n - 1]) * Tp + h[n - 1]
        if hNext > hMax:
            print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            return h
        if hNext < 0:
            print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            return h
        h.append(hNext)
        if n == iterations:
            toc = time.time()
            print("Run script: ", toc - tic)
            print('finisz')
            return h

print('WaterContainer3.py loaded!')
