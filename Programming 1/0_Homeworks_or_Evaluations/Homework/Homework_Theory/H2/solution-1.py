# NO MODIFICAR NADA BAJO ESTA LINEA
def main():
# NO MODIFICAR NADA SOBRE ESTA LINEA
    #=======PROTEGE LA SAGRADA LINEA DEL TIEMPO=======
    N = int(input("N = "))
    viajes = input("viajes = ")
    p = int(input("P = "))
    puntajes = int(input("Puntaje= "))

    # tu solucion empieza aqui

    def viajes_del_tiempo(numero_viajes,anos_viajes,longitud_p,puntaje_viaje):

    year_viajes_lista = []
    p_lista = []
    puntajes_lista = []
    if N == 0:
        print("La línea del tiempo está libre de los viajes de Loki y Sylvie.")
    elif N < 0:
        print("ERROR, no existe información acerca de los viajes de Loki y Sylvie.")
    else:
        #ano_viaje
        for x in range(N):
            viajes = int(input("viajes = "))
            year_viajes_lista.append(viajes)
        #P
        for y in range(N):
            P = int(input("P = "))
            if P <= 0:
                print("Loki y Sylvie pueden seguir viajando, envíe mas soldados en su captura.")
                exit()
            p_lista.append(P)
        #puntajes
        for y in range(N):
            sub_lista = []
            n = int(input("cuantos en la sublista= "))
            for z in range(n):
                sub_lista.append(int(input("puntaje= ")))
            puntajes_lista.append(sub_lista)
        print(year_viajes_lista)
        print(p_lista)
    #def viajes_del_tiempo(numero_viajes, anos_viajes):
        #list = []
        #for i in range(numero_viajes):
            #ga = anos_viajes
            #list.append(ga)
            #for j in range(numero_viajes):
                #points.append(longitud_p)
            #pointsum = sum(points)

            #for x in range(N):
                #puntajes_detalles = []
                #n = int(input("Cuantos elementos son:"))
                #for y in range(n):
                    #puntajes = input("puntajes = ")
                    #puntajes_detalles.append(puntajes)
                #puntajes_lista.append(puntajes_detalles)
     #   return viajes_del_tiempo
    #contenedor_viajes = viajes_del_tiempo(N,viajes)
    #contenedor_viajes = viajes_del_tiempo(N,viajes,p,puntajes)
   #print(contenedor_viajes)

#    if N == 0:
#        print("La línea del tiempo está libre de los viajes de Loki y Sylvie.")
#    elif N < 0:
#        print("ERROR, no existe información acerca de los viajes de Loki y Sylvie.")
#
#        if pointsum >= 0:
#            print("Loki y Sylvie pueden seguir viajando, envíe mas soldados en su captura.")
#        else:
#            print(f"Los soldados de la AVT han logrado atrapar a Loki y Sylvie luego de {N} viajes en el año {last_viaje[-1]}.")
#
#        if viajes_lista:
#            print("PELIGRO, se ha viajado al mismo año 2 veces, envíe mas soldados en su captura.")
#        elif 0 in points:
#            print("ERROR, no pueden existir viajes sin puntos.")

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