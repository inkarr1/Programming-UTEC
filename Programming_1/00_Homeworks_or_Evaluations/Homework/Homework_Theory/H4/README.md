# H4

## E1 Ordenando tareas
Usted es un empleado de una empresa que busca elaborar un algoritmo capaz de ordenar
las tareas que se tienen a partir de las diferentes caracteristicas de la tarea. El algoritmo
recibira una lista con las tareas, cada una en formato de diccionario; el valor a ordenar; y si
se desea ordenar de forma ascendente o descendente.

### 1.1. Ejemplo de formato de tarea
```
tareas = [
{
    'id': 1 ,
    'descripcion': 'Tarea 1',
    'importancia' ’: 1
},
{
    'id': 2,
    'descripcion': 'Tarea 2',
    'importancia': 2
},
]
```
La funci´on debe retornar la lista de diccionarios ordenado.

NOTA: La funcion interpreta el tipo de ordenamiento de la siguiente forma: ascendente:
'asc' y descendente: 'desc'

## E2 Tareas especificas
La misma empresa, te ha solicitado ahora un algoritmo de busqueda para poder saber si existe
o no la tarea x. Para esta ocasion te solicitan hacer una funcion recursiva de busqueda.

Nota: Asumir que el input es una lista de diccionarios ordenada de tareas por su id
y la busqueda se realizara por el valor del id.

### 2.1. Ejemplo de formato de diccionario
```
tareas = [
{
    'id': 1 ,
    'descripcion': 'Tarea 1',
    'importancia': 1
},
{
    'id': 2,
    'descripcion': 'Tarea 2',
    'importancia': 2
},
]
```
### 2.2. Ejemplo de input-output
**Input**
```
pregunta2([
{
    'id': 1 ,
    'descripcion': 'Tarea 1',
    'importancia': 1
},
{
    'id': 2,
    'descripcion': 'Tarea 2',
    'importancia': 2
},
], 1)
```
**Output**
```
{'id': 1, 'descripcion': 'Tarea 1', 'importancia': 1}
```


## E3 Sistema de gestion de inventario de una libreria en linea
Se te ha asignado la tarea de desarrollar un sistema de gesti´on de inventario para una librer´ıa
en l´ınea. El sistema debe manejar varias operaciones relacionadas con el inventario de libros,
incluyendo la b´usqueda de libros, la clasificaci´on de libros y la gesti´on de la informaci´on de
los libros utilizando diccionarios.
El inventario se almacena como una lista de diccionarios que contienen informaci´on del
libro, como t´ıtulo, autor, precio y cantidad disponible. Aqu´ı tienes un ejemplo de representaci´on de un libro en el diccionario de inventario:

```
inventario = [
    {
    'titulo': 'El Gran Gatsby',
    'autor': 'F. Scott Fitzgerald',
    'precio': 12.99,
    'cantidad': 5
    },
    {
    'titulo': 'Matar a un ruisenor',
    'autor': 'Harper Lee',
    'precio': 9.99,
    'cantidad': 8
    }
]
```

Debes implementar las siguientes funcionalidades:
- Busqueda: El sistema debe permitir a los usuarios buscar libros por t´ıtulo o autor. Dada una consulta de b´usqueda, el sistema debe recorrer el diccionario de inventario
y devolver una lista de libros que coincidan exactamente con la consulta de b´usqueda. Coincidencias parciales no se toman en consideracion.
- Clasificacion: El sistema debe proporcionar opciones de clasificaci´on para mostrar
los libros. Los usuarios deben poder ordenar los libros por t´ıtulo o precio en orden
ascendente o descendente. El algoritmo de clasificaci´on debe utilizar recursividad para
lograr el orden de clasificaci´on deseado.


NOTA 1: La funcion de busqueda es realizada sobre un arreglo de diccionarios desordenada.

NOTA 2: Al llamar a la funcion pregunta 3 se envian los siguientes parametros respetando
el orden Diccionario, tipo de funcionalidad, nombre de columna, valor a buscar, tipo de ordenamiento. 
Cuando se desea realizar la funcionalidad de Clasificacion el parametro de valor se ingresa como comillas vacias. Mientras que al llamar a la funcion en modo de Busqueda
el parametro de ord type es en comillas simples.

**Input**
```
pregunta3 ([{ ’ titulo ’: ’El Gran Gatsby ’ ,
’ autor ’: ’F. Scott Fitzgerald ’ ,
’ precio ’: 12.99 ,
’ cantidad ’: 5} ,
{ ’ titulo ’: ’ Matar a un ruisenor ’ ,
’ autor ’: ’ Harper Lee ’ ,
’ precio ’: 9.99 ,
’ cantidad ’: 8} ,
{ ’ titulo ’: ’ Cronica de una muerte anunciada ’ ,
’ autor ’: ’ Gabriel Garcia Marquez ’ ,
’ precio ’: 9.45 ,
’ cantidad ’: 10} ,
{ ’ titulo ’: ’ La lluvia sabe por que ’ ,
’ autor ’: ’ Mar ´ı a Fernanda Heredia ’ ,
’ precio ’: 10 ,
’ cantidad ’: 4}] , ’ Clasificacion ’ , ’ titulo ’ , ’’, ’asc ’)

```

**Output**
```
[{
’ titulo ’: ’ Cronica de una muerte anunciada ’ ,
’ autor ’: ’ Gabriel Garcia Marquez ’ ,
’ precio ’: 9.45 ,
’ cantidad ’: 10 ,
} ,
{
’ titulo ’: ’ El Gran Gatsby ’ ,
’ autor ’: ’F. Scott Fitzgerald ’ ,
’ precio ’: 12.99 ,
’ cantidad ’: 5
} ,
{
’ titulo ’: ’ La lluvia sabe por que ’ ,
’ autor ’: ’ Mar ´ı a Fernanda Heredia ’
’ precio ’: 10 ,
’ cantidad ’: 4
} ,
{
’ titulo ’: ’ Matar a un ruisenor ’ ,
’ autor ’: ’ Harper Lee ’ ,
’ precio ’: 9.99 ,
’ cantidad ’: 8}]

```

**Input**
```
pregunta3 ([{ ’ titulo ’: ’El Gran Gatsby ’ ,
’ autor ’: ’F. Scott Fitzgerald ’ ,
’ precio ’: 12.99 ,
’ cantidad ’: 5} ,
{ ’ titulo ’: ’ Matar a un ruisenor ’ ,
’ autor ’: ’ Harper Lee ’ ,
’ precio ’: 9.99 ,
’ cantidad ’: 8} ,
{ ’ titulo ’: ’ Cronica de una muerte anunciada ’ ,
’ autor ’: ’ Gabriel Garcia Marquez ’ ,
’ precio ’: 9.45 ,
’ cantidad ’: 10} ,
{ ’ titulo ’: ’ La lluvia sabe por que ’ ,
’ autor ’: ’ Mar ´ı a Fernanda Heredia ’ ,
’ precio ’: 10 ,
’ cantidad ’: 4}] , ’ Busqueda ’ , ’ autor ’ , ’Gabriel Garcia’, ’’)
```

**Output**
```
{
’ titulo ’: ’ Cronica de una muerte anunciada ’ ,
’ autor ’: ’ Gabriel Garcia Marquez ’ ,
’ precio ’: 9.45 ,
’ cantidad ’: 10 ,
}

```