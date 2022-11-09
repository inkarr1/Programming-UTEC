# Desarrollar un programa en Python que permita ingresar "N" DNIs a un diccionario
# (se termina de ingresar con un DNI = -1). Al terminar debe mostrar el DNI con el máximo
# valor. Validar que el DNI debe tener 8 dígitos, sino mostrar el mensaje DNI INCORRECTO.
# Recordar cada DNI ingresado debe ser único.

# Ingresar valor de 8 digitos
# almacenar en una lista
# terminar cuando sea -1
# imprimir el mas alto numero

dni = 0
i = 0
d = {}

while dni != -1:
    dni = input("DNI" + str(i + 1) + ": ")
    tam = len(dni)
    dni = int(dni)
    if dni == -1:
        break
    elif tam != 8:
        print("DNI incorrecto")
    else:
        if dni not in d.values():
            d[len(d)+1] = dni

    i+=1

print("El DNI con el valor maximo es", max(d.values()))



