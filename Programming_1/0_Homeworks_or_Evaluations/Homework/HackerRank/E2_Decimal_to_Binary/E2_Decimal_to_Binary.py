num_decimal = int(input(""))
num_binary = ""
index = 0

while num_decimal > 0:
    if num_decimal % 2 == 0:
        num_binary = "0" + num_binary
    else:
        num_binary = "1" + num_binary
    num_decimal //= 2
    index = index + 1

print("El numero en binario es:", num_binary)
print("La cantidad de digitos son:", index)
