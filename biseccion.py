
import math
import numpy as np
def f_x(x):
    res = 2-(np.e**x)
    return res

def abs(number):
    if (number < 0):
        return number*-1
    else:
        return number

def biseccion(a,b,tolerancia):

    m = (a+b)/2 

    while(abs(b-a)>tolerancia):
        if(f_x(a)*f_x(m)>0):
            a=m
        else:
            b=m
        m=a+b/2
    return m

print(biseccion(6,7.5,0.1))