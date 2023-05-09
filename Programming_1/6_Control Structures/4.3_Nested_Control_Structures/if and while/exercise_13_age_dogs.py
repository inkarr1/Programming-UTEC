# Una veterinaria le ha solicitado crear un programa para calcular la edad aproximada
# humana de sus pacientes caninos. El programa que usted realizará solicita un número
# N que indica cuántos pacientes se atenderán. A continuación solicita la edad caninca
# y el nombre de cada paciente. Por cada lectura, usted imprime el nombre y la edad real
# aproxiamada humana:

# Considere que la edad real aproximada se calcula con los siguientes criterios:
# - Los 2 primeros años se consideran como 10.5 años humanos cada uno.
# - Cada año adicional se considera como 4 años humanos
# - Solo se considera edades en números enteros mayor o igual a 1. Se solicita que este
# dato sea validado por su programa. Es decir si no ingresa un valor mayor o igual a 1,
# debe volver a solicitar el dato.
# - El texto de salida debe combinar el nombre y la edad equivalente, tal como se verá en
# los ejemplos de entrada y salida del programa, que se muestran en la diapositiva siguiente.

num = int(input("Numero de perritos: "))
i = 0

while i < num:
    nombre = input("Nombre del perro: ")
    edad = 0

    while edad < 1:
        edad = int(input("Edad canina: "))

    edadCann = 0

    if edad <= 2:
        edadCann = 10.5 * edad
    else:
        edadCann = (10.5) * 2 + 4 * (edad - 2)

    print("La edad de", nombre, "es", edadCann)
    i = i + 1