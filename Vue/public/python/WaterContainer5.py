# A = Area in m^2
# 
# Beta = runoff coefficient, in m^(5/2)/s
# 
# Qd = Maximum and initial flow in m^3/s
# 
# h = Liquid height during steps, h(0) is the starting condition, in m
# 
# Tp= Sampling time/step time
#  
# SimulationLength #in hours

# #constraints
# hMax = 20               #maximum length of container in meters

import math
import time


def setQd(e,Beta, Qdmax, A, hNext ):
    if(e < 0):
        return 0
    if(e == 0):
        return (Beta*math.sqrt(hNext))
    if(e > 0):
        if((e+((Beta*math.sqrt(hNext))/A))>=(Qdmax/A)): 
            return Qdmax
        if((e+((Beta*math.sqrt(hNext))/A))<(Qdmax/A)):
            return ((e*A)+(Beta*math.sqrt(hNext)))
        
def runWaterContainer5(A, Beta, Qdmax, H, hMax, hZadane, Tp, SimulationLength):
    print(A, Beta, Qdmax, H, Tp, SimulationLength, hMax, hZadane)
    Qd=Qdmax
    iterations = int((3600 * SimulationLength) / Tp)
    h=[H]
    ce=0
    se=0
    print(iterations)
    tic = time.time()
    eLast=0
    for n in range(iterations + 1):
        #skip step n = 0
        if (n == 0):
            continue
        hNext = 1/A*(-1*Beta*math.sqrt(h[n-1])+Qd)*Tp+h[n-1]
        if hNext > hMax:
            print('Container overflowed! Happened at iteration = ', n, ' equal to time =', n*Tp, ' s.')
            return h
        
        h.append(hNext)

        if n == iterations:
            toc = time.time()
            print("Run script: ", toc - tic)
            print('finisz')    
            return h
        e=hZadane-hNext
        Qd=setQd(e, Beta ,Qdmax, A, hNext)
        
        
print('WaterContainer5.py loaded!')
