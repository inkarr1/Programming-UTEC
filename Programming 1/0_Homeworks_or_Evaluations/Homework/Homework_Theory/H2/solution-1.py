# NO MODIFICAR NADA BAJO ESTA LINEA
def main():
# NO MODIFICAR NADA SOBRE ESTA LINEA
    #=======PROTEGE LA SAGRADA LINEA DEL TIEMPO=======
    N = int(input("N = "))
    viajes = input("viajes = ")
    P = input("P = ")
    puntajes = input("puntajes = ")

    # tu solucion empieza aqui

    lista_exterior = []

    for i in range(N):
        lista_interior = []
        for j in range(2):
            lista_interior.append(int(input()))
        lista_exterior.append(lista_interior)
    print(lista_exterior)

#    while N>0:
#        if N == 0:
#            print("La línea del tiempo está libre de los viajes de Loki y Sylvie.")
#        elif N < 0:
#            print("ERROR, no existe información acerca de los viajes de Loki y Sylvie.")
#        elif P <= 0:
#            print("ERROR, no pueden existir viajes sin puntos.")
#        print("hola")
#    print("")

    # tu solucion termina aca

# NO MODIFICAR NADA BAJO ESTA LINEA
if __name__ == "__main__":
    main()
# NO MODIFICAR NADA SOBRE ESTA LINEA