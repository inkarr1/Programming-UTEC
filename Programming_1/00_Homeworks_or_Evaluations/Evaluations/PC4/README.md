Se registran los codigos de los medicamentos con las primeras letra
de cada palabra del nombre, el numero cero y un numero correlativo.
Ejemplo de codigos utilizdos:
de un archivo medicamentos.txt
```
LS01, Levotiroxina sodica
MC01 , Metformina clorhidrato
AI01 , Aspirina infantil
CG01 , Clonazepam gotas
```
Se pide registrar nuevos codigo recibiendo el nombre del medicamento y el programa
debe generar una clave que no se repita con las anteriores usando numeros consecutivos para genere el numero al final del not codigo
Importante: Debes actualizar el archivo medicamentos.txt con los nuevos codigos.

Ejemplo:
Input:
````
Ingresar medicamento: Lorazepam solucion
````
Output:
````
LS01, Levotiroxina sodica
MC01 , Metformina clorhidrato
AI01 , Aspirina infantil
CG01 , Clonazepam gotas
LS02, Lorazepam solucion
````


## p3
La lista a continuacion contiene informacion de las ciudades del Peru y tiene datos como: 
el departamento, la altitud y poblacion de la ciudad.

```
lista = [
{'ciudad':'La Rinconada', 'altitud': 5100, 'departamento':'Puno', 'poblacion': 17000},
{'ciudad':'Cerro de Pasco', 'altitud': 4380, 'departamento':'Pasco', 'poblacion': 66860},
{'ciudad':'Junin', 'altitud': 4105, 'departamento':'Junin', 'poblacion': 10000},
{'ciudad':'Yauri', 'altitud': 3976, 'departamento':'Cusco', 'poblacion': 29772},
{'ciudad':'Yanaoca', 'altitud': 3913, 'departamento':'Cusco', 'poblacion': 11000},
{'ciudad':'Ayaviri', 'altitud': 3907, 'departamento':'Puno', 'poblacion': 20152},
{'ciudad':'Lampa', 'altitud': 3878, 'departamento':'Puno', 'poblacion': 14780},
{'ciudad':'Ilave', 'altitud': 3862, 'departamento':'Puno', 'poblacion': 22153},
{'ciudad':'Azangaro', 'altitud': 3859, 'departamento':'Puno', 'poblacion': 35230},
{'ciudad':'Juli', 'altitud': 3850, 'departamento':'Puno', 'poblacion': 23741},
{'ciudad':'Yunguyo', 'altitud': 3847, 'departamento':'Puno', 'poblacion': 11890},
{'ciudad':'Juliaca', 'altitud': 3824, 'departamento':'Puno', 'poblacion': 216716},
{'ciudad':'Puno', 'altitud': 3810, 'departamento':'Puno', 'poblacion': 120229},
{'ciudad':'La Oroya', 'altitud': 3745, 'departamento':'Junín', 'poblacion': 29417},
{'ciudad':'Huancavelica', 'altitud': 3676, 'departamento':'Huancavelica', 'poblacion': 41331},
{'ciudad':'Sicuani', 'altitud': 3549, 'departamento':'Cusco', 'poblacion': 42551},
]
```
Usando la lista mostrada se te solicita realizar un programa que calcule la diferencia de
altitud y poblacion entre dos ciudades, si alguna ciudad no se encuentra se debe indicar
al usuario que no se puede calcular la diferencia.

Su programa debe solicitar el nombre de la ciudad y utilizar la busqueda binaria para 
reportar todos los datos del diccionario respectivo y luego realizar el calculo de la diferencia.

Ejemplo:
````
Ingrese la ciudad 1: Cerro de Pasco
{ 'ciudad': 'Cerro de Pasco' , 'altitud': 4380 , 'departamento':
'Pasco' , 'poblacion': 66860}
Ingrese la ciudad 2: La Oroya
{ 'ciudad': 'La Oroya' , 'altitud': 3745 , 'departamento':
'Junin' , 'poblacion': 29417}

Diferencia de altitud: 634
Diferencia de poblacion: 37443
````

La lista a continuacion contiene informacion de la calidad del aire de paises.

```
calidad_aire = [
{'pais':'Bhutan', 'aire': 28.71, 'expectativa': -2.32},
{'pais':'India', 'aire': 55.80, 'expectativa': -4.98},
{'pais':'Nepal', 'aire': 47.13, 'expectativa': -4.13},
{'pais':'Pakistan', 'aire': 44.17, 'expectativa': -3.84},
{'pais':'Rwanda', 'aire': 32.95, 'expectativa': -2.74},
{'pais':'Burundi', 'aire': 31.76, 'expectativa': -2.62},
{'pais':'China', 'aire': 31.63, 'expectativa': -2.61},
{'pais':'Equatorial Guinea', 'aire': 28.61, 'expectativa': -2.31},
{'pais':'Guatemala', 'aire': 28.45, 'expectativa': -2.30},
{'pais':'Bangladesh', 'aire': 75.76, 'expectativa': -6.93},
{'pais':'Cameroon', 'aire': 31.42, 'expectativa': -2.59},
{'pais':'Qatar', 'aire': 29.19, 'expectativa': -2.37},
{'pais':'Mongolia', 'aire': 31.47, 'expectativa': -2.59},
{'pais':'Laos', 'aire': 28.00, 'expectativa': -2.25},
]
```

Con la lista dada, solicitar al usuario porque campo desea realizar el ordenamiento: pa´ıs
o expectativa y ordenar de forma ascendente por expectativa y de forma descendente por
pa´ıs. Finalmente, debe imprimir el pa´ıs, calidad de aire y expectativa de vida reducida
en el orden solicitado.

Ejemplo 1:
````
Ingrese campo para ordenar ( pais , expectativa ) : expectativa
La lista ordenada por expectativa ascendentemente es :

    Bangladesh    75.76 -6.93
      India       55.8  -4.98
      Nepal       47.13 -4.13
     Pakistan     44.17 -3.84
      Rwanda      32.95 -2.74
     Burundi      31.76 -2.62
      China       31.63 -2.61
     Cameroon     31.42 -2.59
     Mongolia     31.47 -2.59
      Qatar       29.19 -2.37
      Bhutan      28.71 -2.32
Equatorial Guinea 28.61 -2.31
    Guatemala     28.45 -2.3
       Laos       28.0  -2.25
````

Ejemplo 2:
````
Ingrese campo para ordenar ( pais , expectativa ) : pais
La lista ordenada por pais descendentemente es :
Rwanda 32.95 -2.74
Qatar 29.19 -2.37
Pakistan 44.17 -3.84
Nepal 47.13 -4.13
Mongolia 31.47 -2.59
Laos 28.0 -2.25
India 55.8 -4.98
    Guatemala 28.45 -2.3
Equatorial Guinea 28.61 -2.31
      China 31.63 -2.61
     Cameroon 31.42 -2.59
     Burundi 31.76 -2.62
      Bhutan 28.71 -2.32
    Bangladesh 75.76 -6.93
````