import numpy as np


# gain_or_cost dla gain =1 dla cost =-1
def calcC(var1, var2, q, p, gain_or_cost):
    if gain_or_cost == 1:
        if var2 <= var1:
            return 1
        else:
            if var1 <= var2 <= var1 + q:
                return 1
            if var1 + q <= var2 <= var1 + p:
                return np.interp([var2], [var1 + q, var1 + p], [1, 0])[0]
            else:
                return 0
    else:
        if var2 >= var1:
            return 1
        else:
            if var1 >= var2 >= var1 - q:
                return 1
            if var1 - q >= var2 >= var1 - p:
                return np.interp([var2], [var1 - p, var1 - q], [0, 1])[0]
            else:
                return 0


# gain_or_cost dla gain =1 dla cost =-1
def calcV(var1, var2, p, v, gain_or_cost):
    if gain_or_cost == 1:
        if var2 <= var1 + p:
            return 0
        if var1 + p <= var2 <= var1 + v:
            return np.interp([var2], [var1 + p, var1 + v], [0, 1])[0]
        else:
            return 0
    else:
        if var2 >= var1 - p:
            return 0
        if var1 - p >= var2 >= var1 - v:
            return np.interp([var2], [var1 - v, var1 - p], [1, 0])[0]
        else:
            return 0


def calcAll(var1, var2, q, p, v, gain_or_cost):
    print('c= ', calcC(var1, var2, q, p, gain_or_cost))
    print('v= ', calcV(var1, var2, p, v, gain_or_cost))


def calcHowGood(var1, var2, q, p, gain_or_cost):
    diff = var1 - var2
    diff = diff*gain_or_cost
    if diff < 0:
        return 0
    else:
        if diff >= p:
            return 1
        if q <= diff <= p:
            return np.interp([diff], [q, p], [0, 1])[0]
        else:
            return 0


print(calcHowGood(7,8,0,2,1))