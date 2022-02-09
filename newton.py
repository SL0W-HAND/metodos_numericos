import numpy as np

def f_x(x):
    result = 2 - (np.e**(np.cos(x)))
    return result

def derivada(p,incremento_h):
    derivada = (f_x(p + incremento_h)-f_x(p))/incremento_h
    return derivada

def newton(x_i,error):
    x_n = x_i
    dx = -f_x(x_i)/derivada(x_i,0.00001)
    while(np.absolute(dx)>error):
        print(x_n,"----",f_x(x_n),"----",derivada(x_n,0.00001),"----",dx)
        x_n = x_n + dx
        dx = -f_x(x_n)/derivada(x_n,0.00001)
    
    print(x_n,"----",f_x(x_n),"----",derivada(x_n,0.00001),"----",dx)
    return x_n

print(newton(4.5,0.0001))

    