"""
Módulo de visualización de resultados del algoritmo genético.

Genera dos gráficos con matplotlib:
1. Curva de convergencia: Distancia (eje Y) vs. Generación (eje X),
   requerida explícitamente para observar cómo mejora la solución.
2. Mapa de la mejor ruta encontrada, como visualización complementaria
   que facilita interpretar el resultado sobre el mapa del Perú.
"""

import matplotlib
matplotlib.use("Agg")  # backend sin interfaz gráfica, guarda directo a archivo
import matplotlib.pyplot as plt


def graficar_convergencia(historial, ruta_salida="output/convergencia.png"):
    """
    Grafica la evolución de la mejor distancia encontrada a lo largo
    de las generaciones, permitiendo visualizar la convergencia del
    algoritmo genético.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(historial)), historial, color="#2E86AB", linewidth=2)
    plt.title("Convergencia del Algoritmo Genético - TSP Departamentos del Perú")
    plt.xlabel("Generación")
    plt.ylabel("Distancia total de la mejor ruta (km)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()
    print(f"Gráfico de convergencia guardado en: {ruta_salida}")


def graficar_ruta(mejor_ruta, coordenadas, nombres, ruta_salida="output/mejor_ruta.png"):
    """
    Grafica la mejor ruta encontrada sobre un plano de latitud/longitud,
    mostrando el orden en que el agente viajero visita cada departamento
    y el regreso al punto de partida (ciclo cerrado).
    """
    # Se grafica con longitud en X y latitud en Y para que la forma se
    # asemeje a un mapa real (longitud = eje horizontal)
    xs = [coordenadas[i][1] for i in mejor_ruta] + [coordenadas[mejor_ruta[0]][1]]
    ys = [coordenadas[i][0] for i in mejor_ruta] + [coordenadas[mejor_ruta[0]][0]]

    plt.figure(figsize=(9, 11))
    plt.plot(xs, ys, "o-", color="#A23B72", linewidth=1.5, markersize=6)

    for i in mejor_ruta:
        plt.annotate(nombres[i], (coordenadas[i][1], coordenadas[i][0]),
                     textcoords="offset points", xytext=(5, 5), fontsize=8)

    # Resaltar el punto de partida/llegada
    plt.plot(xs[0], ys[0], "o", color="#F18F01", markersize=12, label="Inicio/Fin")

    plt.title("Mejor ruta encontrada (TSP - Algoritmo Genético)")
    plt.xlabel("Longitud")
    plt.ylabel("Latitud")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(ruta_salida, dpi=150)
    plt.close()
    print(f"Gráfico de la mejor ruta guardado en: {ruta_salida}")
