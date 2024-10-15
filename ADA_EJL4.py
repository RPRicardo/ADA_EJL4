import random
import math
import time

inicio = time.time()

# Función para calcular la distancia euclidiana entre dos puntos
def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Función para generar n puntos aleatorios en el rango dado
def generar_puntos(n, rango=(-10, 10)):
    puntos = [(random.uniform(rango[0], rango[1]), random.uniform(rango[0], rango[1])) for _ in range(n)]
    return puntos

# Función para encontrar el par de puntos más cercano
def puntos_mas_cercanos(puntos):
    min_distancia = float('inf')
    par_mas_cercano = None
    
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            distancia = distancia_euclidiana(puntos[i], puntos[j])
            if distancia < min_distancia:
                min_distancia = distancia
                par_mas_cercano = (puntos[i], puntos[j])
    
    return par_mas_cercano, min_distancia

# Generar 10 puntos aleatorios
n = 10
puntos = generar_puntos(n)

# Encontrar el par de puntos más cercano
par, distancia = puntos_mas_cercanos(puntos)

# Imprimir resultados
print(f"Puntos generados: {puntos}")
print(f"Par de puntos más cercano: {par}")
print(f"Distancia mínima: {distancia}")

fin = time.time()
print(f"Tiempo de ejecucion:{fin-inicio}")