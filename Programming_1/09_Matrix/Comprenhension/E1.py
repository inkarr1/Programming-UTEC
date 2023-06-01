# Matriz: Lista de Lista
C = [[2, 3, 4],
     [40, 50, 60],
     [100, 200, 300]]

# SIN COMPREHENSION
'''
# suma por filas
sum_row1 = [sum(x for x in C)]
print(sum_row1)

# equivalente usando for
sum_row2 = []
for row in C:
    subtotal = sum(row)
sum_row2.append(subtotal)
'''


total = sum([x for row in C for x in row])
print(total)
