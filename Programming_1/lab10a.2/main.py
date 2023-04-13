
# Matriz: Lista de Lista
C = [ [2, 3, 4],
      [40, 50, 60],
      [100, 200, 300] ]
"""
# suma por filas
sum_row1 = [sum(x) for x in C]
print(sum_row1)
# equivalente usando for
sum_row2 = []
for row in C:
    subtotal = sum(row)
    sum_row2.append(subtotal)
print(sum_row2)

"""

# suma total
total1 = sum([x for row in C for x in row])
print(total1)
# equivalente usando for
total2 = 0
for row in C:
    for x in row:
        total2 += x
print(total2)
"""
total1 = sum([row[x] for row in C for x in range(len(row)) if x==1])
print(total1)
"""