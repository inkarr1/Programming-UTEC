name = input("Ingrese la palabra: ")

def avanceJuego(palabra):
    print("Inicia el juego:)")
    print("La palabra tiene", len(palabra), "letras:")
    print('-' * len(palabra))
    i = 0
    intentos = len(palabra) + 1
    while i < intentos:
        for i in palabra:
            print(i)
    puzzle = palabra
    return puzzle

result = avanceJuego(name)

print(result)