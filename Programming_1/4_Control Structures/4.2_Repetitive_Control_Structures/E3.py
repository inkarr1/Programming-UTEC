num_input = 0

while num_input <= 0:
    num_input = int(input("Valor de N: "))

i = 0
fact = 1
while i < num_input:
    i += 1
    fact = fact * i

print("El factorial es: ", fact)