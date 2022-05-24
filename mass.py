import pandas as pd
import numpy as np
import math 

t =0  
masa_agua = 5
m_b=0.26

constante_k = 127
z_0 = -((masa_agua+m_b)*9.81)/(constante_k)

def masa_w(t):
    h_0 = 0.1
    f = 0.01 
    res = (masa_agua)*((1-f*t*(math.sqrt(9.81/(2*h_0))))**2)
    return res
tiempo_simulado = 20
delta_t = 0.05

#condiciones iniciales
z = z_0
v = 0 
datos = {
    "t":[0],
    "z":[z],
    "m":[masa_w(0)],
    "v":[v],
    "a":[0],
    "z0-z":[z_0-z]
}

for i in np.arange(0,tiempo_simulado,delta_t):
    
   
    z_actual = z
    z = z_actual+v*delta_t
    v_i = v
    v = v -delta_t*((constante_k/(masa_w(t)+m_b))*z_actual+9.81)
    acc_z = (v-v_i)/delta_t 
    t = t + delta_t 
    datos["t"].append(t)
    datos["z"].append(z)
    datos["m"].append(masa_w(t))
    datos["v"].append(v)
    datos["a"].append(acc_z)
    datos["z0-z"].append(z-z_0)

df = pd.DataFrame({'t(s)':datos["t"],
                    'z(m)':datos["z"],
                    'm(kg)':datos["m"],
                    'v(m/s)':datos["v"],
                    'a(m/s2)':datos["a"],
                    'z-z0(m)':datos["z0-z"]
                    })
print(df)

df.to_excel(r'resultados.xlsx', index = False)