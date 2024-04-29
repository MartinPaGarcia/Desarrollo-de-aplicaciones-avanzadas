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
              <ul>
                <li><a href="#tabla-de-funciones-numpy">Tabla de funciones NumPy</a></li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
    </li>
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

