n_dia_entrega = int(input("Ingrese los dias hasta la entrega del producto: "))
n_desaduanar = int(input("Ingrese los dias para desaduanar el producto: "))
n_fabricacion = int(input("Ingrese los dias de fabricacion: "))
n_instalacion_importado = int(input("Ingrese los dias de instalacion de producto importado: "))
n_instalacion_fabricado = int(input("Ingrese los dias de instalacion de producto fabricado: "))

def empresaTiempo(entrega, desaduanaje, fabricacion, instalacion_impo, instalacion_fabri):

    result_importado = entrega - (desaduanaje + instalacion_impo)
    result_fabricado = entrega - (fabricacion + instalacion_fabri)

    print("Proceso de importacion: ")
    print("Dias del proceso:", entrega)
    print("Dias antes de cumplir el plazo con producto importado: ", result_importado)
    print("Proceso de fabricacion: ")
    print("Dias del proceso:", fabricacion + instalacion_fabri)
    print("Dias antes de cumplir el plazo con producto fabricado: ", result_fabricado)

    return

result = empresaTiempo(n_dia_entrega, n_desaduanar, n_fabricacion, n_instalacion_importado, n_instalacion_fabricado)

print(result)