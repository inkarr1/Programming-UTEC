# Sean s1, s2, s3 las langitudes de los tres lados de un triangulo, para verificar si esos tres
# lados realmente forman un triangulo debe de cumplirse la propiedad de que la suma de 2 de los
# lados  sea mayor al otro lado, es asi por ejemplo que la suma

# s1 + s2 > s3, s2 + s3 > s1, s1 + s3 > s2,

# Si se cumplen estas 3 ecuciones podemos decir que los 3 lados forman un triangulo.

# Desarrollar un programa que lea la longitud de los lados de un triangulo y que muestre
# "ES TRIANGULO VALIDO" si se cumple la regla mencionada arriba o que muestre "NO ES TRIANGULO VALIDO"
# si no se cumple la regla.

s1 = int(input("Ingrese el primer lado: "))
s2 = int(input("Ingrese el segundo lado: "))
s3 = int(input("Ingrese el tercer lado: "))

result = s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2

print(("NO " * (result == False)) + "ES TRIANGULO VALIDO")