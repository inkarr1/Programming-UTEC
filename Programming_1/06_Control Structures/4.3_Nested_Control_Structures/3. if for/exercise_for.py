tam = int(input("Ingrese: "))
for i in range(tam):
    for j in range(tam):
        if i < tam -j - 1:
            print(" ", end="")
        else:
            print("#", end="")
    print("")