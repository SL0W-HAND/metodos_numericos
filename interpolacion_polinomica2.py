import numpy as np

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

def interpolacion_polinomica():
    n = int(input('Ingrese el numero de puntos: '))
    a = []
    for i in range(n):
        print("Punto", i+1)
        x_i = float(input("ingresa valor de x: "))
        a.append([x_i**x for x in range(n)])
        y_i = float(input("ingresa valor de y: "))
        a[i].append(y_i)
        print(50*"--")
    coeficientes_solucion = resolver_matriz(a)
    
    polinomio = [f"y = {coeficientes_solucion[0]:.3f} "] + [ f"+ {coeficientes_solucion[i+1]:.3f}x^{i+1} " for i in range(n-1)]
    polinomio = "".join(polinomio)

    return {'polinomio': polinomio, 'coeficientes': coeficientes_solucion}
def main():
    ecuacion = interpolacion_polinomica()

    print (f"""

    El polinomio que pasa por los puntos es:
    {ecuacion['polinomio']}
    
    """)

if __name__ == "__main__":
    main()