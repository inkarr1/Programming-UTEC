cadena=""
while len(cadena)==0 or len(cadena) % 3!=0:
    cadena = input("Ingrese su cadena de ARN :")

cantT = 0
cantS = 0
for i in range(0,len(cadena),3):
    print("El codon 1 es", cadena[i:i + 3])
    if cadena[i:i + 3]=="AUC":
        cantT+=1
    elif cadena[i:i + 3] == "UCA":
        cantS+=1

print(cantT)
print(cantS)