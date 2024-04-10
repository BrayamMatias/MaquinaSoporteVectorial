import pandas as pd
import numpy as np

# Leer el archivo excel
data_c = pd.read_excel('MSV\Datos.xlsx')
print("Datos cargados correctamente.")

# Inicializacion de variables
b = 0
w = [0.37, 0.58]
# Considera un error de 0.005
e = 0.005
n = 200

data = data_c.drop('Clase', axis=1)
resultados_iteraciones = []

# Iniciar un ciclo de 10 iteraciones
for i in range(10):
    print(f"Iniciando iteración {i+1}")
    # Inicializar lista Ns como una lista de tamaño n llena de ceros
    Ns = [0] * n

    # Calcular φ(x) para la clasificación de los 200 patrones
    fi = []
    for y in range(n):
        if y <= 99:  # truchas
            fi.append((w[0]*data['Brillo'][y] + w[0]*data['Longitud'][y] + w[0]*data['Color'][y]) +
                      (w[1]*data['Brillo'][y] + w[1]*data['Longitud'][y] + w[1]*data['Color'][y]) - b - 1)
        else:  # salmones
            fi.append((w[0]*data['Brillo'][y] + w[0]*data['Longitud'][y] + w[0]*data['Color'][y]) +
                      (w[1]*data['Brillo'][y] + w[1]*data['Longitud'][y] + w[1]*data['Color'][y]) + b + 1)

    print("Cálculo de φ(x) completado.")

    # Calcular Ns
    for y in range(n):
        if y <= 99:
            Ns[y] = 1 if fi[y] < 1 else 0
        if y >= 100:
            Ns[y] = 1 if fi[y] >= 1 else 0

    print("Cálculo de Ns completado.")

    # Calcular tamaño de Ns diferente de 0
    tam_Ns = np.count_nonzero(Ns)
    print(f"Tamaño de Ns diferente de 0: {tam_Ns}")

    # Mientras haya números de soporte, seguir trabajando con ellos
    while tam_Ns > 1:
        # Calcular epsilon
        epsilon = round((e * tam_Ns) / n, 4)

        # Actualizar b
        b = round(b - epsilon, 4)

        # Recalcular φ(x) para la clasificación de los 200 patrones
        fi = []
        for y in range(n):
            if y <= 99:  # truchas
                fi.append((w[0]*data['Brillo'][y] + w[0]*data['Longitud'][y] + w[0]*data['Color'][y]) +
                          (w[1]*data['Brillo'][y] + w[1]*data['Longitud'][y] + w[1]*data['Color'][y]) - b - 1)
            else:  # salmones
                fi.append((w[0]*data['Brillo'][y] + w[0]*data['Longitud'][y] + w[0]*data['Color'][y]) +
                          (w[1]*data['Brillo'][y] + w[1]*data['Longitud'][y] + w[1]*data['Color'][y]) + b + 1)

        # Recalcular Ns y tam_Ns
        for y in range(n):
            if y <= 99:
                Ns[y] = 1 if fi[y] < 1 else 0
            if y >= 100:
                Ns[y] = 1 if fi[y] >= 1 else 0
        tam_Ns = np.count_nonzero(Ns)

        # Almacenar los resultados de la iteración actual
        resultados_iteraciones.append(
            {'tam_Ns': tam_Ns, 'epsilon': epsilon, 'b': b})

        print(f"Resultados de la iteración {i+1}: tam_Ns = {tam_Ns}, epsilon = {epsilon}, b = {b}")

    print(f"Fin de la iteración {i+1}.")

# Convertir la lista de resultados en un DataFrame
df_resultados = pd.DataFrame(resultados_iteraciones)

print("Resultados finales:")
print(df_resultados)