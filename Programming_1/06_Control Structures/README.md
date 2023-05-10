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

#### E37 - PH
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

#### E38 Triangulo
Desarrolle un programa que permita leer el valor de 3 lados supuestamente de un triangulo y el programa realice lo siguiente:
- Verifique si con los 3 lados efectivamente se puede formar un tri´angulo y dar un mensaje al respecto. Recuerde que para que se pueda formar un tri´angulo es necesario que la suma de dos lados debe ser mayor que el tercer lado.
- Si se puede formar un tri´angulo, el programa debe indicar el tipo de tri´angulo es decir si es tri´angulo equil´atero, is´oceles o escaleno.
- Ademas debe hallar el ´area del tri´angulo, utilizando la f´ormula de Heron en donde el `area = (s * (s − l1) * (s − l2) * (s − l3)) ** 1/2`
Donde s: es el semiperimetro, 11, 12, 13 son los lados del triangulo.

Algunos ejemplos de dialogo de este programa serian:

Ejemplo 1:
```
Lado 1 : 3
Lado 2 : 4
Lado 3 : 5

Es un triangulo
Es triangulo escaleno
El area es : 6.0
```

Ejemplo 2:
```
Lado 1 : 7
Lado 2 : 7
Lado 3 : 7

Es un triangulo
Es triangulo equilatero
El area es : 21.21762239271875
```

Ejemplo 3:
```
Lado 1 : 2
Lado 2 : 2
Lado 3 : 5

No se puede formar un triangulo
```

Ejemplo 4:
```
Lado 1 : 5 
Lado 2 : 5 
Lado 3 : 3

Es un triangulo Es triangulo isoceles El area es : 7.1545440106270926
```

Ejemplo 5:
```
Lado 1 : 7
Lado 2 : 7
Lado 3 : 0

No se puede formar un triangulo
```

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

#### E49 Serie de potencia
Disene e implemente un programa para hallar la suma de los n primeros numeros de la siguiente serie:
```
1, 4, 9, 16, 25, 36, 49, 64, ...
```
- Para n = 2, la suma es 1 + 4 = 5
- Para n = 5, la suma es 1 + 4 + 9 + 16 + 25 = 55
- Para n = 7, la suma es 1 + 4 + 9 + 16 + 25 + 36 + 49 = 140
Algunas ejemplos de dialogo de este programa serian:

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

### for
#### E50 
Encuentra tres números diferentes  entre 1 y 12 cuya suma sea igual a 24.

#### E51
Usando nested loops (bucles anidados) imprime el siguiente patrón cuando n = 4.

```
*
* *
* * *
* * * *
```

#### E51
Usando nested loops (bucles anidados) imprime el siguiente patrón cuando n = 7.
```
*
***
*****
*******
```

#### E52
Usando nested loops (bucles anidados) imprime el siguiente patrón cuando n = 5.

```
     *
    * *
   * * *
  * * * *
 * * * * *
  * * * *
   * * *
    * *
     *
```

#### E53
Usando nested loops (bucles anidados) imprime el siguiente patrón cuando n = 5.
```
A
B C
D E F
G H I J
K L M N O
```

#### E54
Encuentra dos números  entre 1 y 12  que multiplicados den como resultado 12.

#### E55
Encuentra dos números  diferentes entre 1 y 100 que:
sean múltiplos de 7 
la suma de ambos 
```
A
B C
D E F
G H I J
K L M N O
```



#### E56
Realice un programa que lea como dato un número mayor a cero y el programa imprima un triángulo como se muesta enel ejemplo.

Ejecución 1
````
Filas: 11
    1
   123
  12345
 1234567
123456789
````
Ejecución 2
````
Filas: 24

````

#### E57

## Nested Control Structures
### if/if
#### E58 Generation
Desarrolle un programa que permita tener como datos:
- La fecha en que una persona nacio, en el formato: dia, mes. ano.
- La fecha actual, en el formato: dia, mes, ano.
Y el programa indique: la edad y a que generacion pertenece, considerando los datos de la siguiente tabla:

| Ano      | Generacion en el Peru   |
|----------|-------------------------|
| 13 - 20  | Generacion Z            |
| 21 -35   | Generacion Y            |
| 36 - 59  | Generacion X            |
| 60 a mas | Generacion Baby Boomers |

Si la edad de la persona es menor a 13, el programa debe imprimir "Su generacion aun no tiene nombre asignado".
- Note que para que el programa halle correctamente la respuesta se debe calcular primero la edad en anos de la persona.
- No es necesario que valide las fechas, puede trabajar bajo el supuesto que se ingersaran fechas correctas. Sin embargo debe realizar el calculo apropiado de la cantidad de anos.
ALgunos ejemplos de dialogo de este programa serian:

Ejemplo 1:
```
Fecha de nacimiento
Dia: 23
Mes: 6
Anio: 1983

Fecha actual
Dia: 14
Mes: 2
Anio: 2021

Su edad es: 37
Su generacion es la Generacion X
```

Ejemplo 2
```
Fecha de nacimiento
Dia: 15
Mes: 2
Anio: 1983

Fecha actual
Dia: 15
Mes: 2
Anio: 2021

Su edad es: 38
Su generacion es la Generacion X
```

Ejemplo 3:
```
Fecha de nacimiento
Dia: 23
Mes: 9
Anio: 1983

Fecha actual
Dia: 15
Mes: 2
Anio: 2021

Su edad es: 37
Su generacion es la Generacion X
```

Ejemplo 4:
```
Fecha de nacimiento
Dia: 27
Mes: 7
Anio: 2006

Fecha actual
Dia: 25
Mes: 12
Anio: 2020

Su edad es: 14
Su generacion es la Generacion Z
```

### While and if/elif/else
#### E59 TicTac
Desarrolle un programa que lea como dato un número cuyo valor puede ser desde 1 hasta el 500 y el programa cuente números desde 1 hasta el número que se ingresa como dato, pero con las siguientes indicaciones:

- Si el número es múltiplo de 4, debe mostrar el número y luego "Tic"
- Si el número es múltiplo de 6, debe mostrar el número y luego "Tac"
- Si el número es múltiplo de 4 y de 6, debe mostrar el número y luego "Tic Tac"
- En cualquier otro caso, solo debe mostrar el número

Ejemplo 1:
```
Número [1 - 500]: 700
Número [1 - 500]: 900
Número [1 - 500]: 34
1
2
3
4 Tic
5
6 Tac
7
8 Tic
9
10
11
12 TicTac
13
14
15
16 Tic
17
18 Tac
19
20 Tic
21
22
23
24 TicTac
25
26
27
28 Tic
29
30 Tac
31
32 Tic
33
34
Fin
```
Ejemplo2:
```
Número [1 - 500]: 20
1
2
3
4 Tic
5
6 Tac
7
8 Tic
9
10
11
12 TicTac
13
14
15
16 Tic
17
18 Tac
19
20 Tic
Fin
```

#### E58 Promedio de notas
Disene e implemente un algoritmo en Python que obtenga el promedio de un conjunto de notas ingresados por el usuario. Se debe contar solo las notas entre 0 y 20, ademas el usuario ingresara -1 para indicar que ya no ingresara mas notas.

Input:
```
15
8
12
24
14
-1
```
Output:
```
12.25
```

#### E Ingresa numeros y cuentalos
Realice un programa que permita leer varios numeros enteros hasta que se introduzca el cero.

Luego el programa mostrara lo siguiente:
- La cantidad de numeros leidos
- La cantidad de numeros pares
- La cantidad de numeros impares

El cero, no debe entrar en el conteo.

Ejemplo 1:
```
Numero [con 0 termina]: 4
Numero [con 0 termina]: 9
Numero [con 0 termina]: 12
Numero [con 0 termina]: 15
Numero [con 0 termina]: 21
Numero [con 0 termina]: 0

Numeros leidos: 5
Numeros pares: 2
Numeros impares: 3
```

Ejemplo 2:
```
Numero [con 0 termina]: 99
Numero [con 0 termina]: 123
Numero [con 0 termina]: 12
Numero [con 0 termina]: 6
Numero [con 0 termina]: 8
Numero [con 0 termina]: 44
Numero [con 0 termina]: 100
Numero [con 0 termina]: 0

Numeros leidos: 7
Numeros pares: 5
Numeros impares: 2
```

#### E Perros
Una veterinaria le ha solicitado crear un programa para calcular la edad aproximada
humana de sus pacientes caninos. El programa que usted realizará solicita un número
N que indica cuántos pacientes se atenderán. A continuación solicita la edad caninca
y el nombre de cada paciente. Por cada lectura, usted imprime el nombre y la edad real
aproxiamada humana:

Considere que la edad real aproximada se calcula con los siguientes criterios:
- Los 2 primeros años se consideran como 10.5 años humanos cada uno.
- Cada año adicional se considera como 4 años humanos
- Solo se considera edades en números enteros mayor o igual a 1. Se solicita que este
dato sea validado por su programa. Es decir si no ingresa un valor mayor o igual a 1,
debe volver a solicitar el dato.
- El texto de salida debe combinar el nombre y la edad equivalente, tal como se verá en
los ejemplos de entrada y salida del programa, que se muestran en la diapositiva siguiente.

Ejemplo 1:
```
Numeros de perritos: 4

Nombre del perro: Ruffo
Edad canina: -2
Edad canina: 0
Edad canina: -5
Edad canina: 4
La edad de Ruffo es de 29

Nombre del perro: Mirly
Edad canina: 12
La edad de Mirly es de: 61

Nombre del perro: Tifon
Edad canina: 6
La edad de Mirly es de: 37

Nombre del perro: Pinky
Edad canina: 3
La edad de Mirly es de: 25
```

Ejemplo 2:
```
Numero de perritos: 2

Nombre del perro: Suitan
Edad canina: 10
La edad de Mirly es de: 53

Nombre del perro: Argos
Edad canina: 1
La edad de Mirly es de: 10.5
```

#### Juego adivina el numero
Modifique el programa del juego en Python, con la finalidad que cuando imprima el mensaje "No adivino. Siga intentando", adicionalmente tambien imprima una ayuda senalando: "El numero a adivinar es menor" o "El numero a adivinar es mayor"


## E65 - Estaciones
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

