# Matriz: Lista de Lista
C = [ [2 , 3, 4],
      [40, 50, 60],
      [100, 200, 300] ]
total = sum([x for row in C for x in row])
print(total)