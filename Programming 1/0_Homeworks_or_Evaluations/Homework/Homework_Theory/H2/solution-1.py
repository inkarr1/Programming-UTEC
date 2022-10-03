# NO MODIFICAR NADA BAJO ESTA LINEA
def main():
# NO MODIFICAR NADA SOBRE ESTA LINEA
    #=======PROTEGE LA SAGRADA LINEA DEL TIEMPO=======
    N = int(input("N = "))

    # tu solucion empieza aqui

    viajes_lista = []
    points = []
    puntajes_lista = []

    for j in range(N):
        viajes = int(input("viajes = "))
        viajes_lista.append(viajes)

    if N == 0:
        print("La línea del tiempo está libre de los viajes de Loki y Sylvie.")
    elif N < 0:
        print("ERROR, no existe información acerca de los viajes de Loki y Sylvie.")

        for i in range(N):
            P = int(input("P = "))
            points.append(P)
        pointsum = sum(points)

        for x in range(N):
            puntajes_detalles = []
            n = int(input("Cuantos elementos son:"))
            for y in range(n):
                puntajes = input("puntajes = ")
                puntajes_detalles.append(puntajes)
            puntajes_lista.append(puntajes_detalles)
        
        if pointsum >= 0:
            print("Loki y Sylvie pueden seguir viajando, envíe mas soldados en su captura.")
        else:
            print(f"Los soldados de la AVT han logrado atrapar a Loki y Sylvie luego de {N} viajes en el año {last_viaje[-1]}.")

        if viajes_lista:
            print("PELIGRO, se ha viajado al mismo año 2 veces, envíe mas soldados en su captura.")
        elif 0 in points:
            print("ERROR, no pueden existir viajes sin puntos.")

#    elif P >= 0 in points:
#        print("ERROR, no pueden existir viajes sin puntos.")

#    print("viajes=", viajes_lista)
#    print("P=", points)
#    print("puntajes=", puntajes_lista)

    # tu solucion termina aca

# NO MODIFICAR NADA BAJO ESTA LINEA
if __name__ == "__main__":
    main()
# NO MODIFICAR NADA SOBRE ESTA LINEA