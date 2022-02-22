import numpy as np

def f_x(x):
    val = 2-(np.e**np.cos(x))
    return val

def f1(x,h):
    return (f_x(x+h)-f_x(x-h))/(2*h)

def f2(x,h):
    return (f_x(x+h)-2*f_x(x)+f_x(x-h))/(h**2)

punto = float(input("En que punto quieres evaluar   "))

print(f"""
la primera derivada es {f1(punto,0.000001):.5f}
la segunda derivada es {f2(punto,0.000001):.5f}
""")