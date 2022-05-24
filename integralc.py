import numpy as np

def funcion(x):
    z = np.complex_(1.736469-5j)
    return (1/(np.pi*np.sqrt(2)))*(np.sin(x)/(x*np.e**(z*(x**2))))

def f2_x(f,x,h):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)

def trapecio(f,a,b):
    h = b-a
    x = (a + b)/2
    return ((h/2)*(f(a)+f(b)))-((h**3)/12)*f2_x(f,x,0.1)
  
def integral(f,a,b,metodo):
    n = int((b-a)/0.01)+1
    h = (b-a)/n
    sum = 0
    for i in range(n):
        sum += metodo(f,a,(a+h))
        a += h
    return (1/(np.pi*np.sqrt(2)))* sum

print("definde un intervalo")
a = float(input("valor de a:  "))
b = float(input("valor de b:  "))

y = integral(funcion,a,b,trapecio)

print(f"parte real:{y.real}, parte compleja:{y.imag},")
