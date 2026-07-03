# Algoritmo genético **Mg. Huarote Zegarra Raúl. rhuarote@untels.edu.pe** 

**Sesión 9** 

## : **Objetivos** 

- Comprenda la funcionalidad del algoritmo genético. 

- La utilidad del algoritmo genético. 

## TEMAS A TRATAR: 

- Introducción 

- Esquema básico 

- Codificación 

- Métodos 

- Ejemplos de aplicaciones de ejercicios. 

Motivación https://www.youtube.com/watch?v=06iwEZokIGk 

## Algoritmo genético 

Desde que el taxónomo Francés (Lamarck,1801) acuñó el nombre “biología” indica que los organismos desarrollan a lo largo de su vida estructuras que se adaptan a su ambiente, y que estas modificaciones estructurales del individuo son heredadas en las siguientes generaciones. 

Haciendo referencia a la publicación de (Charles Darwin,1859) donde menciona “sobrevive el más apto” donde pasará a la siguiente generación aquel que se adapte a los embates internos y externos. 

## **Historia - Algoritmo genético** 

Al dar una mirada desde el nacimiento del algoritmo genético, considerando al biólogo Fraser en [8] donde publicó una serie de investigaciones acerca de sistemas biológicos en una computadora digital, que no es más que la representación de Charles en [9] donde “sobrevive el más apto”. Simulados por Bremermann  en [10] y que posteriormente fue utilizada por Yovitts  en [11] acuñando el nombre de “Algoritmos Genéticos”, posteriormente Golberg  en [12] toma ésta idea como “métodos adaptativos, generalmente usados en problemas de búsqueda y optimización de parámetros, basados en la reproducción sexual y en el principio de supervivencia del más apto”. Para Jasbir  en [13] y Carlton  en [14] el algoritmo genético pertenece a la clase de métodos de optimización de búsqueda estocástica. 

## **¿Qué es? - Algoritmo genético** 

- “Métodos adaptativos, generalmente usados en problemas de búsqueda y optimización de parámetros, basados en la reproducción sexual y en el principio de supervivencia del más apto” (D. Golberg,1989). 

- Los organismos vivientes son consumados resolvedores de problemas. (John Holland, 1975 ) 

## **¿Qué es? - Algoritmo genético** 

- Por tanto, algoritmo genético es un modelo computacional de búsqueda de la posible mejor solución, basándose en la adaptación del modelo evolutivo. (Huarote , 2020). 

## **Evolución - Algoritmo genético** 

- Aquellos individuos que tienen más éxito en sobrevivir y en atraer compañeros tienen mayor probabilidad de generar un gran número de descendientes. 

- Esto significa que los genes de los individuos mejor adaptados se propagarán en sucesivas generaciones hacia un número de individuos creciente. 

- Las especies evolucionan logrando unas características cada vez mejor adaptadas al entorno en el que viven. 

- Los Algoritmos Genéticos usan una analogía directa con el comportamiento natural. 

## **Ventaja y Desventaja - Algoritmo genético** 

- No necesitan conocimientos específicos sobre el problema que intentan resolver. 

- Operan de forma simultánea con varias soluciones, en vez de trabajar de forma secuencial como las técnicas tradicionales. 

- Cuando se usan para problemas de optimización maximizar una función objetivo- resultan menos afectados por los máximos locales (falsas soluciones) que las técnicas tradicionales. 

- Resulta sumamente fácil ejecutarlos en las modernas arquitecturas masivamente paralelas. 

- **Ventaja y Desventaja - Algoritmo genético** 

- • Usan operadores probabilísticos, en vez de los típicos operadores determinísticos de las otras técnicas. 

- Pueden tardar mucho en converger, o no converger en absoluto, dependiendo en cierta medida de los parámetros que se utilicen tamaño de la población, número de generaciones, etc. 

- • Pueden converger prematuramente debido a una serie de problemas de diversa índole. 

## **Cuando usar - Algoritmo genético** 

No todos los problemas pudieran ser apropiados para la técnica, y se recomienda en general tomar en cuenta las siguientes características del mismo antes de intentar usarla: 

- Su espacio de búsqueda (i.e., sus posibles soluciones) debe estar delimitado dentro de un cierto rango. 

- Debe poderse definir una función de aptitud que nos indique qué tan buena o mala es una cierta respuesta. 

• Las soluciones deben codificarse de una forma que resulte relativamente fácil de implementar en la computadora. 

## **Enfoques - Algoritmo genético** 

- La Programación Genética 

- La Programación Evolutiva 

- Sistemas Clasificadores 

## ALGORITMOS PARA SOFTWARE AUTÓNOMO 

**Algoritmo genético** : Basándose en el modelo evolutivo de Charles Darwin, donde sobrevive el que más se adapta. Este es un método de búsqueda alternativo para tomar una posible mejor decisión. 

**==> picture [462 x 75] intentionally omitted <==**

**----- Start of picture text -----**<br>
SENSORES EFECTORE<br>S<br>/ DECISIÓN<br>. —> —<br>A™<br>Mejor acción<br>Percepciones<br>**----- End of picture text -----**<br>


## Codificación 

- Individuo: cromosoma 

- Cromosoma: cadena de caracteres 

   - En principio, cualquier representación es válida 

- Codificación óptima: alfabeto binario (teorema de los esquemas) 

- Codificación habitual: cadena de bits 

1 

4 

## **Esquema básico - Algoritmo genético** 

     

 

   

   

 

    

 

            

   

 

 

  

## **Población - Algoritmo genético** 

Población es el conjunto de elementos de referencia sobre el que se realizan las observaciones. Es necesario realizar un análisis de este concepto para el proceso del Algoritmo Genético, se consideran los siguientes dos puntos: 

- El tamaño de la población. Problemática en poblaciones pequeñas y extensas. 

- • La población inicial. Esto es como se le asignarán los valores a la población inicial. 

**Función objetivo (fitness) - Algoritmo genético** Esta función determina el grado de adaptación o aproximación de cada individuo al objetivo y por lo tanto permite distinguir a los mejores individuos de los peores. Por función entendemos una magnitud cuyo valor depende de una u otras variables. Ejemplo: 

- función objetivo f1(x1,x2,....xn), las variables estando sujetas a restricciones ( f2(x1,x2,...xn)= 0 o f2(x1,x2,...xn) ≥ 0 ...) 

- Aspectos relevantes: 

Determinación de una adecuada función de adaptación. 

Codificación utilizada. 

## Selección 

Selección de los elementos que se reproducen a partir de la función de aptitud 

- Varios métodos 

   - Rueda de ruleta 

   - Basado en el rango 

   - Selección de torneo 

   - Elitista 

- Cambio de generación 

   - Manteniendo el tamaño de la población 1 

   - Aumentando el tamaño de la evaluación 8 

## **Selección - Algoritmo genético** 

_La ruleta_ . 

Consiste en asignar una porción de la “ruleta” a cada individuo de forma que el tamaño de cada porción sea proporcional a su fitness. Los mejores individuos dispondrán de una porción mayor y por lo tanto de más posibilidades de ser seleccionados. 

## Rueda de ruleta 

Se asigna a cada individuo la probabilidad: 

 Si algún individuo domina la población, se escala o normaliza. 

 Se elijen parejas aleatorias de individuos de acuerdo a su probabilidad 

 Inconveniente: los individuos con más aptitud tiende a dominar la población en pocas generaciones 

_aptitud_ ( _x_ ) _x_ = Pr( ) _aptitud_ ( _y_ )  _y_  _población_ 

**==> picture [91 x 93] intentionally omitted <==**

**----- Start of picture text -----**<br>
4 1<br>3<br>2<br>**----- End of picture text -----**<br>


20 

## Ejemplos de codificación maximización función 

 f(x)=1-x[2] , parábola invertida con máximo en x=0 

 Único parámetro o atributo: variable x  Codificamos el valor de la variable mediante un byte [0,255], ajustado al intervalo real [-1,1], donde queremos hallar el máximo de la función 

**==> picture [267 x 220] intentionally omitted <==**

**----- Start of picture text -----**<br>
Valor  Descodi- Valor<br>ficación<br>binario real<br>10010100 148 0,161<br>10010001 145 0,137<br>00101001 41 -0,678<br>01000101 65 -0,490<br>=<br>2/255*x -1= y<br>**----- End of picture text -----**<br>


21 

## Rueda 

|Valor|Descodi|Valor|Aptitud|Probabilidad|Probabilidad|
|---|---|---|---|---|---|
|binario|-ficación|real|||acumulada|
|10010100|148 0,161|148 0,161|0.974|0.299|0.299|
|10010001|145|0,137|0.981|0.301|0.600|
|00101001|41|-0,678|0.540|0.166|0.766|
|01000101|65|-0,490|0.760|0.233|1.000|
|||4|1|||
|||3|2|||



22 

## Basado en el rango 

- Se ordena la población por orden creciente de aptitud 

- Se eliminan los M primeros (menor aptitud) 

- Se eligen de forma aleatoria, con probabilidad dada por el rango, pares de individuos y sus descendientes se añaden a la población 

2 

3 

## **Selección - Algoritmo genético** 

## _El Torneo_ . 

- Consiste en hacer competir a los individuos en grupos aleatorios (normalmente parejas), el que tenga el fitness más elevado será el ganador. 

- • Se seleccionan dos individuos aleatoriamente 

- Se elije el más apto con una probabilidad P y el menos apto con una probabilidad (1-P) 

- Introduce más diversidad en la población 

## Cambio de generación 

- Manteniendo el tamaño de la población intermedia 

   - Reemplazar padres por hijos 

   - Reemplazar un par de individuos elegidos aleatoriamente por los hijos 

   - Otros 

- Aumentando el tamaño de la población intermedia 

   - Crear población temporal con padres e hijos, seleccionando los mejores 

   - Dados n padres generar m (m>n) hijos y de ellos seleccionar los n mejores 2 5 

**Cruce - Algoritmo genético** “La riqueza no está en el azar, sino en la diversidad” 

Consiste en el intercambio de material genético entre dos elementos de un universo. 

Su función es mezclar las mejores características o propiedades  que se encuentran en los elementos de una población dada, y que serán los que den a los mismos una buena puntuación. El Cruzamiento es el principal operador genético, hasta el punto que se puede decir que no es un algoritmo genético si no tiene cruzamiento. 

## _crossover_ Operador de cruce ( ) 

- Principal operador genético 

- Simula el intercambio de material genético o genes 

- Se aplica con probabilidad pc a individuos seleccionados 

- Cruce ideal: recombina buenos bloques de construcción de sus progenitores 

- Operadores 

   - Cruce de n-puntos 

   - Cruce multipunto 2 

   - Cruce especializado 7 

## Cruce de un punto 

- Seleccionar aleatoriamente una posición en el cromosoma 

- Intercambiar el final del cromosoma a partir de dicho punto 

padre 

madre 

hijo 1 

hijo 2 

|1|0|0|1|1|0|1|1|0|0|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|1|0|1|1|0|1|0|0|0|0|
|||||||||||
|1|0|0|1|0|1|0|0|0|0|
|||||||||||
|1|0|1|1|1|0|1|1|0|0|



28 

## Cruce de dos puntos 

padre madre 

|1|0|0|1|1|0|1|1|0|0|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|1|0|1|1|0|1|0|0|0|0|



hijo 1 hijo 2 

|1|0|0|1|0|1|0|1|0|0|
|---|---|---|---|---|---|---|---|---|---|
|||||||||||
|1|0|1|1|1|0|1|0|0|0|



29 

## Otros operadores de cruce 

- Multipunto o uniforme 

   - Cada bit se hereda de un padre aleatoriamente 

- Operadores especializados 

 En aquellos problemas donde un cruce aleatorio puede generar individuos no válidos 

3 0 

## Ejemplo cruce 1 punto 8 reinas 

- La selección aleatoria del punto de cruce no es interesante 

   - Genera individuos válidos 

   - La mezcla de bloques –genes- no parece asimilable a un operador del problema real 

- Seleccionar aleatoriamente el gen a partir del que se hace el reemplazo 

   - Seleccionar aleatoriamente un entero 1 y 7 (número de genes) 3 

   - Equivale a intercambiar columnas contiguas 1 entre tableros padres 

Ejemplo cruce 1 punto 8 reinas Col.1 Col. 2 Col. 3 Col. 4 Col. 5 Col. 6 Col. 7 Col. 8 1 0 1 1 1 1 1 0 0 0 1 1 0 1 1 1 1 0 0 0 0 0 1 0 Col.1 Col. 2 Col. 3 Col. 4 Col. 5 Col. 6 Col. 7 Col. 8 1 1 0 1 1 1 1 0 1 1 1 0 0 1 0 1 1 0 0 0 1 0 1 1 Col.1 Col. 2 Col. 3 Col. 4 Col. 5 Col. 6 Col. 7 Col. 8 1 0 1 1 1 1 1 0 0 1 1 0 0 1 0 1 1 0 0 0 1 0 1 1 Col.1 Col. 2 Col. 3 Col. 4 Col. 5 Col. 6 Col. 7 Col. 8 1 1 0 1 1 1 1 0 1 0 1 1 0 1 1 1 1 0 0 0 0 0 1 0 3 2 

**==> picture [612 x 422] intentionally omitted <==**

**----- Start of picture text -----**<br>
Ejemplo cruce 1 punto 8 reinas<br>¤ ¤<br>¤ ¤<br>¤ ¤<br>Aptitud:20 ¤ padres ¤ ¤ Aptitud:26<br>¤<br>¤ ¤<br>¤ ¤<br>¤ ¤<br>¤ ¤<br>¤ ¤<br>¤ ¤<br>Aptitud:25 ¤ ¤ hijos ¤ Aptitud:27<br>¤<br>¤ ¤<br>¤ ¤<br>3 ¤ ¤<br>3<br>[=]<br>**----- End of picture text -----**<br>


## **Mutación - Algoritmo genético** 

Se considera un operador básico, que proporciona un pequeño elemento de aleatoriedad en el entorno de los individuos de la población. 

Una vez establecida la frecuencia de mutación, por ejemplo, uno por mil, se examina cada bit de cada cadena cuando se vaya a crear a un nuevo elemento a partir de sus padres. Si un número generado aleatoriamente está por debajo de esa probabilidad, se cambiará el bit (es decir, de 0 a 1 o de 1 a 0). Si no, se dejará como está. 

## Operador de Mutación 

- En la evolución 

   - Las mutaciones son poco frecuentes 

   - En la mayor parte de los casos letales 

- En promedio, contribuyen a la diversidad genética 

- En los algoritmos genéticos: 

   - Se simula cambiando aleatoriamente el valor de un bit 

   - Se aplica con probabilidad baja (10-3 o menor) a cada bit de un nuevo individuo, habitualmente junto al cruce 

   - Dependiendo del tamaño de la población y del 3 número de bits por individuo, la mutación puede 5 ser extremadamente rara en una generación 

## Utilidad de la mutación 

- Genera diversidad 

   - Puede ser de utilidad cuando un algoritmo genético está estancado 

   - Su abuso reduce al algoritmo genético a una búsqueda aleatoria 

- Otros mecanismos de generación de diversidad 

   - Aumentar el tamaño de la población 

   - Garantizar la aleatoriedad de la población inicial 

3 6 

## Otros operadores 

- Cromosomas de longitud variable 

   - Añadir, eliminar 

- Operadores de nicho 

   - Fuerzan a que cromosomas similares sólo reemplacen a cromosomas similares 

   - Intentan mantener la diversidad 

      - Distintas “especies” en la población 

 Cada una de ellas puede converger a un 3 máximo diferente 7 

## Mutación 

- Probabilidad mutación: 10[-3] 

- Suponer no se produce ninguna mutación 

3 8 

## Nueva población: reemplazar padres por hijos 

|Población 1ª|Población 1ª|x|aptitud|Probabilidad|Probabilidad|
|---|---|---|---|---|---|
|iteración||||selección|acumulada|
|h1<br>11011||27|729|0.44|0.44|
|h2<br>10000||16|256|0.15|0.59|
|h3<br>01100||8|64|0.04|0.63|
|h4<br>11001||25|625|0.37|1.00|
|Suma|||1674|||
|Media|||418,5|||
|mejor|||729|||



39 

## **Referencias - Algoritmo genético** 

[8]A. Fraser, “Simulation of genetic systems by automatic digital computers Introduction”, Aust. J. Biol Sci. Vol. 10, 1957. pp 484491. 

[9] D. Charles. “El origen de las especies”, London College of Cambridge, 1859. 

[10] H. J. Bremermann, “Optimization through evolution and recombination”, In Self-organization system, M. C. Yovitts et al. Spartan Books, Washinton, D. C. 1962. pp 93-106. [11] J. Holland, “Adaptation in Natural and Artificial Systems”, Cambridge, MA: MIT Press, 1992. 

[12] D. Golberg, “Genetics Algorithms in search, optimization and machine learning”, MA: Addison-Wesley Professional, 1989. [13] A. Jasbir, “Introduction to Optimum Design”, Elsevier Inc. Third Edition, 2012, USA, Chapter 16, pp 643. [14] J. S. Carlton, “Marine Propeller and Propulsion”, ButterworthHeinemann. FourthEdition, 2019, USA, pp 469-497. 

, 

## GRACIAS 

## **Tarea grupal de laboratorio** 

_Implementar el algoritmo del agente viajero en Python, usando algoritmo genético generacional, aplicado al caso real de las distancias de los departamentos del Perú. Nota 1: Las distancias lo puede obtener de Google maps. Nota 2: puede optar por otros puntos geolocalizados como: Distritos de Lima. Inkafarma de Lima Mifarma de Lima Grifos de Lima ( Repsol). Etc. Nota 3: Usar para encontrar la distancia el método de Haversin_ 

# **Tarea grupal de laboratorio** 

