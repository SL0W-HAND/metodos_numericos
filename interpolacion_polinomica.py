import numpy as np
      
def interpolacion_polinomica():
    a = []
    b = []
    num_puntos = int(input("Ingrese el numero de puntos: "))
    print(50*"--")
    
    for i in range(num_puntos):
        print("Punto", i+1)
        x_i = float(input("ingresa valor de x: "))
        a.append([x_i**x for x in range(num_puntos)])
        y_i = float(input("ingresa valor de y: "))
        b.append(y_i)
        print(50*"--")
    
    a = np.array(a)
    b = np.array(b)

    coeficientes_solucion = np.linalg.solve(a,b)
    
    polinomio = [f"y = {coeficientes_solucion[0]:.3f} "] + [ f"+ {coeficientes_solucion[i+1]:.3f}x^{i+1} " for i in range(num_puntos-1)]
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