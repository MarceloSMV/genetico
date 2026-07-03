"""
Punto de entrada principal del proyecto.

Resuelve el Problema del Agente Viajero (TSP) aplicado a una muestra
representativa de departamentos del Perú, mediante un Algoritmo
Genético Generacional, usando la fórmula de Haversine para calcular
distancias geográficas reales.

Uso:
    python main.py
"""

import os
import sys
import time

# En Windows, la consola por defecto puede usar una codificación distinta
# a UTF-8 (p. ej. cp1252), lo que distorsiona tildes y eñes al imprimir.
# Se reconfigura la salida estándar a UTF-8 para mostrar correctamente
# los nombres de los departamentos y los mensajes en español.
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

from src.data import obtener_ciudades
from src.haversine import construir_matriz_distancias
from src.genetic_algorithm import ejecutar_algoritmo_genetico
from src.visualization import graficar_convergencia, graficar_ruta

# --- Parámetros del algoritmo genético (ajustables) ---
TAMANO_POBLACION = 150
GENERACIONES_MAXIMAS = 1000        # tope de seguridad, evita ejecución infinita
PROBABILIDAD_CRUCE = 0.9
PROBABILIDAD_MUTACION = 0.02
TAMANO_TORNEO = 3
PACIENCIA_EARLY_STOPPING = 50      # generaciones sin mejora antes de detenerse

CARPETA_SALIDA = "output"


def main():
    os.makedirs(CARPETA_SALIDA, exist_ok=True)

    # 1. Cargar los datos: nombres y coordenadas (lat, lon) de los
    #    departamentos del Perú
    nombres, coordenadas = obtener_ciudades()
    print(f"Ciudades cargadas: {len(nombres)}")
    print(", ".join(nombres))
    print()

    # 2. Construir la matriz de distancias reales usando Haversine
    print("Calculando matriz de distancias (Haversine)...")
    matriz_distancias = construir_matriz_distancias(coordenadas)
    print("Matriz de distancias lista.\n")

    # 3. Ejecutar el Algoritmo Genético Generacional
    print("Iniciando Algoritmo Genético Generacional...\n")
    inicio = time.time()

    mejor_ruta, mejor_distancia, historial = ejecutar_algoritmo_genetico(
        matriz_distancias,
        tamano_poblacion=TAMANO_POBLACION,
        generaciones_maximas=GENERACIONES_MAXIMAS,
        prob_cruce=PROBABILIDAD_CRUCE,
        prob_mutacion=PROBABILIDAD_MUTACION,
        tamano_torneo=TAMANO_TORNEO,
        paciencia_early_stopping=PACIENCIA_EARLY_STOPPING,
        verbose=True,
    )

    duracion = time.time() - inicio

    # 4. Mostrar resultados finales
    print("\n" + "=" * 60)
    print("RESULTADO FINAL")
    print("=" * 60)
    print(f"Generaciones ejecutadas : {len(historial) - 1}")
    print(f"Tiempo de ejecución     : {duracion:.2f} segundos")
    print(f"Distancia total         : {mejor_distancia:.2f} km")
    print("Ruta óptima encontrada:")
    ruta_nombres = [nombres[i] for i in mejor_ruta] + [nombres[mejor_ruta[0]]]
    print("  " + " -> ".join(ruta_nombres))
    print("=" * 60 + "\n")

    # 5. Generar visualizaciones
    graficar_convergencia(historial, os.path.join(CARPETA_SALIDA, "convergencia.png"))
    graficar_ruta(mejor_ruta, coordenadas, nombres, os.path.join(CARPETA_SALIDA, "mejor_ruta.png"))


if __name__ == "__main__":
    main()
