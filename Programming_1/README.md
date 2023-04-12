# Programming 1
## 1・Basics
### Caracteres especiales
#### Backslash
````python
s = 'Asi\nfunciona\nel\nfin\nde\nlinea'
print(s)
s = "Esto\tes\tuna\ttabulacion"
````

## 2・Type Data
[Ejercicios](https://github.com/jhanpieremontes/Programming-UTEC/tree/master/Programming_1/1_Type_Data_and_Aritmetics_Operators)

## 3・Aritmetics Operators
- Si ambos operandos son enteros (int), el resultado es entero.
- Si al menso un operando es decimal (float, el resultado es decimal.
- Suma, resta, multiplicación,división real, división entera, módulo y potencia.

### Exercises
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


## 4・Estructuras de Control Selectiva
La estructura selectiva permite ejecutar instrucciones según un criterio o condición.

### Selectiva Simple - If
![img.png](../Assets/selectiva_simple.png)
### Selectiva Doble - If/Else
![img.png](../Assets/selectiva_doble.png)
### Selectiva Múltiple - If/Elif/Else
![img.png](../Assets/selectiva_multiple.png)
### Estructuras de Control Anidadas
Las estructuras de control selectivas pueden anidarse unas dentro de otras, cuando sea necesario tener más alternativas según la lógica del problema.
![img.png](../Assets/estructuras_de_control_anidadas.png)
## Repetitive Control Structures
### While
La sentencia while es una Estructura de Control Repetitiva.
Al igua que una sentencia condicional if, la sentencia while utiliza una expresión condicional.
El bloque de instrucciones de while se ejecutará mientras la expresión condicional se evalúe como verdadera (True).
![img.png](../Assets/while.png)
### Break
Hasta el momento hemos visto que todas las instrucciones del bucle while se ejecutan en cada iteración.
Python proporciona la palabra reservada break que termina un bucle por completo y salta a la siguiente instrucción que sigue al bucle.
![img.png](../Assets/while_break.png)
### Continue
Hasta el momento hemos visto que todas las instrucciones del bucle while se ejecutan en cada iteración.
Python proporciona la palabra reservada continue que indica al bucle saltar a la evaluación de la condición nuevamente y continuar con el bucle.
![img.png](../Assets/while_continue.png)