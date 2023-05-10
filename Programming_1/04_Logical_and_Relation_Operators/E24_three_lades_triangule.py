s1 = int(input("Ingrese el primer lado: "))
s2 = int(input("Ingrese el segundo lado: "))
s3 = int(input("Ingrese el tercer lado: "))

result = s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2

print(("NO " * (result == False)) + "ES TRIANGULO VALIDO")