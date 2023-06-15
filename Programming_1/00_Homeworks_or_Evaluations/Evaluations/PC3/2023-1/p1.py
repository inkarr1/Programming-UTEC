texto1 = input("texto 1: ")
texto2 = input("texto 2: ")

lista1 = texto1.split()
lista2 = texto2.split()

lista_resultante1 = [palabra for palabra in lista1 if palabra not in lista2]
lista_resultante2 = [palabra for palabra in lista2 if palabra not in lista1]

resultado1 = ' '.join(lista_resultante1)
resultado2 = ' '.join(lista_resultante2)


print("Resultado de string 1:")
print(resultado1)
print("Resultado de string 2:")
print(resultado2)

