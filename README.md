<div id="top"></div>

<br />
<div align="center">
  <a href="https://image.isu.pub/170818010004-890bd89904ad3bd71b4e466939f1030f/jpg/page_1_thumb_large.jpg">
    <img src="logo.jpg" alt="Logo" width="350" height="350">
  </a>

  <h3 align="center">Desarrollo de aplicaciones avanzadas</h3>

  <p align="center">
    TC3002B.201
    
  </p>
</div>
<br> <br>

# Elaborado por:

- [Martín Palomares García](https://github.com/MartinPaGarcia)
- [Marco Antonio Torres](https://github.com/marcotorresx)
- [Salomon Dabbah Beracha](https://github.com/SalomonDabs?tab=overview&from=2024-04-01&to=2024-04-29)

# PDF evidencia final
Aqui se encuentra el documento que incluye todas los rubros especificados en CANVAS para el entregable final, incluye las reglas de la gramática, demostraciones, llamadas a funciones, muestras de la asignación de variables, implementación de flujos de imágenes y aplicación de filtros de Open CV.

- [Evidencia Final Compiladores Desarrollo de herramienta de soporte al proceso de análisis de imágenes](/Evidencia%20Final%20Compiladores%20Desarrollo%20de%20herramienta%20de%20soporte%20al%20proceso%20de%20análisis%20de%20imágenes.pdf)
# Tabla de contenidos

<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li><a href="#propósito-del-proyecto">Acerca del proyecto</a></li>
    <li><a href="#descripción-de-los-componentes-clave">Descripción de los componentes clave</a></li>
    <li><a href="#cómo-instalar-el-repositorio">Instalación</a></li>
    <li><a href="#gramática">Gramática</a></li>
      <ul>
        <li><a href="#tabla-de-gramática">Tabla de gramática</a></li>
        <li><a href="#los-terminales">Símbolos terminales</a></li>
      </ul>
    </li>
    <li><a href="#cómo-usar-el-código"> Cómo usar el código</a></li>
      <ul>
        <li><a href="#nuestro-lenguaje-y-cómo-usarlo">Nuestro lenguaje y cómo usarlo</a></li>
        <li><a href="#operaciones-aritméticas">Operaciones aritméticas</a></li>
        <li><a href="#asignación-de-variables"> Asignación de variables</a></li>
          <ul>
            <li><a href="#operaciones-matemáticas-con-variables">Operaciones matemáticas con variables</a></li>
            <li><a href="#funciones-numpy">Funciones NumPy</a></li>
            <li><a href="#ejemplo-de-uso-de-nuestra-librería">Ejmeplos de uso</a></li>
                <li><a href="#tabla-de-funciones-numpy">Tabla de funciones NumPy</a></li>          
            </li>
          </ul>
        </li>
      </ul>
    </li>
    <ul>
        <li><a href="#tests">Tests</a></li>
      </ul>
  </ol>
</details>

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

# Gramática

Nuestra gramática está declarada en el documento [parser.out](/parser.out).

Esta [gramática](#gramática) describe un lenguaje de programación simple que incluye términos como variables, cadenas de texto, números y operadores aritméticos y de asignación, así como funciones y llamadas a funciones con parámetros. Los [terminales](#los-terminales) incluyen elementos como paréntesis, comas y conectores específicos, junto con operadores como suma, resta, multiplicación y división, y símbolos de asignación.

## Tabla de Gramática

```shell
Grammar

Rule 0     S' -> assignment
Rule 1     assignment -> VARIABLE SETTO expression
Rule 2     assignment -> VARIABLE SETTO flow
Rule 3     flow -> VARIABLE CONNECT flow_functions
Rule 4     flow_functions -> flow_function_call CONNECT flow_functions
Rule 5     flow_functions -> flow_function_call
Rule 6     flow_function_call -> VARIABLE LPAREN params RPAREN
Rule 7     assignment -> expression
Rule 8     expression -> expression PLUS term
Rule 9     expression -> expression MINUS term
Rule 10    expression -> term
Rule 11    expression -> string
Rule 12    string -> STRING
Rule 13    term -> term TIMES exponent
Rule 14    term -> term DIVIDE exponent
Rule 15    term -> exponent
Rule 16    exponent -> factor EXP factor
Rule 17    exponent -> factor
Rule 18    exponent -> LPAREN expression RPAREN
Rule 19    factor -> NUMBER
Rule 20    factor -> VARIABLE
Rule 21    factor -> function_call
Rule 22    function_call -> VARIABLE LPAREN RPAREN
Rule 23    function_call -> VARIABLE LPAREN params RPAREN
Rule 24    params -> params COMMA expression
Rule 25    params -> expression
```

## Los terminales

Terminals, with rules where they appear

```shell
Terminals, with rules where they appear

COMMA                : 24
CONNECT              : 3 4
DIVIDE               : 14
EXP                  : 16
LPAREN               : 6 18 22 23
MINUS                : 9
NUMBER               : 19
PLUS                 : 8
RPAREN               : 6 18 22 23
SETTO                : 1 2
STRING               : 12
TIMES                : 13
VARIABLE             : 1 2 3 6 20 22 23
error                :
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

### Tabla de Funciones (NumPy)

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

### Descripción de las funciones de Library

| Función    | Parámetro/s                 | Descripción                                                                                                                                                                                                                                                                                          |
| ---------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| load_image | imagen                      | Carga una imagen al compilador y la lee.                                                                                                                                                                                                                                                             |
| save_image | nombre_del_archivo, imagen  | Guarda la imagen en el dispositivo con el nombre seleccionado.                                                                                                                                                                                                                                       |
| show_image | imagen                      | Despliega la imagen en el dispositivo.                                                                                                                                                                                                                                                               |
| search_cv2 | nombre_de_la_funcion        | Se usa para ver si una función existe en la librería de cv2, en caso de que exista, la función la regresa, de lo contrario arroja un error diciendo que no existe.                                                                                                                                   |
| gen_matrix | filas, columnas, argumentos | Crea una matriz de x filas, por y columnas, y se le introducen los argumentos, es importante tener en cuenta que se tienen que introducir la cantidad de argumentos resultante de la multiplicación de x por y, por ejemplo, si la matriz sería de 3 x 3 tendría que tener 9 argumentos exactamente. |
| gen_vector | argumentos                  | Crea un vector que contiene los argumentos que se le proporcionen.                                                                                                                                                                                                                                   |
| my_mean    | argumentos                  | Obtiene la media de los argumentos proporcionados.                                                                                                                                                                                                                                                   |
| my_sum     | argumentos                  | Obtiene la sumatoria de los argumentos proporcionados.                                                                                                                                                                                                                                               |
| my_median  | argumentos                  | Obtiene la mediana de los argumentos proporcionados.                                                                                                                                                                                                                                                 |
| my_std     | argumentos                  | Obtiene la desviación estándar de los argumentos proporcionados.                                                                                                                                                                                                                                     |
| my_max     | argumentos                  | Obtiene el elemento más grande de los argumentos proporcionados.                                                                                                                                                                                                                                     |
| my_min     | argumentos                  | Obtiene el elemento más pequeño de los argumentos proporcionados.                                                                                                                                                                                                                                    |
| my_sin     | argumentos                  | Obtiene los senos de los argumentos proporcionados.                                                                                                                                                                                                                                                  |
| my_cos     | argumentos                  | Obtiene los cosenos de los argumentos proporcionados.                                                                                                                                                                                                                                                |
| my_tan     | argumentos                  | Obtiene las tangentes de los argumentos proporcionados.                                                                                                                                                                                                                                              |
| histogram  | imagen                      | Convierte la imagen a escala de grises y calcula su histograma, que muestra la distribución de intensidades de píxeles de 0 (negro) a 255 (blanco).                                                                                                                                                  |
| canny_edge | imagen                      | Convierte la imagen a escala de grises y detecta los bordes utilizando el método de Canny. Luego, muestra la imagen original y la imagen de los bordes.                                                                                                                                              |
| gray_scale | imagen                      | Carga la imagen y la convierte en blanco y negro.                                                                                                                                                                                                                                                    |

### Ejemplo de uso de nuestra librería

#### Funciones numpy

```shell
input>> a = 30
input>> b = 25
input>> c = 45
input>> my_mean(a,b,c)
3.333333333333332
```

# Tests
En esta sección se mostrarán los casos de prueba para nuestro compilador/traductor:

```shell
pemdas = 5 + (3 * 2) / 7 ^ 2 - 1
a = 1 + 1
b = a + 3
c = a + b
c
cadena = "hola"
cadena + "hola"
my_sum(a,b,c)
my_mean(a,b,c)
my_max(a,b,c)
my_min(a,b,c)
my_median(a,b,c)
my_std(a,b,c)
my_sin(a)
my_cos(a)
my_tan(a)
search_cv2("imread")
gen_matrix(3,3,1,2,3,4,5,6,7,8,9)
img = load_image("test.jpg")
canny = canny_edge("test.jpg")
hist = histogram("test.jpg")
show_image(img)
show_image(gray_scale("test.jpg"))
save_image("test2.jpg",img)
size = gen_vector(4,5)
img2 = img -> blur(size)-> blur(size)-> blur(size)  
show_image(img2)
```