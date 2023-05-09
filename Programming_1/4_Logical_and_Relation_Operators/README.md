# Ejercicios
### E22・Electricity consume
Escriba un código que calcule el consumo de electricidad en soles dado el consumo en kW, con las siguientes condiciones:
- Si el consumo es menor o igual a 100kW, el kw cuesta 0.4522 soles.
- Si el consumo es mayor que 100kW, se aplica la tarifa anterior hasta 100kW y 0.7Soles por kW para el consumo sobre 100kW.

Realice el programa sin utilizar estructuras de control:

```
1°
Input:
Kw: 75
El monto a pagar es: 33.915

2º
Input:
Kw: 130

Output:
El monto a pagar es: 66.22
```
### E23・Par o Impar
Desarrolle un programa que permita leer un número entero y el programa indique si el 
número es par o impar.
Realice el programa sin utilizar estructuras de control.

```
Ejemplo 1:
Numero: 45
Es impar

Ejemplo 2:
Numero: 34
Es par

Ejemplo 3:
Numero: 0
Es par
```

### E24・Verificar si es un triangulo
Sean _s1_, _s2_ y _s3_ las longitudes de los tres lados de un triangulo, para verificar si esos tres lados realmente forman un triangulo debe de cumplirse la propiedad de que la suma de 2 de los lados sea mayor al otro lado, es asi por ejemplo que la suma:
`s1 + s2 > s3, s2 + s3 > s1 y s1 + s3 > s2`
si se cumplen estas 3 ecuaciones podemos decir que los 3 lados forman un triangulo.

Desarrollar un programa que lea la longitud de los lados de un triangulo y que muestre "ES TRIANGULO VALIDO" si se cumple la regla mencionada arriba o que muestre "NO ES TRIANGULO VALIDO" si no se cumple la regla.

Ralice el programa sin utilizar estructuras de control.

### E25・Pago con IGV

El dueno de un restaurante, ha decidido incluir un porcentaje del 5% por la atencion de los mozos como concepto de propina e incluir el impuesto del IGV de 18%, al realizar el calculo del monto a pagar por sus clientes.
El impuesto del IGV y el porcentaje por el concepto de las propinas se aplican sobre el monto consumido.

Con esta informacion, se solicita se realice un programa que permita calcular el monto a pagar por el cliente.

Ejemplo 1:
```
Consumo: 100
El monto a pagar es 123.00
```
Ejemplo 2:
```
Consumo 500
El monto a pagar es 615.00
```

### E26・Reciclaje de botellas
La municipalidad de Miraflores, ha decidigo incentivar el reciclaje de botella entre los vecinos de este distrito. Asi por cada botella que se entregue al municipio devolvera dinero.

Por cada botella de hasta un litro devolvera 1.25 sol y por cada botella cuya capacidad sea de mas de un litro devolvera 3.75 soles.

Realice un programa que permita calcular el monto a devolver al vecino por las botellas que entregue al municipio.
Imprima el resultado con dos decimales.

Ejemplo 1:
```
Numero de botellas de hasta un litro: 14
Numero de botellas de mas de un litro: 7

El monto a favor es de 43.75
```

Ejecucion 2:
```
Numero de botellas de hasta un litro: 12
Numero de botellas de mas de un litro: 29

El monto a favor es de 123.75
```

### E27・Leer un numero y sumar sus digitos
Realice un programa que permita leer un numero entero de 4 digitos y el programa imprima y se visualice la suma de los digitos tal y como se muestra en el ejemplo.

Trabaje bajo el supuesto, que el usuario siempre ingresara un numero entero de 4 digitos.

Ejecucion 1:
```
Numero: 6521
6 + 5 + 2 + 1 = 14
```

Ejecucion 2:
```
Numero: 8912
8 + 9 + 1 + 2 = 20
```

Ejecucion 3:
```
Numero: 5001
5 + 0 + 0 + 1 = 6
```

### E28・3 Numeros ordenados de forma ascendente
Realice un programa que permita leer 3 numeros enteros y el programa luego los imprima en orden ascendente.
Utilice las funciones: min() y max()

Ejecucion 1:
```
Numero 1: 33
Numero 2: 101
Numero 3: 12

12, 33, 101
```

Ejecucion 2:
```
Numero 1: 23
Numero 2: 101
Numero 3: 12

12, 23, 101
```

Ejecucion 3:
```
Numero 1: 12
Numero 2: 90
Numero 3: 12

12, 12, 90
```