codigos = {
    'A1T': 'Alonso Tinoco',
    'P1C': 'Pierina Carbajal',
    'R1G': 'Rosa Guardia',
    'P2C': 'Pablo Cusi'
}

nombre = input("Ingresar nombre: ")
apellido = input("Ingresar apellido: ")

# Generar el código utilizando la primera letra del nombre, la primera letra del apellido y un número consecutivo
numero = str(len(codigos) + 1)
codigo = nombre[0].upper() + numero + apellido[0].upper()

# Agregar el nuevo código al diccionario
codigos[codigo] = nombre + " " + apellido

print("Resultado:")
print(codigos)
