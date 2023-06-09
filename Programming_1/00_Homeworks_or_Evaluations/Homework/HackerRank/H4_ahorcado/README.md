# Exercises

## E4 
En el juego ”El ahorcado”, el jugador tiene que adivinar una palabra, adivinando las letras que la componen. Si el jugador adivina la palabra está salvado, si no, está ahorcado. Para implementar el juego debes cubrir las siguientes funcionalidades:

1. Permitir ingresar una palabra a adivinar. (Ej. barranco)
2. Permitir ingresar intentos de las letras hasta el tamaño de la palabra más uno, es decir para la palabra barranco (8 letras) son 9 intentos.
3. Crear una función llamada 'avanceJuego' para mostrar las letras adivinadas luego de ingresar el intento del usuario.
4. Imprimir el resultado ”¡Te salvaste!” si gano, o ”¡Estas ahorcado!” si perdio.

Input Format
```
barranco
a
r
c
m
n
o
b
```

Constraints
Debes utilizar strings y funciones

Output Format
```
Inicia el juego :)
La palabra tiene 8 letras
--------
Tienes 9 intentos
Intento 1 :
-a--a---
Intento 2:
-arra---
Intento 3:
-arra-c-
Intento 4:
-arra-c-
Intento 5:
-arranc-
Intento 6:
-arranco
Intento 7:
barranco
Te salvaste:
```

Sample Input 0
````
barranco
a
r
c
m
n
o
b
````

Sample Output 0
````
Inicia el juego:)
La palabra tiene 8 letras:
--------
Tienes 9 intentos
Intento 1 :
-a--a---
Intento 2 :
-arra---
Intento 3 :
-arra-c-
Intento 4 :
-arra-c-
Intento 5 :
-arranc-
Intento 6 :
-arranco
Intento 7 :
barranco
Te salvaste!
````

Sample Input 1
````
utec
a
i
c
e
u
````

Sample Output 1
````
Inicia el juego:)
La palabra tiene 4 letras:
----
Tienes 5 intentos
Intento 1 :
----
Intento 2 :
----
Intento 3 :
---c
Intento 4 :
--ec
Intento 5 :
u-ec
Estas ahorcado!
````
