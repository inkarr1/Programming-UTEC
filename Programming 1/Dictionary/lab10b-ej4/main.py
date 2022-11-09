cadena = input("Input: ")

d={}
d[cadena[0]] = 0;
d[cadena[- 1]] = 0;
print(len(cadena))
for base in cadena:
    if base in d.keys():
        d[base] = d[base] + 1

print(d)