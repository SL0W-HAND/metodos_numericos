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


name_dict = {
            'Name': ['a','b','c','d'],
            'Score': [90,80,95,20]
          }

df = pd.DataFrame(name_dict)

df.to_excel(r'File Name.xlsx', index = False)
print (df)

