def evaluar_expresion(expresion):
    divisiones = expresion.split('+')
    for division in divisiones:
        numerador, denominador = division.split('/')
        if denominador == '0':
            return False
    return True


def calcular_expresion(expresion):
    if not evaluar_expresion(expresion):
        return "La expresión es incorrecta. No se puede dividir entre cero."

    divisiones = expresion.split('+')
    resultado = 0
    for division in divisiones:
        numerador, denominador = division.split('/')
        resultado += int(numerador) / int(denominador)

    return resultado



expresion = input("Ingrese expresión: ")
es_correcta = evaluar_expresion(expresion)

if es_correcta:
    resultado = calcular_expresion(expresion)
    print("La expresión es correcta.")
    print("El resultado es:", "{:.3f}".format(resultado))
else:
    print("La expresión es incorrecta. No se puede dividir entre cero.")
