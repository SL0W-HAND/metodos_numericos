import numpy as np

def funcion1(x):
    return 2 - np.e**np.cos(x)

def funcion2(x):
    return (x**np.log(x))-2*x

def f2_x(f,x,h):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)

def f4(f,x,h):
    return ((f(x+2*h)-4*f(x+h)+6*f(x)-4*f(x-h)+f(x-2*h))/(h**4))

def trapecio(f,a,b):
    h = b-a
    x = (a + b)/2
    return ((h/2)*(f(a)+f(b)))-((h**3)/12)*f2_x(f,x,0.1)

def simpson(f,a,b):
    h = (b-a)/2
    x = (a+b)/2
    return ((h/3)*(f(a)+4*f(x)+f(b)))#-((h**5)/90)*f4(f,x,0.001)
  
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


print(f"El area es aproximadamente {integral(funcion1,a,b,simpson):.6f}")