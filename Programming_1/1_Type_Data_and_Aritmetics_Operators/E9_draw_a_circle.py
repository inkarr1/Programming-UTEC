from turtle import *

radio = 100
goto(-radio, 0)
#Para hacer mas circulos cambiando el tamano del radio.
for radio in range(300,400,10):
    for x in range(-radio, radio):
        y = (radio ** 2 - x ** 2) ** (1 / 2)
        goto(x, y)
    for x in range(radio, -radio, -1):
        y = -(radio ** 2 - x ** 2) ** (1 / 2)
        goto(x, y)
input()
