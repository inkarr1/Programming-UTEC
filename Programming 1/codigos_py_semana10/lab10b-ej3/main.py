texto = input("Input: ")
texto = texto.lower()
lista = [x for x in texto.split(' ')]
print(lista)

d={}
for palabra in lista:
    if palabra in d.keys():
        d[palabra] = d[palabra] + 1
    else:
        d[palabra] = 1

print(d)