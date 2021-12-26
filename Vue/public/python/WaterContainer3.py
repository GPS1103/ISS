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
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt


def norm(x):
    # hardcoded values from data used to train currently used model
    stat = {'mean': [15.926381, 6.080413, 0.549178],
            'std': [3.693254, 2.660454, 0.274814]}
    stats = pd.DataFrame(stat)
    return (x - stats['mean']) / stats['std']


def ejaj_regression(x):
    layer1_weights = np.array([[-0.3652133, 0.21523532, -0.18504205],
                               [-0.04038384, -0.79980546, 0.33047605],
                               [-0.06612226, 0.30116287, -0.68323517]])
    layer2_weights = np.array([[0.50059885, -0.7809136, 0.6293891, -0.6783556, 0.8568411, -0.31585088, -0.44407186,
                                -0.37129068, -0.01422959, 0.52406424, -0.15060587, -0.05142915],
                               [-0.49986053, 0.62625426, -0.03423691, 0.3039353, -0.1370309, 0.39112607, 0.2569834,
                                0.48216978, 0.09662178, 0.10427687, -0.12222373, 0.38825998],
                               [-0.6488712, 0.3516692, 0.27214754, 0.68684685, 0.20752552, 0.37605286, 0.12521814,
                                0.8151313, -0.03946819, -0.26146895, 0.02113781, 0.57765824]])
    layer3_weights = np.array([[-1.0649244, -0.4311106, 0.43716633],
                               [0.99008816, -0.20103736, 0.18401256],
                               [-0.8408843, -0.5221815, -0.19181532],
                               [0.82978517, -0.5841328, 0.3049313],
                               [-1.0228319, -0.08258318, 0.24165727],
                               [0.7129268, 0.39536184, 0.05969885],
                               [0.6144482, 0.19874875, 0.269269],
                               [1.013823, -0.17119884, -0.18200162],
                               [-0.6478733, -0.4983679, -0.35537305],
                               [-0.55266607, -0.02704109, -0.17890051],
                               [-0.45730424, -0.04757564, 0.20883375],
                               [0.7781466, -0.51592374, 0.19370884]])
    bias1_weights = np.array([-0.67134786, 0.781727, 0.63493973])
    bias2_weights = np.array([-0.6360266, 0.58692867, -0.6305925, 0.56498355, -0.6043997,
                              0.72020423, 0.72026134, 0.5927433, -0.5990368, -0.6210684,
                              -0.69730043, 0.5852299])
    bias3_weights = np.array([0.59310997, 0.87822074, 0.02386161])

    lr1 = np.matmul(x, layer1_weights) + bias1_weights
    lr2 = np.matmul(lr1, layer2_weights) + bias2_weights
    lr3 = np.matmul(lr2, layer3_weights) + bias3_weights
    return lr3


def ejaj_genetic(x):
    layer1_weights = np.array([[0.03148309, 0.96470755, 0.31385922],
                               [0.26323122, 0.47487006, -0.24926558],
                               [-0.16710225, -0.2671372, -0.4856029]])
    layer2_weights = np.array([[0.45904192, -0.47147676, -0.5665473, 0.54480773, -0.27064613, 0.41692072, -0.5315104,
                                -0.47442725, -0.38240486, -0.77487606, -1.0760137, -0.21705118],
                               [-0.38431764, 0.49730435, -0.5679229, -0.1752016, -0.47159067, -0.1156661, 0.6925907,
                                0.6180956, 0.5753126, 0.13503708, -0.02828509, -0.20610504],
                               [-0.430212, 0.2972506, 0.6453489, -0.33420444, 0.07009264, -0.6730274, 0.8562382,
                                0.123173, 0.6320153, 0.40915293, -0.6546112, -0.59275335]])
    layer3_weights = np.array([[0.45048776, 0.17205307, 0.02798988],
                               [-0.79187137, -0.33189797, -0.06331079],
                               [1.0217173, -0.5932268, 0.03887472],
                               [-0.3324613, -0.4992611, -0.48627472],
                               [-0.3672185, 0.49752894, -0.50380665],
                               [-1.265403, 0.20936805, 0.3980982],
                               [1.7889122, 0.3309147, -0.09893087],
                               [0.39163172, -0.1339374, -0.7404828],
                               [0.7482656, 0.0909865, 0.7674827],
                               [0.4588971, 0.06416436, -0.3261943],
                               [0.77597743, 0.28720677, 0.67396814],
                               [0.48735735, -0.01402764, -0.5233335]])
    bias1_weights = np.array([-1.0257411, 0.13517432, 0.8068179])
    bias2_weights = np.array([0.6058146, -1.0962118, 0.47091955, -0.280491, -0.01567817, -1.1206177,
                              1.135427, 0.02486483, 0.26483908, 0.11905928, 1.043513, 0.53086066])
    bias3_weights = np.array([1.2450136, 0.29801425, 0.24449526])

    lr1 = np.matmul(x, layer1_weights) + bias1_weights
    lr2 = np.matmul(lr1, layer2_weights) + bias2_weights
    lr3 = np.matmul(lr2, layer3_weights) + bias3_weights
    return lr3


def norm(x):
    # hardcoded values from data used to train currently used model
    stat = {'mean': [15.926381, 6.080413, 0.549178],
            'std': [3.693254, 2.660454, 0.274814]}
    # I don't get why I need to do it this way (dict -> dataframe -> func)
    # but it wouldn't work with (dataframe -> func) and I don't have time to fuck around
    stats = pd.DataFrame(stat)
    return (x - stats['mean']) / stats['std']


def ejaj(x):
    layer1_weights = np.array([[0.03148309, 0.96470755, 0.31385922],
                               [0.26323122, 0.47487006, -0.24926558],
                               [-0.16710225, -0.2671372, -0.4856029]])
    layer2_weights = np.array([[0.45904192, -0.47147676, -0.5665473, 0.54480773, -0.27064613, 0.41692072, -0.5315104,
                                -0.47442725, -0.38240486, -0.77487606, -1.0760137, -0.21705118],
                               [-0.38431764, 0.49730435, -0.5679229, -0.1752016, -0.47159067, -0.1156661, 0.6925907,
                                0.6180956, 0.5753126, 0.13503708, -0.02828509, -0.20610504],
                               [-0.430212, 0.2972506, 0.6453489, -0.33420444, 0.07009264, -0.6730274, 0.8562382,
                                0.123173, 0.6320153, 0.40915293, -0.6546112, -0.59275335]])
    layer3_weights = np.array([[0.45048776, 0.17205307, 0.02798988],
                               [-0.79187137, -0.33189797, -0.06331079],
                               [1.0217173, -0.5932268, 0.03887472],
                               [-0.3324613, -0.4992611, -0.48627472],
                               [-0.3672185, 0.49752894, -0.50380665],
                               [-1.265403, 0.20936805, 0.3980982],
                               [1.7889122, 0.3309147, -0.09893087],
                               [0.39163172, -0.1339374, -0.7404828],
                               [0.7482656, 0.0909865, 0.7674827],
                               [0.4588971, 0.06416436, -0.3261943],
                               [0.77597743, 0.28720677, 0.67396814],
                               [0.48735735, -0.01402764, -0.5233335]])
    bias1_weights = np.array([-1.0257411, 0.13517432, 0.8068179])
    bias2_weights = np.array(
        [0.6058146, -1.0962118, 0.47091955, -0.280491, -0.01567817, -1.1206177, 1.135427, 0.02486483, 0.26483908,
         0.11905928, 1.043513, 0.53086066])
    bias3_weights = np.array([1.2450136, 0.29801425, 0.24449526])
    lr1 = np.matmul(x, layer1_weights) + bias1_weights
    lr2 = np.matmul(lr1, layer2_weights) + bias2_weights
    lr3 = np.matmul(lr2, layer3_weights) + bias3_weights
    return lr3


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


def runWaterContainer3(A, Beta, H, hMax, target_level, maxInput, P1, I1, D1, Tp, SimulationLength):
    # 1: calculate number of iterations
    tic = time.time()
    iterations = int((3600 * SimulationLength) / Tp)
    h = [H]
    Qd = []
    e = []
    PID_controller = PIDController(P1, I1, D1, Tp)
    for n in range(iterations + 1):
        # calculate errors for the controller
        e.append(target_level - h[n])
        if n == 0:
            de = dde = 0
        else:
            de = e[n] - e[n - 1]
        if n < 1:
            dde = 0
        else:
            dde = e[n] - 2 * e[n - 1] + e[n - 2]
        # calculate the signal from PID, remember to sum it
        inpt = PID_controller.calc_delta_u(de, e[n], dde)
        if n != 0:
            inpt += Qd[n - 1]
        if inpt <= 0:
            inpt = 0
        if inpt > maxInput:
            inpt = maxInput
        Qd.append(inpt)
        # calc next water lever
        # it has to have Qd[n] so we can keep calculating with a softer start
        hNext = 1 / A * (-1 * Beta * math.sqrt(h[n]) + Qd[n]) * Tp + h[n]
        if hNext > hMax:
            print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            """
            plt.plot(Qd)
            plt.plot(h)
            plt.ylabel('Qd[m^3/s] and h[m]')
            plt.axis([0, iterations, 0, max(h)])
            plt.show()
            """
            return h
        if hNext < 0:
            print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            """
            plt.plot(Qd)
            plt.plot(h)
            plt.ylabel('Qd[m^3/s] and h[m]')
            plt.axis([0, iterations, 0, max(h)])
            plt.show()
            """
            return h
        h.append(hNext)
        if n == iterations:
            toc = time.time()
            print("Run script: ", toc - tic)
            print('finisz')
            """
            plt.plot(Qd)
            plt.plot(h)
            plt.ylabel('Qd[m^3/s] and h[m]')
            plt.axis([0, iterations, 0, max(h)])
            plt.show()
            """
            return h


# runWaterContainer3(1, 0.5, 2.9, 5, 25, 0.25, 0.05, 12, 5, 2, 20, 0.25)


def runWaterContainer3_1(A, Beta, H, hMax, target_level, maxInput, version, Tp, SimulationLength):
    tic = time.time()
    iterations = int((3600 * SimulationLength) / Tp)
    h = [H]
    Qd = []
    e = []
    inpar = norm([A, Beta, Tp]).to_numpy()
    # ewentualnie mozna na sztywno zdefiniowac
    if version == 0:
        prd = ejaj_regression(inpar)
    else:
        prd = ejaj_genetic(inpar)

    pid_val1 = prd[0] if prd[0] > 0 else 0
    pid_val2 = prd[1] if prd[1] > 1 else 1
    pid_val3 = prd[2] if prd[2] > 0 else 0
    #temporary measure
    pid_val1 = pid_val1/(Beta*(Beta*-290+153))
    pid_val2 = pid_val2*10
    pid_val3 = pid_val3/(Beta*500)

    PID_controller = PIDController(pid_val1, pid_val2, pid_val3, Tp)

    for n in range(iterations + 1):
        # calculate errors for the controller
        e.append(target_level - h[n])
        if n == 0:
            de = 0
        else:
            de = e[n] - e[n - 1]
        if n < 1:
            dde = 0
        else:
            dde = e[n] - 2 * e[n - 1] + e[n - 2]
        # calculate the signal from PID, remember to sum it
        inpt = PID_controller.calc_delta_u(de, e[n], dde)
        if n != 0:
            inpt += Qd[n - 1]
        if inpt <= 0:
            inpt = 0
        if inpt > maxInput:
            inpt = maxInput
        Qd.append(inpt)
        # calc next water lever
        # it has to have Qd[n] so we can keep calculating with a softer start
        hNext = 1 / A * (-1 * Beta * math.sqrt(h[n]) + Qd[n]) * Tp + h[n]
        if hNext > hMax:
            print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            """
            plt.plot(Qd)
            plt.plot(h)
            plt.ylabel('Qd[m^3/s] and h[m]')
            plt.axis([0, iterations, 0, max(h)])
            plt.show()
            """
            return h
        if hNext < 0:
            print('Container empty! Happened at iteration = ', n, ' equal to time =', n * Tp, ' s.')
            """
            plt.plot(Qd)
            plt.plot(h)
            plt.ylabel('Qd[m^3/s] and h[m]')
            plt.axis([0, iterations, 0, max(h)])
            plt.show()
            """
            return h
        h.append(hNext)
        if n == (iterations - 1):
            toc = time.time()
            print("Run script: ", toc - tic)
            print('finisz')
            """
            plt.plot(Qd)
            plt.plot(h)
            plt.ylabel('Qd[m^3/s] and h[m]')
            plt.axis([0, iterations, 0, max(h)])
            plt.show()
            """
            return h


print('WaterContainer3.py loaded!')
# runWaterContainer3(10, 0.5, 2.9, 5, 25, 0.25, 0.05, 12, 5, 0)