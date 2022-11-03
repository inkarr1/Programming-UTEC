nombres = [input(f"Ingrese nombre:") for i in range(int(input("numero de nombres: ")))]
nombres_con_s = [ nombre for nombre in nombres if nombre.endswith('s') and len(nombre)>4]
print(nombres_con_s)