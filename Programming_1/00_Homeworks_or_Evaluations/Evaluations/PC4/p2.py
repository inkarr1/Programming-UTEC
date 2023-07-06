def generar_codigo(nuevo_nombre_medicamento, lista_medicamentos):
    palabras = nuevo_nombre_medicamento.split()
    codigo = ''.join(palabra[0].upper() for palabra in palabras)
    numero = 1
    while any(medicamento['codigo'] == f'{codigo}{numero:02d}' for medicamento in lista_medicamentos):
        numero += 1

    return f'{codigo}{numero:02d}'


def actualizar_medicamentos(lista_medicamentos):
    with open('./medicamentos.txt', "r+") as archivo:
        for medicamento in lista_medicamentos:
            archivo.write(f"{medicamento['codigo']}, {medicamento['nombre']}\n")


lista_medicamentos = []
with open('./medicamentos.txt', "r") as archivo:
    for linea in archivo:
        codigo, nombre = linea.strip().split(',')
        lista_medicamentos.append({'codigo': codigo.strip(), 'nombre': nombre.strip()})

nuevo_nombre_medicamento = input("Ingresar medicamento: ")
nuevo_codigo = generar_codigo(nuevo_nombre_medicamento, lista_medicamentos)
lista_medicamentos.append({'codigo': nuevo_codigo, 'nombre': nuevo_nombre_medicamento})
actualizar_medicamentos(lista_medicamentos)

