"""
Cálculo de distancias geográficas usando la fórmula de Haversine.

La fórmula de Haversine calcula la distancia de "gran círculo" entre dos
puntos sobre la superficie de una esfera a partir de su latitud y
longitud. Es más precisa que la distancia euclidiana para coordenadas
geográficas, ya que considera la curvatura de la Tierra.

Fórmula:
    a = sen²(Δφ/2) + cos(φ1) * cos(φ2) * sen²(Δλ/2)
    c = 2 * atan2(√a, √(1−a))
    d = R * c

Donde:
    φ1, φ2 = latitudes de los dos puntos (en radianes)
    Δφ     = diferencia de latitudes
    Δλ     = diferencia de longitudes
    R      = radio medio de la Tierra (6371 km)
"""

import math

# Radio medio de la Tierra en kilómetros
RADIO_TIERRA_KM = 6371.0


def haversine(coord1, coord2):
    """
    Calcula la distancia en kilómetros entre dos coordenadas geográficas
    (lat, lon) usando la fórmula de Haversine.

    Parámetros:
        coord1: tupla (latitud, longitud) en grados decimales
        coord2: tupla (latitud, longitud) en grados decimales

    Retorna:
        Distancia en kilómetros (float)
    """
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # Convertir grados a radianes, ya que las funciones trigonométricas
    # de Python trabajan en radianes
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    # Fórmula de Haversine
    a = (math.sin(delta_phi / 2) ** 2 +
         math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return RADIO_TIERRA_KM * c


def construir_matriz_distancias(coordenadas):
    """
    Construye la matriz de distancias N x N entre todas las ciudades,
    aplicando Haversine a cada par (i, j). Se calcula una sola vez al
    inicio para evitar recalcular distancias en cada generación del
    algoritmo genético (optimización de rendimiento).

    Parámetros:
        coordenadas: lista de tuplas (lat, lon)

    Retorna:
        Lista de listas (matriz) donde matriz[i][j] = distancia en km
        entre la ciudad i y la ciudad j.
    """
    n = len(coordenadas)
    matriz = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            d = haversine(coordenadas[i], coordenadas[j])
            # La matriz es simétrica: distancia(i, j) == distancia(j, i)
            matriz[i][j] = d
            matriz[j][i] = d

    return matriz
