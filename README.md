# Propósito del proyecto

Este código proporciona un lenguaje simple para procesar datos, manejar tareas básicas de visualización de imágenes y realizar cálculos matemáticos.

En nuestro código se pueden encontrar los isguientes componentes:

- Un lexer: Analiza el texto de entrada y divide el código en tokens reconocibles (números, variables y símbolos matemáticos, etc.).
- Un parser: Comprende la estructura gramatical del código de entrada, usando las reglas definidas por la gramática, y crea un árbol de análisis para representar operaciones que se analizarán.
- Un intérprete: Ejecuta el código representando el árbol de análisis, realizando los cálculos y operaciones necesarias.
- Manejo de funciones: Incluye funciones predefinidas para las operaciones usuales y permite la incorporación de funciones externas de librerías como Numpy y OpenCV.

# Descripción de los componentes clave

- Symbol table: Almacena variables definidas por el usuario y sus correspondientes valores.
- Funciones predefinidas: Incluye funciones comunes como print(), operaciones matemáticas básicas, y funciones para manipular imágenes con OpenCV (load_image(), show_image(), etc.).
- Implementación de histogram(): Permite la visualización de histogramas de los datos de una imagen a partir de OpenCV.
- Mecanismo de flujo/encadenamiento (flow flow_functions): Facilita la conexión de funciones entre sí para realizar un procesamiento encadenado o secuencial de los datos.

# Cómo instalar el repositorio

Para poder instalar instalar el repositorio, puede utilizar el siguiente comando:

```shell
git clone https://github.com/MartinPaGarcia/Desarrollo-de-aplicaciones-avanzadas.git
```

Una vez descargado nuestro repositorio en su ordenador, entrará a su editor de texto de preferencia y abrirá la carpeta dentro de su editor de texto.

Para ejecutar el código, tendrá que tener instalada la última versión de python en su ordenador junto con las siguientes librerías

Para instalar python en su ordenador podrá hacerlo desde esta página:

- [Descargar Python](https://www.python.org/downloads/windows/)
- [Descargar pip](https://pip.pypa.io/en/stable/installation/)

Una vez instalada python y pip, podrá instalar las siguientes librerías:

```shell
pip install numpy
pip install opencv-python
pip install matplotlib
pip install networkx
pip install py-yacc
pip install lex2
```

# Cómo usar el código:

Para poder hacer uso del código, como ya se mencionó en [Cómo instalar el repositorio](#cómo-instalar-el-repositorio) es necesario tener todas las dependencias instaladas y tener nuestra carpeta abierta en su editor de texto de preferencia, una vez realizado todo ese proceso, podremos comenzar ejecutando el código desde su terminal o la terminal de su editor de texto.

```shell
python translator.py
```

## Nuestro lenguaje y cómo usarlo

Nuestro lenguaje es simple y sencillo de usar, contamos con las siguientes palabras clave:

Para las variables es tan simple como escribir la palabra deseada, sin "" comillas. Hay que tener en cuenta que siempre que se coloque una variable, es importante primero, que esté [asignado](#asignación-de-variables), sino se mostrará el siguiente error.

```shell
input>> n
KeyError: 'n'
```

También es posible realizar operaciones aritméticas con nuestro lenguaje, para ello podemos ir a la sección de [operaciones aritméticas](#operaciones-aritméticas).

Para nuestro proyecto no incluimos operaciones lógicas en nuestro lexer, sin embargo, es posible realizar operaciones matemáticas más avanzadas, haciendo uso de nuestra librería que incluye la librería de Numpy, OpenCV, entre otras, con la finalidad de ampliar el uso de nuestro lenguaje.

## Operaciones aritméticas

```console
input>> 9+3
12
input>> 9-3
6
input>> 9*3
27
input>> 9/3
3.0
```

## Asignación de variables

Para poder hacer una correcta asignación de variables, necesitamos escribirla de la siguiente manera.

```shell
input>> a = 1
```

### Operaciones matemáticas con variables

```shell
input>> a = 1
input>> b = 2
input>> a + b
```

### Funciones (NumPy)

| Función             | Uso             |
| ------------------- | --------------- |
| Suma                | my_sum(args)    |
| Promedio            | my_mean(args)   |
| Mediana             | my_median(args) |
| Desviación Estándar | my_std(args)    |
| Valor Máximo        | my_max(args)    |
| Valor Mínimo        | my_min(args)    |
| Seno                | my_sin(args)    |
| Coseno              | my_cos(args)    |
| Tangente            | my_tan(args)    |



### Ejemplo de uso de nuestra librería

#### Funciones numpy

```shell
input>> a = 30
input>> b = 25
input>> c = 45
input>> my_mean(a,b,c)
3.333333333333332
```
