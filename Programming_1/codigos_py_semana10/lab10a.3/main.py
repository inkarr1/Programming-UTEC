
# llamada usando for
n = int(input("Cantidad #1: "))
lista1 = []
for i in range(n):
  value = int(input(f"Ingrese {i+1}:"))
  lista1.append(value)

# llamada concisa usando comprehension
n = int(input("Cantidad #2: "))
lista2 = [int(input(f"Ingrese {i+1}:")) for i in range(n)]

# llamada mas concisa
lista3 = [int(input(f"Ingrese {i+1}:")) for i in range(int(input("Cantidad #3: ")))]

# mostrando listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3:", lista3)
