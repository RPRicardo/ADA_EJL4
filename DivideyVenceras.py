import math
import time
inicio=time.time()

# Función para calcular la distancia euclidiana entre dos puntos
def distancia_euclidiana(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Función que encuentra la distancia mínima en un subarray de puntos
def distancia_minima_strip(strip, size, d):
    min_distancia = d  # Inicialmente, la distancia mínima es d

    # Ordenar el strip según las coordenadas y
    strip.sort(key=lambda punto: punto[1])

    # Comprobar el número de puntos a lo largo del strip que están a una distancia menor que d
    for i in range(size):
        j = i + 1
        while j < size and (strip[j][1] - strip[i][1]) < min_distancia:
            min_distancia = min(min_distancia, distancia_euclidiana(strip[i], strip[j]))
            j += 1

    return min_distancia

# Función recursiva que implementa el algoritmo divide y vencerás
def distancia_minima_recursiva(puntos, izq, der):
    # Si hay 2 o 3 puntos, usamos la distancia euclidiana directa
    if der - izq <= 3:
        return min(distancia_euclidiana(puntos[i], puntos[j]) for i in range(izq, der) for j in range(i+1, der))

    # Encontrar el punto medio
    medio = (izq + der) // 2
    punto_medio = puntos[medio]

    # Calcular la distancia mínima en las dos mitades recursivamente
    dl = distancia_minima_recursiva(puntos, izq, medio)
    dr = distancia_minima_recursiva(puntos, medio, der)

    # Distancia mínima de ambas mitades
    d = min(dl, dr)

    # Crear un array strip[] de todos los puntos que están dentro de la distancia d del punto medio
    strip = [punto for punto in puntos[izq:der] if abs(punto[0] - punto_medio[0]) < d]

    # Encontrar la distancia mínima en el strip
    return min(d, distancia_minima_strip(strip, len(strip), d))

# Función principal que encuentra la distancia mínima entre todos los puntos
def distancia_mas_cercana(puntos):
    # Ordenar los puntos según las coordenadas x
    puntos.sort(key=lambda punto: punto[0])
    return distancia_minima_recursiva(puntos, 0, len(puntos))

# Generar puntos aleatorios (puedes usar esta función o pasar tus propios puntos)
import random
def generar_puntos(n, rango=(-10, 10)):
    return [(random.uniform(rango[0], rango[1]), random.uniform(rango[0], rango[1])) for _ in range(n)]

# Ejemplo de uso
puntos = generar_puntos(1000)
print(f"Puntos generados: {puntos}")
distancia_minima = distancia_mas_cercana(puntos)
print(f"Distancia mínima: {distancia_minima}")

fin = time.time()
print(f"Tiempo de ejecucion:{fin-inicio}")