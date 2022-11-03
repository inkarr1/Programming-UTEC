palabra = input("Input: ")
d= {}
for letra in palabra:
    if letra in d.keys():
        d[letra] = d[letra] + 1
    else:
        d[letra] = 1

print(d)
for key in d.keys():
    print(key + ":",d[key],end=", ");