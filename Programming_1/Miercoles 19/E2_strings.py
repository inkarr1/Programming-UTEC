strings = ["Domingo", "Lunes", "Martes"]

r3 = []

for e in strings:
    e = e.upper()
    r3.append(e)
print(r3)

r4 =[e.upper() for e in strings]
print(r4)
