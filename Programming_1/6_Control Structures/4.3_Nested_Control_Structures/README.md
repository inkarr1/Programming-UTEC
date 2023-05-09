# Nested Control Structures Exercises
## E1・TicTac
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

## E2 PROMEDIO DE UN CONJUNTO DE NÚMEROS
Diseñe e implemente un algoritmo en Python que obtenga el promedio de un conjunto de números ingresados por el usurio. El usuario ingresará cero para indicar que ya no ingresará más números. EL cero no se considera en el promedio.

## E3・(Lectura con centinela)
Diseñe e implemente un algoritmo en Python que obtenga el promedio de un conjunto de notas ingresados por el usuario. Se debe contar solo las notas entre 0 y 20, además el usuario ingresará -1 para indicar que ya no ingresará más notas.

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
## E4
Realice un programa, que permita leer varios números enteros hasta que se introduzca el cero.

Luego el programa mostrará lo siguiente:
- La cantidad de números leídos
- La cantidad de números pares
- La cantidad de números impares

El cero, no debe entrar en el conteo.

Ejemplo 1:
```
Número [con 0 termina]: 4
Número [con 0 termina]: 9
Número [con 0 termina]: 12
Número [con 0 termina]: 15
Número [con 0 termina]: 21
Número [con 0 termina]: 0

Número leídos: 5
Número pares: 2
Números impares: 3
```

Ejemplo 2:
```
Número [con 0 termina]: 99
Número [con 0 termina]: 123
Número [con 0 termina]: 12
Número [con 0 termina]: 6
Número [con 0 termina]: 44
Número [con 0 termina]: 100
Número [con 0 termina]: 0

Números leídos: 7
Números pares: 5
Números impares: 2
```
## E5
Realice un programa, que permita leer un número entero mayor que uno y determine si el número
es un número perfecto o no.
Un número es Perfecto, cuando el número es igual a la suma de sus divisores positivos menores
que él.
El 6 es un número perfecto porque la suma de sus divisores: 1 + 2 + 3 es igual a 6.
El 28 es un número Perfecto, porque la suma de sus divisores: 1 + 2 + 4 + 7 + 14 es igual a 28.

Ejemplo 1:
```
Número [Mayo a 1]: 0
Número [Mayo a 1]: -4
Número [Mayo a 1]: 28
El número es Perfecto
```

Ejemplo 2:
```
Número [mayor a 1]: 496
El número es Perfecto
```

Ejemplo 3:
```
Número [Mayo a 1]: 45
El número no es Perfecto
```

## E6
Una veterinaria le ha solicitado crear un programa para calcular la edad aproximada humana de
sus pacientes caninos. El programa que usted realizará solicita un número N que indica cuántos
pacientes se atenderán. A continuación solicita la edad caninca y el nombre de cada paciente. Por
cada lectura, usted imprime el nombre y la edad real aproximada humana:

Considere que la edad real aproximada se calcula con los siguientes criterios.

- Los 2 primeros años se consideran como 10.5 años humanos cada uno.}
- Cada año adicional se considera como 4 años humanos.
- Solo se considera edades en números enteros mayor o igual a 1. Se solicita que este dato 
sea validado por su progra. Es decir si no ingresa un valor mayor o igual a 1, debe volver a 
solicitar el dato.
- El texto de salida debe combinar el nombre y la edad equivalente, tal como se verá en los 
ejemplos de entrada y salida del programa, que se muestran en la diapositiva siguiente.

Ejemplo 1:
```
Número de perritos: 4

Nombre del perro: Ruffo
Edad canina: -2
Edad canina: 0
Edad canina: -5
Edad canina: 4
La edad de Ruffo es de 29

Nombre del perro: Mirly
Edad canina: 12
La edad de Mirly es de 61

Nombre del perro Tifon
Edad canina: 6
La edad de Tifon es de 37

Nombre del perro: Pinky
Edad canina: 3
La edad de Pinky es de 25
```

Ejemplo 2:
```
Número de perritos: 2

Nombre del perro: Sultan
Edad canina: 10
La edad de Sultan es de 53

Nombre del perro: Argos

```