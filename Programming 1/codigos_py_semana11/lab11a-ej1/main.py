import json

n = int(input("Ingrese la cantidad de cursos: "))
dictCurso = {}
dictDocente  = {}
for i in range(n):
    print("------- Datos del curso " + str(i+1) +" -------")
    nombre = input("Ingrese el nombre: ")
    carrera = input("Ingrese la carrera: ")
    ciclo = input("Ingrese el ciclo: ")
    creditos = int(input("Ingrese la cantidad de creditos: "))
    print("------- Datos del docente -------")
    nombreDoc = input("Ingrese el nombre: ")
    correo = input("Ingrese el correo: ")
    horario = input("Ingrese el horario: ")

    dictDocente = {"nombre": nombreDoc, "correo":correo, "horario":horario}
    dictCurso[i+1] = {"nombre": nombre, "carrera":carrera,"ciclo":ciclo,
                      "creditos":creditos}#, "docente":dictDocente}
    dictCurso[i+1]["docente"] = dictDocente

print(dictCurso)

with open('data.json','w') as outfile:
    json.dump(dictCurso,outfile)
