num = int(input("Ingrese la cantidad: "))
en_binario = ""

while num >= 1:
    cociente = num // 2
    residuo = num % 2
    en_binario = str(residuo) + en_binario
    num = cociente
print(en_binario)