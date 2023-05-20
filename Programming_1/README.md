# Programming 1
## 1・Basics
### Caracteres especiales
#### Backslash
````python
s = 'Asi\nfunciona\nel\nfin\nde\nlinea'
print(s)
s = "Esto\tes\tuna\ttabulacion"
````

### Identacion
En Python, la identacion (sangria, espacios en blanco al inicio de la linea) tiene un significado semantico. Por ello, es importante que, por ahora, todas las lineas que escribas empiecen desde la primera posicion, es decir, que no esten identadas.

## 2・Type Data
- Numeros enteros (int)
- Numeros de punto flotante (float)
- Numeros complejos (complex)
- Valores booleanos (bool)
- Cadenas de caracteres (str)

### int
- Es de precision ilimitada
- Decimal, binario, octal, hexadecimal
```python
n = 45
print(n)
n = 0b10
print(n)
n = 0o10
print(n)
n = 0x10
print(n)
```

### float
- Numeros literales, notacion cientifica, constructor float.
- Decimal, binario, octal, hexadecimal
```python
n = 3.1415
print(n)
n = 15e4
print(n)
n = 1.616e-35
print(n)
n = float(7)
print(n)
n = float("3.1415")
print(n)
```

### bool
- Representacion logica
- Muy importante para las estructuras de control condicional y repetitiva.
```python
b = true
print(b)
b = false
print(b)
b = bool(0)
print(b)
b = bool(4)
print(b)
b = bool(1.234)
print(b)
b = bool("")
print(b)
b = bool("test")
```

### str
- Es inmutable (no puede ser modificado una vez que ha sido creado).
- Secuencia de caracteres

```python
s = "Estas 'comillas simples' dentro de comillas dobles"
print(s)
s = 'Estas "comillas dobles" dentro de comillas simples'
print(s)
s = """Tambien se puede usar triple "comilla doble" """
print(s)
```

### Ejercicios
[Ejercicios](https://github.com/jhanpieremontes/Programming-UTEC/tree/master/Programming_1/1_Type_Data_and_Aritmetics_Operators)

## 3・Aritmetics Operators
- Si ambos operandos son enteros (int), el resultado es entero.
- Si al menso un operando es decimal (float, el resultado es decimal.
- Suma, resta, multiplicación,división real, división entera, módulo y potencia.

```python
print("1: ", 5 + 2) #1: 7
print("2: ", 5 + 7.5) #2: 12.5
print("3: ", 5 - 2) #3: 3
print("4: ", 5.0 - 2) #4: 3.0
print("5: ", 5.2 * 10) #5: 52.0
print("6: ", 5 * 2) #6: 10
print("7: ", 5 / 2) #7: 2.5
print("8: ", 5.0 / 2) #8: 2.5
print("9: ", 5 // 2) #9: 2
print("10: ", 5 % 2) #10: 1
print("11: ", 5.0 % 2) #11: 1.0
print("12: ", 2 ** 5) #12: 
print("13: ",2.0 ** 5) #13:
```

### Operaciones con Cadena
- Unir dos cadenas (concatenar)
- Obtener un elemento de la cadena ([])
```python
a = "UTEC"
b = "Life"
c = "Hackers"
logo = a + " " + b + c
print(logo)
print(logo[0])
print(logo[1])
```

### Precendencia de Operadores
| Prioridad | Operador     |
|-----------|--------------|
| 1         | Potencia: ** |
| 2         | Multiplicacion, division, division entera, modulo: *, /, //, % |
| 3 | Suma, resta: +, - |

```python
print(3 * 5 + 1)
print(3 * (5 + 1))
```

### Exercises

## 4・Operadores logicos y de relacion
### 4.1・Operadores logicos - Conectores logicos
Los conectores logicos son:
- `and` Es True si ambos son True
- `or` Es True si al menos uno es True
- `not` Convierte el True en False y viceversa

### 4.2・Operadores de relacion
- `>` mayor
- `>=` mayor o igual
- `<` menor
- `<=` menor o igual
- `!=` diferente
- `==` iguales

### 4.3・Algunas caracteristicas de los operadores logicos
- Los operadores de relacion tienen mayor precedencia que los operadores logicos. Es decir, se resuelven primero.
- Operaciones con la misma precedencia se evaluan de isquierda a derecha.
- Los parentesis permiten modificar las precendencias
- Tienen menor precedencia que los operadores matematicos.

## 5・Booleans Operators
### 5.1・Variables Booleanas
Es una variable binaria, que tiene dos valores posibles llamadas True y False.
Una variable booleana podemos almacenar solo dos posibles valores.

Algoritmo: Si estudio

Programa:
```python
estudio = True
```

Algoritmo: No esta soleado.

Programa:
```python
esta_soleado = False
```

### 5.2・Expresiones Booleanas
Es una expresión utilizada en lenguajes de programación que produce un valor booleano cuando se evalúa

#### Operadores Booleanos
| Operador | Nombre | Ejemplo |
| --- | --- |---------|
| `<` | Menor| 4 < 5   |
| `<=` | Menor o igual | 4 <= 5  |
| `>` | Mayor | 4 > 5   |
| `>=` | Mayor o igual | 4 >= 5  |
| `==` | Igual | 4 == 5 |
| `!=` | Distinto | 4 != 5  |
| `not` | Negacion | not True |

### 5.3・Combinando Expresiones Booleanas
#### Operador `and`
| A | B | A and B |
| --- | --- |---------|
| True | True | True    |
| True | False | False   |
|False | True | False   |
| False | False | False |

#### Operator `or`
| v1 | v2 | v1 `or` v2 |
| --- | --- | --- |
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False|


## 6・Estructuras de Control 

### 6.1・Estructuras de Control Selectiva
La estructura selectiva permite ejecutar instrucciones según un criterio o condición.

#### Selectiva Simple - If
![img.png](../Assets/selectiva_simple.png)
#### Selectiva Doble - If/Else
![img.png](../Assets/selectiva_doble.png)
#### Selectiva Múltiple - If/Elif/Else
![img.png](../Assets/selectiva_multiple.png)
#### Estructuras de Control Anidadas
Las estructuras de control selectivas pueden anidarse unas dentro de otras, cuando sea necesario tener más alternativas según la lógica del problema.
![img.png](../Assets/estructuras_de_control_anidadas.png)
### 6.2・Repetitive Control Structures
Son intrucciones que permiten que el flujo de ejecucion repita una parte del programa de acuerdo a una condicion.
#### While
La sentencia while es una Estructura de Control Repetitiva.
Al igua que una sentencia condicional if, la sentencia while utiliza una expresión condicional.
El bloque de instrucciones de while se ejecutará mientras la expresión condicional se evalúe como verdadera (True).
![img.png](../Assets/while.png)
#### Break
Hasta el momento hemos visto que todas las instrucciones del bucle while se ejecutan en cada iteración.
Python proporciona la palabra reservada break que termina un bucle por completo y salta a la siguiente instrucción que sigue al bucle.
![img.png](../Assets/while_break.png)
#### Continue
Hasta el momento hemos visto que todas las instrucciones del bucle while se ejecutan en cada iteración.
Python proporciona la palabra reservada continue que indica al bucle saltar a la evaluación de la condición nuevamente y continuar con el bucle.
![img.png](../Assets/while_continue.png)


## Strings - Cadenas de caracteres
___
Una cadena (string) es un tipo de dato en Python (str) que consiste en una secuencia ordenada de caracteres.
Una cadena contiene caracteres que pueden ser: letras, números, signos de puntuación, espacios en blanco, caracteres especiales, etc.


¿Cómo se representa?
En Python las cadenas se pueden delimitar utilizando comillas simple, comilla doble o triple comilla.

````python
mensaje = 'Esto es un string'
print(mensaje)
mensaje = "Mi nombre es Carlos D'Alessio"
print(mensaje)
mensaje = """Lorem ipsum dolor ait amer,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(mensaje)
````

### Operaciones con Strings
#### 1. Concatenación (+)
Dado 2 strings podemos concatenarlos para formar un solo string. El resultado será un nuevo string que contiene todos los caracteres del primer string seguidos de todos los caracteres del segundo string.

````python
first_string = "hola"
second_string = "amigo"
result = first_string + " " + second_string
print(result)
````

#### 2. Repetición (*)
Podemos producir un string que es el resultado de repetir un mismo string varias veces.

### Uso de índices
Posiciones dentro de un string.

````python
s = "Monty Python"
print(s[2])
print(s[:6] + s[6:10] + s[10:12])
print(s[:3] + s[6:8])
print(s[3:5] + "Ba" + s[8:])
````

### Inmutables
Los strings en Python son inmutables. No pueden ser cambiados. No es válida una signación.
