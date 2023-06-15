codigos = {
    'A1T': 'Alonso Tinoco',
    'P1C': 'Pierina Carbajal',
    'R1G': 'Rosa Guardia',
    'P2C': 'Pablo Cusi'
}

nombre = input("Ingrese nombre: ")
apellido = input("Ingrese apellido: ")

# Generar el código utilizando la primera letra del nombre y apellido
num = 1
codigo = nombre[0].upper() + str(num) + apellido[0].upper()

# Buscar un número que no se repita en el diccionario
while codigo in codigos:
    num += 1

# Generar el nuevo código único
codigo += str(num)

# Agregar el nuevo código y nombre al diccionario
codigos[codigo] = nombre + ' ' + apellido

# Mostrar el resultado
print(codigos)
