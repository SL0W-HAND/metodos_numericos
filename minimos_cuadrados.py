import numpy as np
from functools import reduce

def resolver_matriz(matriz):
    n = len(matriz)
    matriz = np.array(matriz)
    sol = np.zeros(n)
    #Gauss Jordan
    for i in range(n):     
        for j in range(n):
            if i != j:
                cociente = matriz[j][i]/matriz[i][i]

                for k in range(n+1):
                    matriz[j][k] = matriz[j][k] - cociente * matriz[i][k]

    for i in range(n):
        sol[i] = matriz[i][n]/matriz[i][i]

    return sol

def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n-1)

def minimos_cuadrados():
    n = int(input('Ingrese el numero de puntos: '))
    grado = int(input('Ingrese el grado del polinomio: '))
    puntos_x = []
    puntos_y = []
    for i in range(n):
        print("Punto", i+1)
        x_i = float(input("ingresa valor de x: "))
        puntos_x.append(x_i)
        y_i = float(input("ingresa valor de y: "))
        puntos_y.append(y_i)
        print(50*"--")
    
    matriz = []

    for i in range(grado+1):
        fila = []
        for j in range(grado+1):
            sum = reduce(lambda a,b: a+b,[potencia(x_i, i+j) for x_i in puntos_x])
            fila.append(sum)
        sum_y = reduce(lambda a,b: a+b,[y_i*(puntos_x[index]**i) for index, y_i in enumerate(puntos_y) ])
        fila.append(sum_y)
        matriz.append(fila)
    print(matriz)
    coeficientes_solucion = resolver_matriz(matriz)
    print(coeficientes_solucion)

    polinomio = [f"y = {coeficientes_solucion[0]:.3f} "] + [ f"+ {coeficientes_solucion[i+1]:.3f}x^{i+1} " for i in range(grado)]
    polinomio = "".join(polinomio)

    return {'polinomio': polinomio, 'coeficientes': coeficientes_solucion}

def main():
    ecuacion =  minimos_cuadrados()

    print (f"""

    El polinomio que pasa por los puntos es:
    {ecuacion['polinomio']}
    
    """)

if __name__ == "__main__":
    main()