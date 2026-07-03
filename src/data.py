"""
Datos geográficos de entrada para el problema del Agente Viajero (TSP).

Se utiliza una muestra representativa de 15 departamentos del Perú
(cubriendo costa, sierra y selva), identificados por la ubicación de
su capital departamental. Las coordenadas (latitud, longitud) son
valores reales en grados decimales (WGS84), obtenidos de fuentes
geográficas públicas (Google Maps / Wikipedia).
"""

# Diccionario: nombre del departamento -> (latitud, longitud)
DEPARTAMENTOS = {
    "Lima": (-12.0464, -77.0428),
    "Arequipa": (-16.4090, -71.5375),
    "La Libertad (Trujillo)": (-8.1116, -79.0288),
    "Lambayeque (Chiclayo)": (-6.7714, -79.8409),
    "Piura": (-5.1945, -80.6328),
    "Cusco": (-13.5319, -71.9675),
    "Loreto (Iquitos)": (-3.7491, -73.2538),
    "Junín (Huancayo)": (-12.0651, -75.2049),
    "Puno": (-15.8402, -70.0219),
    "Tacna": (-18.0146, -70.2534),
    "Ica": (-14.0678, -75.7286),
    "Cajamarca": (-7.1638, -78.5003),
    "Ayacucho": (-13.1588, -74.2232),
    "Tumbes": (-3.5669, -80.4515),
    "Ucayali (Pucallpa)": (-8.3791, -74.5539),
}


def obtener_ciudades():
    """
    Devuelve dos listas alineadas por índice:
      - nombres: lista de nombres de departamentos
      - coordenadas: lista de tuplas (lat, lon) en grados decimales

    Trabajar con listas alineadas por índice simplifica la codificación
    del cromosoma del algoritmo genético, donde cada gen es simplemente
    un índice entero que representa una ciudad.
    """
    nombres = list(DEPARTAMENTOS.keys())
    coordenadas = [DEPARTAMENTOS[nombre] for nombre in nombres]
    return nombres, coordenadas
