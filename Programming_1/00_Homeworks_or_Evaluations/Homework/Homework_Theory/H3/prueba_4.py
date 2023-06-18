import numpy as np
import imageio


def leer_imagen(ruta):
    np_array = np.array(imageio.v3.imread(ruta), dtype='int')
    lista_3d = np_array.tolist()
    return lista_3d


def similitud(imagen1, imagen2, factor_similitud):
    # Verificar si las dimensiones de las imágenes son iguales
    if len(imagen1) != len(imagen2) or len(imagen1[0]) != len(imagen2[0]):
        raise ValueError("Las dimensiones de las imágenes no son iguales")

    N = len(imagen1)
    M = len(imagen1[0])

    pixeles_similares = 0
    total_de_pixeles = N * M

    for i in range(N):
        for j in range(M):
            distancia = np.linalg.norm(np.array(imagen1[i][j]) - np.array(imagen2[i][j]))
            if distancia < factor_similitud:
                pixeles_similares += 1

    porcentaje_similitud = round((pixeles_similares / total_de_pixeles) * 100)

    return porcentaje_similitud


# Ejemplo de uso
imagen1 = leer_imagen("foto_utec.bmp")
imagen2 = leer_imagen("foto_utec_r.bmp")
factor_similitud = 50  # Puedes ajustar este valor según tus necesidades

porcentaje = similitud(imagen1, imagen2, factor_similitud)
print(f"Porcentaje de similitud: {porcentaje}%")
