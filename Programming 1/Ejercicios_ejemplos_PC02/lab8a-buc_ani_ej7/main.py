robots = 0
while robots<1 or robots>10:
    robots = int(input("Ingrese el total de robots :"))

tipo1=0
tipo2=0
tipo3=0
for i in range(1,robots+1):
    tipo = 0
    while tipo < 1 or tipo > 3:
        tipo = int(input("Ingrese el tipo de robot " + str(i) + ":"))

    if tipo==1: tipo1+=1
    elif tipo == 2: tipo2 += 1
    elif tipo == 3: tipo3 += 1

print("Kit A:", tipo1 + tipo2)
print("Kit B:", tipo2 + tipo3)
print("Kit C:", tipo1 + tipo3)