import numpy as np

#gain_or_cost dla gain =1 dla cost =-1
def calcC(var1, var2, q, p, gain_or_cost):
    if var1*gain_or_cost >= var2*gain_or_cost:
        return 1
    else:
        if var1 + q * gain_or_cost <= var2 <= var1:
            return 1
        if var1 + q * gain_or_cost <= var2 <= var1 + p * gain_or_cost:
            return np.interp([var2], [var1 + q * gain_or_cost, var1 + p * gain_or_cost], [1,0])
        else:
            return 0

#gain_or_cost dla gain =1 dla cost =-1
def calcV(var1, var2, p,v, gain_or_cost):
    if var1*gain_or_cost >= var2*gain_or_cost:
        return 0
    else:
        if var2 <= var1 + p * gain_or_cost:
            return 0
        if var2 >= var1 + v * gain_or_cost:
            return 1
        if var1 + p * gain_or_cost <= var2 <= var1 + v * gain_or_cost:
            return np.interp([var2], [var1 + p * gain_or_cost, var1 + v * gain_or_cost], [0,1])

