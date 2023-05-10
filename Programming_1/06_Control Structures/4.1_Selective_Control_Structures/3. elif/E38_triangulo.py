from math import sqrt
lado1 = int(input("Lado 1: "))
lado2 = int(input("Lado 2: "))
lado3 = int(input("Lado 3: "))

cond1 = (lado1+lado2>lado3)
cond2 = (lado2+lado3>lado1)
cond3 = (lado1+lado3>lado2)

#estructura 1
if cond1 and cond2 and cond3:
    print("Es un triangulo")
else:
    print("No se puede formar un triangulo")

#estructura 2
if lado1+lado2<lado3:
    print("No se puede formar un triangulo")
elif lado1+lado3<lado2:
    print("No se puede formar un triangulo")
elif lado2+lado3<lado1:
    print("No se puede formar un triangulo")
else:
    print("Es un triangulo")

if lado1==lado2 and lado2==lado3 and lado1==lado3:
    print("Es un triangulo equilatero")
elif lado1 == lado2 or lado2 == lado3 or lado3==lado1:
    print("Es un triangulo isoceles")
else:
    print("Es un triangulo escaleno")

s = (lado1+lado2+lado3)/2
area = (s*(s-lado1)*(s-lado2)*(s-lado3))**(0.5)
#area = sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
#area = pow(s*(s-lado1)*(s-lado2)*(s-lado3),0.5)
print("El area es:", area)