"""
Algoritmo Genético Generacional para el Problema del Agente Viajero (TSP).

Resumen del diseño:
- Codificación: cada cromosoma (individuo) es una permutación de índices
  de ciudades, por ejemplo [3, 0, 4, 1, 2]. Esto garantiza que cada
  ciudad aparezca exactamente una vez (ruta válida).
- Fitness: distancia total de la ruta (incluyendo el regreso a la
  ciudad de origen), calculada con la matriz de distancias Haversine.
  Como es un problema de MINIMIZACIÓN, un fitness más bajo es mejor.
- Selección: torneo (selección por torneo), robusto y simple de ajustar
  mediante el tamaño del torneo (presión selectiva).
- Cruce: Order Crossover (OX1), diseñado específicamente para
  problemas de permutación como el TSP, ya que preserva el orden
  relativo de las ciudades sin generar duplicados.
- Mutación: mutación por intercambio (swap mutation), intercambia dos
  ciudades de posición, manteniendo la validez de la ruta.
- Reemplazo: generacional. La nueva generación de hijos reemplaza por
  completo a la generación anterior. Se conserva únicamente el mejor
  individuo histórico mediante elitismo de tamaño 1, práctica estándar
  para no perder la mejor solución encontrada durante la búsqueda
  estocástica (sin esto, un algoritmo puramente generacional podría
  "olvidar" la mejor ruta hallada).
- Criterio de parada: Early Stopping. Si la mejor distancia no mejora
  tras un número determinado de generaciones consecutivas (paciencia),
  el algoritmo se detiene. También existe un tope máximo de
  generaciones como salvaguarda ante la no convergencia.
"""

import random


def distancia_ruta(ruta, matriz_distancias):
    """
    Calcula la distancia total de una ruta cerrada (ciclo): suma las
    distancias entre ciudades consecutivas y agrega el regreso desde
    la última ciudad hasta la primera (el agente viajero debe volver
    al punto de partida).
    """
    total = 0.0
    n = len(ruta)
    for i in range(n):
        ciudad_actual = ruta[i]
        ciudad_siguiente = ruta[(i + 1) % n]  # módulo para cerrar el ciclo
        total += matriz_distancias[ciudad_actual][ciudad_siguiente]
    return total


def crear_poblacion_inicial(tamano_poblacion, num_ciudades):
    """
    Genera la población inicial: 'tamano_poblacion' permutaciones
    aleatorias de las ciudades [0, 1, ..., num_ciudades-1].
    La aleatoriedad de la población inicial favorece la diversidad
    genética desde el arranque del algoritmo.
    """
    poblacion = []
    base = list(range(num_ciudades))
    for _ in range(tamano_poblacion):
        individuo = base.copy()
        random.shuffle(individuo)
        poblacion.append(individuo)
    return poblacion


def evaluar_poblacion(poblacion, matriz_distancias):
    """
    Calcula el fitness (distancia total) de cada individuo de la
    población. Retorna una lista de distancias alineada por índice
    con la población.
    """
    return [distancia_ruta(ind, matriz_distancias) for ind in poblacion]


def seleccion_torneo(poblacion, fitness, tamano_torneo=3):
    """
    Selección por torneo: se eligen 'tamano_torneo' individuos al azar
    de la población y se selecciona el que tenga menor distancia
    (mejor fitness, ya que minimizamos). Un torneo de mayor tamaño
    aumenta la presión selectiva (converge más rápido pero reduce
    diversidad); un torneo pequeño favorece la exploración.
    """
    participantes = random.sample(range(len(poblacion)), tamano_torneo)
    ganador = min(participantes, key=lambda idx: fitness[idx])
    return poblacion[ganador]


def cruce_ox1(padre1, padre2):
    """
    Order Crossover (OX1): operador de cruce especializado para
    permutaciones, evita generar rutas inválidas con ciudades
    duplicadas o faltantes.

    Procedimiento:
    1. Se eligen dos puntos de corte aleatorios [inicio, fin].
    2. El segmento del padre1 entre esos puntos se copia directamente
       al hijo, en las mismas posiciones.
    3. Las posiciones restantes del hijo se completan recorriendo el
       padre2 en orden (comenzando después del punto 'fin', de forma
       cíclica), insertando las ciudades que aún no estén en el hijo.

    Esto preserva el orden relativo de las ciudades del padre2 mientras
    conserva un bloque contiguo del padre1, y garantiza que el hijo sea
    una permutación válida (sin repeticiones).
    """
    n = len(padre1)
    inicio, fin = sorted(random.sample(range(n), 2))

    # Hijo inicializado con espacios vacíos (None)
    hijo = [None] * n

    # Paso 1: copiar el segmento del padre1 tal cual
    hijo[inicio:fin + 1] = padre1[inicio:fin + 1]
    genes_en_hijo = set(hijo[inicio:fin + 1])

    # Paso 2: completar con los genes del padre2 en su orden relativo,
    # comenzando justo después del punto de corte 'fin' (de forma
    # cíclica) y saltando las ciudades que ya están en el hijo.
    pos_hijo = (fin + 1) % n
    pos_padre2 = (fin + 1) % n

    while None in hijo:
        gen = padre2[pos_padre2]
        if gen not in genes_en_hijo:
            hijo[pos_hijo] = gen
            genes_en_hijo.add(gen)
            pos_hijo = (pos_hijo + 1) % n
        pos_padre2 = (pos_padre2 + 1) % n

    return hijo


def mutacion_swap(individuo, probabilidad_mutacion):
    """
    Mutación por intercambio (swap mutation): con una probabilidad dada,
    intercambia la posición de dos ciudades elegidas al azar dentro del
    cromosoma. Al ser un intercambio de posiciones (no un cambio de
    valor arbitrario), la ruta resultante sigue siendo una permutación
    válida, sin duplicar ni omitir ciudades.
    """
    individuo = individuo.copy()
    if random.random() < probabilidad_mutacion:
        i, j = random.sample(range(len(individuo)), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo


def ejecutar_algoritmo_genetico(
    matriz_distancias,
    tamano_poblacion=150,
    generaciones_maximas=1000,
    prob_cruce=0.9,
    prob_mutacion=0.02,
    tamano_torneo=3,
    paciencia_early_stopping=50,
    verbose=True,
):
    """
    Ejecuta el algoritmo genético generacional completo para resolver
    el TSP sobre la matriz de distancias dada.

    Parámetros:
        matriz_distancias: matriz N x N de distancias Haversine (km)
        tamano_poblacion: número de individuos por generación
        generaciones_maximas: tope máximo de generaciones (salvaguarda
            contra ejecución infinita si nunca se activa el early stopping)
        prob_cruce: probabilidad de aplicar cruce OX1 a una pareja
        prob_mutacion: probabilidad de mutación por individuo
        tamano_torneo: número de participantes en cada torneo de selección
        paciencia_early_stopping: número de generaciones consecutivas
            sin mejora tras las cuales se detiene el algoritmo
        verbose: si True, imprime el progreso cada cierto número de
            generaciones

    Retorna:
        mejor_ruta: lista de índices de ciudades (mejor ruta encontrada)
        mejor_distancia: distancia total de la mejor ruta (km)
        historial: lista con la mejor distancia registrada en cada
            generación (usada para graficar la convergencia)
    """
    num_ciudades = len(matriz_distancias)

    # --- Inicialización ---
    poblacion = crear_poblacion_inicial(tamano_poblacion, num_ciudades)
    fitness = evaluar_poblacion(poblacion, matriz_distancias)

    mejor_idx = min(range(len(poblacion)), key=lambda i: fitness[i])
    mejor_ruta = poblacion[mejor_idx].copy()
    mejor_distancia = fitness[mejor_idx]

    historial = [mejor_distancia]
    generaciones_sin_mejora = 0

    for generacion in range(1, generaciones_maximas + 1):
        nueva_poblacion = []

        # Elitismo: el mejor individuo histórico pasa directo a la
        # siguiente generación, para no perder la mejor solución en un
        # esquema puramente generacional (que reemplaza toda la
        # población cada iteración).
        nueva_poblacion.append(mejor_ruta.copy())

        # --- Reemplazo generacional: se generan hijos hasta completar
        # una nueva población del mismo tamaño, que reemplaza por
        # completo a la anterior ---
        while len(nueva_poblacion) < tamano_poblacion:
            padre1 = seleccion_torneo(poblacion, fitness, tamano_torneo)
            padre2 = seleccion_torneo(poblacion, fitness, tamano_torneo)

            if random.random() < prob_cruce:
                hijo = cruce_ox1(padre1, padre2)
            else:
                # Sin cruce, el hijo es una copia de uno de los padres
                hijo = padre1.copy()

            hijo = mutacion_swap(hijo, prob_mutacion)
            nueva_poblacion.append(hijo)

        poblacion = nueva_poblacion
        fitness = evaluar_poblacion(poblacion, matriz_distancias)

        idx_mejor_generacion = min(range(len(poblacion)), key=lambda i: fitness[i])
        distancia_mejor_generacion = fitness[idx_mejor_generacion]

        # --- Control de Early Stopping ---
        if distancia_mejor_generacion < mejor_distancia - 1e-9:
            mejor_distancia = distancia_mejor_generacion
            mejor_ruta = poblacion[idx_mejor_generacion].copy()
            generaciones_sin_mejora = 0
        else:
            generaciones_sin_mejora += 1

        historial.append(mejor_distancia)

        if verbose and generacion % 25 == 0:
            print(f"Generación {generacion:4d} | Mejor distancia: {mejor_distancia:.2f} km "
                  f"| Sin mejora: {generaciones_sin_mejora}/{paciencia_early_stopping}")

        if generaciones_sin_mejora >= paciencia_early_stopping:
            if verbose:
                print(f"\nEarly stopping activado en la generación {generacion}: "
                      f"sin mejora durante {paciencia_early_stopping} generaciones consecutivas.")
            break

    return mejor_ruta, mejor_distancia, historial
