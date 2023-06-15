# Practice
## E1 Evalua Listas
Desarrollar un programa que solicite un numero al usuario para generar numeros aleatorios de tres cifras, entre 100 y 999, almacenarlos en una lista del tamano ingresado por el usuario.
Luego, debes crear una nueva lista que contiene el penultimo divisor de cada numero aleatorio generado. Finalmente debes imprimir la lista con los divisores encontrados.

>IMPORTANTE: En este ejercicio debe utilizar la libreria random para generar la lista de numero aleatorios

## E2 Evalua Matrices
En este ejercicio debes generar una matriz de letras de forma aleatoria, y luego crear un string a partir de las letras de la matriz seleccionando las letras en posicion vertical a partir de una fila y columna indicada por el usuario.
Tu programa debe iniciar la matriz con las dimensiones ingresadas por el usuario, y debe mostrar la matriz generada. Luego debe solicitar al usuario una posicion de inicio y fin y un tamano para generar un string con las letras que se encuentran en la matriz usando las letras continuas en posicion vertical.
Si el tamano sobrepasa la matriz debe indicar que se sobrepaso el tamano de la matriz y que no se puede obtener el string.
Algunos ejemplos de dialogo de este programa serıan:


```
Ingrese las filas : 8
Ingrese las columnas : 3
```
```
D M D
G S H
S R T
E M Y
W Y H
M C R
M R Z
S W R
```
```
Ingrese la posicion de inicio de fila : 3
Ingrese la posicion de inicio de columna : 2
Ingrese tamano del string : 5
```
```
Resultado:
YHRZR
```

## E3 Evalua Listas por comprension
Realizar un programa que permita calcular la siguiente serie hasta un numero maximo de terminos indicado por el usuario:

```
S = (2/5) + (3/6) + (4/7) + (5/8) + ... + (n/(n+3))
```
Su programa debe solicitar al usuario una cantidad de terminos, y calcular los terminos
de la serie usando listas por comprension. Luego como resultado debe imprimir el ultimo
termino de la serie y la sumatoria de todos los terminos.

IMPORTANTE: En este ejercicio solo debes utilizar listas por comprensi´on.

```
Ingrese cuantos numeros desea calcular en la serie : 3
```
```
Resultados :
Ultimo termino : 0.571
Sumatoria : 1.471
```

## E4 Evalua Diccionarios
Un colegio esta utilizando codigos para las bicicletas de sus alumnos usando la primera
letra de su nombre, de su apellido y un numero.

```
codigos = {
'A1T': 'Alonso Tinoco',
'P1C': 'Pierina Carbajal',
'R1G': 'Rosa Guardia' ,
'P2C': 'Pablo Cusi'
}
```
Usando el diccionario brindado (esta disponible para descargar desde canvas), se te pide
registrar nuevos codigos recibiendo el nombre y apellido de los alumnos. Tu programa
debe generar una clave que no se repita en el diccionario usando numeros consecutivos
para el numero que se encuentra al medio del codigo.

IMPORTANTE: Debes utilizar el diccionario brindado y actualizarlo con los nuevos codigos.

```
Ingresar nombre : Patricia
Ingresar apellido : Cerpa
```
```
Resultado :
{ 'A1T': 'Alonso Tinoco' , 'P1C': 'Pierina Carbajal' , 'R1G': 'Rosa Guardia' , 'P2C': 'Pablo Cusi' , 'P3C': 'Patricia Cerpa' }
```
