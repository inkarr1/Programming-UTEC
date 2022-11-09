# Diseñe e implemente un algoritmo que imprima los números pares del 8 al 0 si se detecta el número 4, que acabe el bucle
# y muestre el mensaje "while terminado".

i = 10

while i >= 0:
    i = i - 2

    if i == 4:
        break
    print(i)
print("While terminado")