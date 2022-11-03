"""
d = {1:'Geeks', 2:'for', 3:'geeks'}
print(d)
d = {'name':'Geeks', 1:[1,2,3,4]}
print(d)

d = dict({1:'Geeks', 2:'for'})
print(d)
l=[(1,'Geeks'), (2,'for')]
d = dict([(1,'Geeks'), (2,'for')])
print(d)
print(type(l))
print(type(d))

d={'name':'Zara', 'edad':7, 'clase':'First'}
print("d['name']: ", d['name'])
print("d['edad']: ", d['edad'])
print(d["clase"])
#print("d['Alice']: ", d['Alice'])

d={'name':'Zara', 'edad':7, 'clase':'First'}
print("Claves: %s" % d.keys())
print("Valores: %s" % d.values())


d={'name':'Zara', 'edad':7, 'clase':'First'}
d['edad'] = 8
d['colegio'] = 'DPS colegio'
d['clase'] = 'Second'
print("d['edad']: ", d['edad'])
print("d['colegio']: ", d['colegio'])
print(d['clase'])
print(d)
"""

d={'nombre':'Zara', 'edad':7, 'clase':'First'}
#del d['nombre']
#d.clear()
del d
#print(d)
print("d['edad']: ", d['edad'])
print("d['nombre']: ", d['nombre'])
