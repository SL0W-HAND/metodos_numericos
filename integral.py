import numpy as np

def funcion1(x):
    return 2- (np.e**np.cos(x))

def funcion2(x):
    return (x**np.log(x))-2*x

def f2_x(f,x,h):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)

def trapecio(f,a,b):
    h = b-a
    x = (a + b)/2
    return ((h/2)*(f(a)+f(b)))-((h**3)/12)*f2_x(f,x,0.000001)
  
def integral(f,a,b,metodo):
    n = int((b-a)/0.001)+1
    h = (b-a)/n
    sum = 0
    for i in range(n):
        sum += metodo(f,a,(a+h))
        a += h
    return sum

print("definde un intervalo")
a = float(input("valor de a:  "))
b = float(input("valor de b:  "))

print(f"El area es aproximadamente {integral(funcion2,a,b,trapecio):.6f}")
