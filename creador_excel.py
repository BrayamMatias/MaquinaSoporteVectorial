import pandas as pd
import numpy as np

rango_brillo_truchas = [0.1,0.70]
rango_brillo_salmon = [0.1,0.69]

rango_longitud_truchas = [0.20,0.39]
rango_longitud_salmon = [0.40,0.91]

#Crear un dataframe con 200 patrones aleatorios truncado a 4 decimales
patrones = 200
brillo_truchas = np.round(np.random.uniform(rango_brillo_truchas[0], rango_brillo_truchas[1], 100), 4)
rango_longitud_truchas = np.round(np.random.uniform(rango_longitud_truchas[0], rango_longitud_truchas[1], 100), 4)
brillo_salmon = np.round(np.random.uniform(rango_brillo_salmon[0], rango_brillo_salmon[1], 100), 4)
longitud_salmon = np.round(np.random.uniform(rango_longitud_salmon[0], rango_longitud_salmon[1], 100), 4)

brillo = np.concatenate((brillo_truchas, brillo_salmon))
longitud = np.concatenate((rango_longitud_truchas, longitud_salmon))

#Asignar los 100 primeros valores a 0.33 (0.33 = plateados) para las truchas y el resto de valores a 0.99 (0.99 = rosas) para el color del salmón
color = np.zeros(patrones)
color[:100] = 0.33
color[100:] = 0.99

#Asignar los 100 primeros valores a 1 para las truchas y el resto de valores a 0 para el salmón
clase = np.zeros(patrones)
clase[:100] = 1

#Crear un dataframe con los datos y guardarlos en un excel
df = pd.DataFrame({'Brillo': brillo, 'Longitud': longitud, 'Color': color, 'Clase': clase})
df.to_excel('Datos.xlsx', index=False)
print('Archivo excel creado exitosamente')
