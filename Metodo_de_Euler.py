import decimal
import numpy as np
decimal.getcontext().prec = 7
def f_prima(x,y):
    return np.sqrt(1-y**2)

def euler(f,condicion_i_x,condicion_i_y,valor_y,h):
    
    iteraciones = valor_y/h

    x = condicion_i_x
    y = condicion_i_y

    for i in range(int(iteraciones+1)):
        print(f"{x:.2f} ------------{y:.7f}------------{f_prima(x,y):.7f}")
        y =  y
        x = x
        y = y + h*f(x,y)
        x = x +  h
    
    return x,y

euler(f_prima,0,0,1,0.1)