# Control Structures Exercises
## Selective Control Structures
### If
#### E29 Si es mayor de edad
Elaborar un algoritmo y un programa que solicite el nombre y la edad de una persona. 
Deberá imprimir un saludo: "Hola <nombre>". Además, otro mensaje si la persona tiene
18 años : "Usted debe tramitar ante RENIEC su DNI de mayor de edad".

### If and else
#### E30
Elaborar un algoritmo que evalúe una nota aprobatoria >= 11 e imprima un mensaje de felicitación.

### Elif
#### E31
Escribir  un programa que permita leer como dato un número entero y luego imprima si es positivo, negativo o es cero.

#### E32
Realice un programa que permita leer la edad de una persona y el programa determine el costo
de la entrada del cine, según la tabla:

|  Edad      |  Precio en soles  |
|------------|-------------------|
|  0-17      |  15               |
|  18- 30    |  25               |
|  31 - 45   |  30               |
|  46 a mas  |  10               |


#### E33
Cada denominación monetaria del dólar tiene asociado a un personaje con algún tipo de relevancia
histórica, usualmente presidentes y héroes. Aunque existen denominaciones de 500, 1000, 5000 y 10 000
para uso público estas denominaciones han sido descontinuadas en 1969. A continuación, mostramos la lista
vigente:

|  Personaje           |  Denominación  |
|----------------------|----------------|
|  George Washington   |  1             |
|  Thomas Jefferson    |  2             |
|  Abraham Lincoln     |  5             |
|  Alexander Hamilton  |  10            |
|  Andrew Jackson      |  20            |
|  Ulysses S. Grant    |  50            |
|  Benjamin Franklin   |  100           |

Escribir un programa que lea la denominación y que muestre  el nombre del personaje, en el caso de los
billetes de 500, 1000, 5000 y 10000 deberá mostrarse el mensaje "Denominación descontinuada" en otros
valores deberá mostrar "No existe esa denominación"


#### E34
Escribir un programa que permita ingresar 3 edades e indique cuál es el mayor

#### E35
Escribir un programa que permita ingresar un número del 1-7 y muestre su equivalente en letras.
Ejemplo: 1 = Lunes, 2 = Martes, 3 = Miércoles, 4 = Jueves, etc. Si esta fuera el rango mostrar el mensaje error.

#### E36
Escribir un programa en Python que permita ingresar un número del 1-12 y muestre el mes que
corresponde y la estación a la que pertenece.
Ejemplo: 1 = Enero, 2 = Febrero, 3 = Marzo, etc.


## Repetitive Control Structures
### while
#### E37
Disene e implemente un algoritmo en Python que imprima los numeros del 1 al 5.

#### E38
Disene e implemente un algoritmo en Python que imprima los numeros del 5 al 35 en 5 en 5.

#### E39
Disene e implemente un algoritmo que imprima los numeros pares del 10 al 0.

#### E40
Disene e implemente un algoritmo que imprima los numeros de la siguiente serie: 1, 2, 4, 8, 16, ... hasta el termino 'n' ingresado por el usuario.

#### E41 IMPRIME NÚMEROS PARES
Diseñe e implemente un algoritmo en Python que permita al usuario ingresar un número,
y el algoritmo debe imprimir los números pares, desde cero hasta el número ingresado.

Input
```
12
```

Output
```
0
2
4
6
8
10
12
```

#### E42 Promedio de un conjunto de numeros
Disene e implemente un algoritmo en Python que obtenga el promedio de un conjunto de numeros ingresados por el usuario. El usuario ingresara cero para indicar que ya no ingresara mas numeros. El cero no se considera en el promedio.

Input:
```
1
6
2
14
0
```

Output:
```
5.75
```

#### E43 Serie simple
Dada la serie: 1, 4, 9, 16, 25,36,...

Disene e implemente un algoritmo en Python que permita al usuario ingresar la cantidad de numeros a mostrar.
El algoritmo debe imprimir la secuecnia: 1, 4, 9, 16, 25, 36, ..., hasta el cuadrado del numero n.

Input
```
4
```

Output:
```
1
4
9
16
```

#### E44 TABLA DE MULTIPLICAR
Desarrolle un programa que imprima la tabla de multiplicar de un número n ingresado por teclado.

Input:
```
5
```

Output:
```
5x1=5
5x2=10
5x3=15
5x4=20
5x5=25
5x6=30
5x7=35
5x8=40
5x9=45
5x10=50
5x11=55
5x12=60
```

#### E45 Numeros multiplos
Desarrolle un programa que imprima los numeros multiplos de un numero n ingresado por teclado que se encuentran entre 1 y 50.

Input:
```
7
```

Output:
```
7
14
21
28
35
42
49
```

#### E46
Dada la serie: 2, 6, 12, 20, 30, 42, ...
Disene e implemente un algoritmo en Python que permita al usuario ingresar la cantidad de numeros a mostrar.
El algoritmo debe imprimir la secuencia: 2, 6, 12, 20, 30, 42, ..., hasta el numero `n x (n + 1)`.

Input: 
```
4
```

Output:
```
2
6
12
20
```
#### E47
Desarrolle un programa que permita hallar la sumatoria de la siguiente serie:
```
1 ** 5 + 2 ** 5 + 3 ** 5 + ... + n ** 5
```

La serie corresponde a los numeros naturales, en donde cada numero es elevado a la quinta. Se pide que realice un programa que lea como dato el numero del termino y halle la suma de los terminos de serie desde 1 hasta el numero que se ingreso como dato.

Ejemplo 1:
```
Valor de N: 3
La suma es: 276
```

Ejemplo 2:
```
Valor de N: 10
La suma es: 220825
```

#### E48
Desarrolle un programa que permita hallar el factorial de un nuemro entero positivo mayor que cero. El programa debe validar el ingreso del dato, de tal manera que solo acepte numeros mayores o iguales a 1.

Ejemplo 1:
```
Numero [mayor o igual a 1]: -3
Numero [mayor o igual a 1]: 0
Numero [mayor o igual a 1]: 5
El factorial es: 120
```

Ejemplo 2:
```
Numero [mayor o igual a 1]: 7
El factorial es: 5040
```


### for

## Nested Control Structures

#### Juego adivina el numero
Modifique el programa del juego en Python, con la finalidad que cuando imprima el mensaje "No adivino. Siga intentando", adicionalmente tambien imprima una ayuda senalando: "El numero a adivinar es menor" o "El numero a adivinar es mayor"


## E1 - Generaciones
Desarrolle un programa que permita tener como datos:
- La fecha en que una persona nació, en el formato: día, mes, año
- La fecha actual, en el formato: día, mes, año
Y el programa indique: **la edad y a qué generación pertenece**, considerando los
datos de la siguiente tabla:

| Año | Generación en el Perú |
| --- |-----------------------|
| 13- 20 | Generación Z |
| 21 - 35 | Generación Y |
| 36 - 59 | Generación X |
| 60 a más | Generación Baby Boomers |

Si la edad de la persona es menor a 13, el programa debe imprimir **"Su generación aun no tiene nombre asignado"**
- Note que para que el programa halle correctamente la respuesta, se debe calcular primero la edad en años de la persona.
- No es necesario que valide las fechas, puede trabajar bajo el supuesto que se ingresarán fechas correctas. Sin embargo debe realizar el cálculo apropiado de la cantidad de años.

Algunos ejemplos de diálogo de este programa serían:

Ejemplo 1:
```
Fecha de nacimiento
Día: 23
Mes: 6
Año: 1983

Fecha actual
Día: 14
Mes: 2
Año: 2021

Su edad es: 37
Su generación es la Generación X
```

Ejemplo 2:
```
Fecha de nacimiento
Día: 15
Mes: 2
Año: 1983

Fecha actual
Día: 15
Mes: 2
Año: 2021

Su edad es: 38
Su generación es la Generación X
```

Ejemplo 3:
```
Fecha de nacimiento
Día: 23
Mes: 9
Año: 1983

Fecha actual
Día: 15
Mes: 2
Año: 2021

Su edad es: 37
Su generación es la Generación X
```

Ejemplo 4:
```
Fecha de nacimiento
Día: 27
Mes: 7
Año: 2006

Fecha actual
Día: 25
Mes: 12
Año: 2020

Su edad es: 14
Su generación es la Generación Z
```

## E2 - Serie
Diseñe e implemente un pograma para hallar la suma de los **n** primeros números de la siguiente serie:

1, 4, 9, 16, 25, 36, 49, 64, ...

Para n = 2, la suma es 1 + 4 = 5
Para n= 5, la suma es 1 + 4 + 9 + 16 + 25 = 55
Para n = 7, la suma es 1 + 4 + 9 + 16 + 25 + 36 + 49 = 140

Algunos ejemplos de diálogo de este programa serían:

Ejemplo 1:
```
n: 5
suma: 55
```

Ejemplo 2:
```
n: 7
suma: 140
```
## E3 - Estaciones
Un profesor desea contar con un programa que le permita saber los porcentajes de
alumnos de su sección que han nacido en cada una de las estaciones del año.
Para ello se pide que elabore un programa que:
- Lea como dato la cantidad de alumnos, **dato que debe ser mayor a 5 y menor a 41**. El programa debe validar el ingreso de esta información.
- Permita a cada alumno ingresar el día y el mes en que nació. No es necesario validar el día y mes, se trabajará bajo la premisa que cada alumno ingresará datos correctos.
Con esta información se realizará el cálculo de los porcentajes de nacimiento en cada estación de año.
- Finalmente, el programa mostrará los porcentajes.
Se le recuerda que las estaciones estan marcadas de acuerdo a las fechas que se indican en la siguiente tabla:

| Estación | Inicio | Fin |
| --- | --- | --- |
| Verano | 21 Diciembre | 20 Marzo |
| Otoño | 21 Marzo | 21 Junio |
| Invierno | 22 Junio | 22 Setiembre |
| Primavera | 23 Setiembre | 20 Diciembre |

Algunos ejemplos de diálogo de este programa serían:

Ejemplo 1:
```
Número de alumnos [6 - 40]: 3
Número de alumnos [6 - 40]: 44
Número de alumnos [6 - 40]: 7
Fecha de nacimiento
Día: 27
Mes: 9
Fecha de nacimiento
Día: 28
Mes: 9
Fecha de nacimiento
Día: 29
Mes: 9
Fecha de nacimiento
Día: 2
Mes: 10
Fecha de nacimiento
Día: 30
Mes: 6
Fecha de nacimiento
Día: 28
Mes: 6
Fecha de nacimiento
Día: 27
Mes: 6

Reporte

Nacidos en verano: 0.000
Nacidos en otoño: 0.000
Nacidos en invierno: 42.857
Nacidos en primavera: 57.143
```

Ejemplo 2:
```
Número de alumnos [6 - 40]: 10
Fecha de nacimiento
Día: 30
Mes: 12
Fecha de nacimiento
Día: 2
Mes: 2
Fecha de nacimiento
Día: 5
Mes: 1
Fecha de nacimiento
Día: 23
Mes: 1
Fecha de nacimiento
Día: 5
Mes: 5
Fecha de nacimiento
Día: 6
Mes: 5
Fecha de nacimiento
Día: 12
Mes: 6
Fecha de nacimiento
Día: 10
Mes: 10
Fecha de nacimiento
Día: 11
Mes: 10
Fecha de nacimiento
Día: 12
Mes: 10

Reporte

Nacidos en verano: 40.000
Nacidos en otoño: 30.000
Nacidos en invierno: 0.000
Nacidos en primavera: 30.000
```

## E4 - PH
La escala de PH va desde el cero al 14 y permite medir el grado de acidez o alcalinidad.
En la siguiente tabla se indican los detalles:

| Grado ácido-base | Escala de PH |
| --- | --- |
| Muy ácido | 0 -1 |
| Moderadamente ácido | 2 - 4 |
| Ligeramente ácido | 5 - 6 |
| Neutro | 7 |
| Ligeramente básico | 8 - 9 |
| Moderadamente básico | 10 - 12 |
| Muy básico | 13 - 14 |

Realice un programa que permita el ingreso de la escala de PH y el programa indique el 
grado de Acido-Base que corresponde. Si se ingresa valores menores a cero o mayores a 14 debe indicar el mensaje "Error en el ingreso del dato".