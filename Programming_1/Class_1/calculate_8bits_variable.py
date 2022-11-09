# Si cada variable necesita 8bits de espacio de memoria

variable = int(input("Ingresar la cantidad de Bytes a calcular: "))

bit = 1 / 8

if variable == 1000:
    bytes = 1024
    result = bit * bytes
elif variable == 1000000:
    bytes = 1024000
    result = bit * bytes
else:
    result = bit * variable

print(f"La cantidad de Bytes en Bits es: {result}")
