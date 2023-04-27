# Selective
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