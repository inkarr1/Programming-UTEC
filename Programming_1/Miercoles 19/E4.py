# Se puede crear variables de los rangos

start = 2
end = 28
step = 2
mult = 3

C = [x for x in range(start, end, step) if x % mult == 0]

print(C)