print("Ingrese el producto a consultar:"
                               "\n1. Aceite"
                               "\n2. Refrigerante"
                               "\n3. Filtro"
                               "\n4. Espejos"
                               "\n5. Bujia"
                               "\n6. Amortiguador\n")
producto_consulta = int(input("Ingrese opcion (1-6): "))

if producto_consulta == 1:
    recomendacion = "Filtro y Amortiguador"
    promocion = "Descuento del 5%"
elif producto_consulta == 2:
    recomendacion = "Aceite, Filtro y Bujia"
    promocion = "Descuento del 5%"
elif producto_consulta == 3:
    recomendacion = "Aceite"
    promocion = "Descuento del 15%"
elif producto_consulta == 4:
    recomendacion = "Refrigerante y Filtro"
    promocion = "Descuento del 15%"
elif producto_consulta == 5:
    recomendacion = "Refrigerante y Espejos"
    promocion = "Descuento del 10%"
elif producto_consulta == 6:
    recomendacion = "Aceite y Filtro"
    promocion = "Descuento del 10%"

print("\nRecomendaciones:\n", recomendacion, "\n",
      "\nPromocion:\n", promocion)
