"""

numeros = [1,2,3,4,5,6,7,8]

r1 = []
for e in numeros:
  e = e*2
  r1.append(e)
#print(r1)

r2 = [e*2 for e in numeros]
print(r2)
"""

"""

strings = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

r3 = []
for e in strings:
  e = e.upper()
  r3.append(e)
#print(r3)

r4 = [e.upper() for e in strings]
print(r4)


"""
"""
A = [x for x in range(2,25,2)]
B = [x for x in range(3,28,3)]
#C = [x for x in range(6,28,6)]
C = [x for x in range(2,28,2) if x%3==0]
print(A)
print(B)
print(C)
"""


start =4
end=80
step=4
mult=12
C = [x for x in range(start,end,step) if x%mult==0]
print(C)

