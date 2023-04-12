alumnos = {
    "Alejandro": ["ceviche", "lomo saltado", "pollo a la brasa"],
    "Roberto": ["lomo saltado"],
    "Jesús": ["lomo saltado", "lasagna"],
    "Carlos": ["lasagna"],
    "Melina": ["ceviche", "arroz con pollo"]
}
platos = {}
for alumno in alumnos.keys():
    #print(alumno)
    for plato in alumnos[alumno]:
        if plato in platos.keys():
            platos[plato].append(alumno)
        else:
            platos[plato] = [alumno]
print(platos)
print("Pueden comer juntos:")
for alumnos in platos.values():
    #print(plato)
    if len(alumnos) > 1:
        for i in range(len(alumnos)):
            print(alumnos[i],end=", ");
        print("")
print(platos.values())
print(platos.keys())
#print(key + ":",d[key],end=", ");