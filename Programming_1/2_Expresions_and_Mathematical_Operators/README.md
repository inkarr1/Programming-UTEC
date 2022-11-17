# Ejercicios
### E17・Hallar el BMI
Desarrolle un programa que permita leer el peso de una persona expresado en gramos, la altura expresada en centímetros y el programa calcule el índice de masa corporal.

El índice de la masa corporal, de las siglas en inglés BMI se calcula utilizando la siguiente fórmula:

BMI = peso(Kg) / altura(m) * altura(m)

```
Input:
Ingrese el peso en grs: 8200
Ingrese la altura en cms: 170

Output:
El índice de masa corporal (BMI) es igual a: 2.837
```

### E18・Hallar distancia entre dos puntos
Desarrolle un programa que permita hallar la distancia entre dos puntos.
Puede utilizar la siguiente fórmula para calcular la distancia:

Distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1/2

### E19・Revertir un número de 3 dígitos
Realice un programa que permita leer un número entero de 3 dígitos y el programa imprima el número al revés.

Desarrolle el programa utilizando los operadores matemáticos y trabaje bajo el supuesto que el usuario siempre ingresará un número de 3 dígitos:

```
1°
Input:
Numero: 567

Output:
Numero invertido: 765

2°
Input: 
Numero: 104

Output:
Numero invertido: 401

3°
Input: 
Numero: 100
Numero invertido: 1
```

### E20・Convertir segundos a días, horas, minutos y segundos (E16)
Desarrolle un programa que permita convertir segundos a: días, horas, minutos y segundos. El programa deberá mostrar el equivalente de los segundos utilizando el formato:  
D:HH:MM:SS,  donde  D,HH,MM  y  SS  representan  los  días,  horas,  minutos  y  segundos respectivamente.  
Las horas, minutos y segundos deberá formatearse de tal manera que solo ocupe exactamente dos dígitos, incluyendo el 0 si es necesario.
```
1°
Input:
Segundos: 100000

Output:
Equivale a: 1 : 3 : 46 :  40

2°
Input:
Segundos 230000

Output:
Equivale a: 2 : 15 : 53 :20

3°
Input:
Segundos: 350

Output:
Equivale a: 0 : 0 : 5 : 50
```
[Resolution]()

### E21・Calcular el area de un poligono regular
Un poligono regular es aquel que tiene longitud de sus lados iguales y el angulo  entre los lados adyacentes es igual. Desarrolle un programa que permita calcular  el area de un pologino regular.

Puede calcular el area de un poligono regular utilizando la siguiente formula:
area = (n * (s ** 2)) / 4 * tan(pi / n)

Donde:
- s es la longitud de los lados
- n es el numero de lados

NOTA: Para calculo se requiere de PI y llamar a la funcion tan en la biblioteca
math:`from` math `import` pi, tan

[Resolution]()