# Diccionario
d = {'name': 'Zara', 'age': 7, 'class': 'First'}
c = {'name': 'Zara', 'age': 7, 'class': 'First'}
print(d)
d['age'] = 8
print(d)

# Borrar
del d['name']
print(d)

# Borrar totalmente del diccionario
del c
print(c)

# Borrar parcialmente
d.clear()
print(d)

