for i in range(100,-1,-10):
    F = (i*9/5) + 32
    print("La temperatura es",i,"C,",round(F),"F")



N = int(input("Ingrese el valor de N:"))
serie=0
for i in range(1,N+1):
    serie = serie + i**5
print(serie)

