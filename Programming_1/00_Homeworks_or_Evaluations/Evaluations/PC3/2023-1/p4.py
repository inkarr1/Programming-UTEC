medicamentos = {
    'LS01': 'Levotiroxina sódica',
    'MC01': 'Metformina clorhidrato',
    'AI01': 'Aspirina infantil',
    'CG01': 'Clonazepam gotas'
}

medicamento = input("Ingresar medicamento: ")

palabras = medicamento.split()
codigo = ''.join(palabra[0] for palabra in palabras).upper()
numero = str(len(medicamentos) + 1)

if len(numero) < 2:
    numero = '0' + numero

codigo_medicamento = codigo + numero

for medicamento in medicamentos.keys():
    if medicamento == codigo_medicamento:
        numero += 1
        codigo_medicamento = codigo + numero
    print(medicamento)

medicamentos[codigo_medicamento] = medicamento

print(medicamentos)

