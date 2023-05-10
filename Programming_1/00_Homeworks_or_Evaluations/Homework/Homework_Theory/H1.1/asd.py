N = int(input('N: '))
M = int(input('N: '))

#result = ((N % M == 1) * "no ") + "es multiplo de " + str(M)
print('es multiplo de {M}' if N % M == 0 else f'no es multiplo de {M}')

