# RUN.md — Puesta en marcha del proyecto

Proyecto: **TSP con Algoritmo Genético Generacional aplicado a departamentos del Perú**
(distancias calculadas con la fórmula de Haversine).

Estas instrucciones asumen que acabas de clonar o descargar el código y que
trabajas en **Windows**, en la ruta `E:\Proyectos\genetico`, con **Python 3.12.3**
instalado.

## 1. Requisitos previos

- Python 3.12.3 instalado en el sistema.
- Verifica la versión disponible (puede variar el comando según tu instalación):

```powershell
python --version
# o, si tienes el Python Launcher de Windows con varias versiones instaladas:
py -3.12 --version
```

## 2. Crear la carpeta del proyecto (si no existe)

```powershell
mkdir E:\Proyectos\genetico
cd E:\Proyectos\genetico
```

Si ya descargaste/clonaste el código dentro de esa carpeta, simplemente navega a ella:

```powershell
cd E:\Proyectos\genetico
```

## 3. Crear el entorno virtual "venv" con Python 3.12.3

```powershell
py -3.12 -m venv venv
```

(Si `python --version` ya reporta 3.12.3 como versión por defecto, puedes usar
`python -m venv venv` en su lugar).

## 4. Activar el entorno virtual

En **PowerShell**:

```powershell
.\venv\Scripts\Activate.ps1
```

> Si PowerShell bloquea la ejecución de scripts, ejecuta una sola vez (como
> administrador o para el usuario actual):
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

En **CMD**:

```cmd
venv\Scripts\activate.bat
```

Al activarse correctamente, verás el prefijo `(venv)` al inicio de la línea de comandos.

## 5. Instalar las dependencias

```powershell
pip install -r requirements.txt
```

## 6. Ejecutar el script principal

```powershell
python main.py
```

Durante la ejecución verás en consola:
- La lista de departamentos cargados.
- El progreso del algoritmo genético cada 25 generaciones (mejor distancia
  encontrada y contador de generaciones sin mejora).
- El mensaje de activación del **early stopping** si el algoritmo deja de
  mejorar durante 50 generaciones consecutivas.
- El resumen final: distancia total de la mejor ruta y el orden de las
  ciudades a visitar.

## 7. Resultados generados

Al finalizar, el script crea la carpeta `output/` (si no existe) con dos imágenes:

- `output/convergencia.png` — gráfico de **Distancia vs. Generación**, mostrando
  cómo converge el algoritmo genético.
- `output/mejor_ruta.png` — mapa con la mejor ruta encontrada entre los
  departamentos.

## 8. Desactivar el entorno virtual (al terminar)

```powershell
deactivate
```

## Estructura del proyecto

```
genetico\
├── main.py                     # Script principal (orquesta todo el proceso)
├── requirements.txt            # Dependencias del proyecto
├── RUN.md                      # Este archivo
├── src\
│   ├── data.py                 # Departamentos del Perú y sus coordenadas
│   ├── haversine.py            # Fórmula de Haversine y matriz de distancias
│   ├── genetic_algorithm.py    # Algoritmo genético generacional (OX1, torneo, etc.)
│   └── visualization.py        # Gráficos de convergencia y de la ruta
├── output\                     # Se genera al ejecutar main.py (gráficos .png)
└── venv\                       # Entorno virtual (no versionar en git)
```

## Ajuste de parámetros

Los parámetros del algoritmo genético (tamaño de población, probabilidad de
cruce/mutación, tamaño del torneo, paciencia del early stopping, etc.) se
encuentran al inicio de `main.py` y pueden modificarse directamente ahí para
experimentar con distintas configuraciones.
