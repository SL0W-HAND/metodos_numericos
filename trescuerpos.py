import pandas as pd
import numpy as np
import math 

# creando la clase planeta
class Planeta:

  def __init__ (self,posicion,velocidad,masa):
    self.posiciones=[[posicion[0]],[posicion[1]],[posicion[2]]]
    self.posicion_actual= posicion
    self.velocidad = velocidad
    self.momento = masa*velocidad
    self.masa = masa
    self.aceleracion = np.array([0,0,0])

def calculos(coleccion_planetas,constante_G,delta_t,tiempo_simulado):

    keys =["t"]
    
    valores = [[0]]
    for i in range(0,len(coleccion_planetas)):
        keys.append("X{0}".format(i))
        valores.append([coleccion_planetas[i].posicion_actual[0]])
        keys.append("Y{0}".format(i))
        valores.append([coleccion_planetas[i].posicion_actual[1]])
        keys.append("V_x{0}".format(i))
        valores.append([coleccion_planetas[i].velocidad[0]])
        keys.append("V_y{0}".format(i))
        valores.append([coleccion_planetas[i].velocidad[1]])
        keys.append("a_x{0}".format(i))
        valores.append([coleccion_planetas[i].aceleracion[0]])
        keys.append("a_y{0}".format(i))
        valores.append([coleccion_planetas[i].aceleracion[1]])

    datos = dict(zip(keys, valores))
    
    #simulacion de cada iteracion
    def draw(n):
        for i in coleccion_planetas:
            acum_acc = np.array([0,0,0])
            for j in coleccion_planetas:

                if i != j:
                    ##Calculo del vector que va de i a j
                    r_ij =  j.posicion_actual - i.posicion_actual 
                    r_ij_magnitud = math.sqrt(sum(k**2 for k in r_ij))
                    r_ij_unitario = r_ij/r_ij_magnitud

                    ##calculando aceleracion con un solo cuerpo
                    acc_neta_i = ((constante_G*j.masa)/(r_ij_magnitud**2))*r_ij_unitario 
                    
                    #subiendolo al acumulador para sumar la celeracion que produce cada cuerpo
                    acum_acc =acum_acc + acc_neta_i

                #asignando aceleracion calculada
                i.aceleracion = acum_acc

        #calcular la nueva posicion de cada planeta
        for i,index in zip(coleccion_planetas,range(0,len(coleccion_planetas))):
            
            i.velocidad = i.aceleracion*delta_t + i.velocidad
            i.posicion_actual = i.posicion_actual + i.velocidad*delta_t
            #print(i.velocidad)
            datos[str(f"X{index}")].append(i.posicion_actual[0])
            datos[str(f"Y{index}")].append(i.posicion_actual[1])
            datos[str(f"V_x{index}")].append(i.velocidad[0])
            datos[str(f"V_y{index}")].append(i.velocidad[0])
            datos[str(f"a_x{index}")].append(i.aceleracion[0])
            datos[str(f"a_y{index}")].append(i.aceleracion[0])
            for k in range(0,2):
                i.posiciones[k].append(i.posicion_actual[k])

        #datos_actualizados= [[f"{np.linalg.norm(i.velocidad):.2f} m/s",f"{np.linalg.norm(i.aceleracion):.2f}m/s^2",f"x:{i.posicion_actual[0]:.2f},y:{i.posicion_actual[1]:.2f}"] for i in coleccion_planetas]
        #tabla.table(cellText=datos_actualizados,rowLabels=etiquetas_fila,colLabels=['velocidad','aceleracion','posicion'],colLoc='center',loc='center')
        tiempo = n*delta_t
        datos["t"].append(tiempo)
    
    iteraciones = math.ceil(tiempo_simulado/delta_t)
    ##los intervalos afectan la duracion de la animacion bajos intervalos son una animacion mas rapida y altos intervalos son una animacion mas lenta
    for i in range(0,iteraciones):
        draw(i)
    return datos
  


sol = Planeta(np.array([0,0,0]),np.array([0,0,0]),1.989e30)
tierra = Planeta(np.array([1.5e11,0,0]),np.array([0,29800,0]),5.97e24)
luna = Planeta(np.array([(1.5e11+3.48e8),0,0]),np.array([0,29810,0]),7.34767e22)

cuerpos = [sol,tierra,luna]

G = 6.67e-11#constante de gravedad
dt = 3600#intervalo de tiempo en segundos
t = 3600*24*100 #segundos de simulacion
data = calculos(cuerpos,G,dt,t)

df = pd.DataFrame(data)

df.to_excel(r'valores problema de los tres cuerpos.xlsx', index = False)
print (df)

