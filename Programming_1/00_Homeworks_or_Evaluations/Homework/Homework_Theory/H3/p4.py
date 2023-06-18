import numpy as np
import imageio

def leer_imagen(ruta):
    np_array = np.array(imageio.v3.imread(ruta), dtype='int')
    lista_3d = np_array.tolist()
    return lista_3d


def guardar_imagen(ruta, lista_3d):
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))


def similitud(img, img_2, factor):
    porcentaje_similitud = 0
    pixeles_similares = 0
    total_de_pixeles = 0

    # Verificar que las dimensiones de las imágenes sean iguales
    if len(img) != len(img_2) or len(img[0]) != len(img_2[0]):
        return porcentaje_similitud

    # Obtener las dimensiones de las imágenes
    N = len(img)
    M = len(img[0])

    # Recorrer todos los píxeles de las imágenes
    for i in range(N):
        for j in range(M):
            # Calcular la distancia euclidiana entre los píxeles
            distancia = sum([(a - b) ** 2 for a, b in zip(img[i][j], img_2[i][j])]) ** 0.5
            # Verificar si los píxeles son similares
            if distancia < factor:
                pixeles_similares += 1
            total_de_pixeles += 1

    # Calcular el porcentaje de similitud
    porcentaje_similitud = round((pixeles_similares / total_de_pixeles) * 100)
    return porcentaje_similitud


# Ejemplo de uso
imagen1 = "foto_utec.bmp"
imagen2 = "otra_foto_utec_r.bmp"
factor = 10

# Leer las imágenes
matriz1 = leer_imagen(imagen1)
matriz2 = leer_imagen(imagen2)

# Realizar el cálculo de similitud
porcentaje = similitud(matriz1, matriz2, factor)
print("Porcentaje de similitud:", porcentaje)

