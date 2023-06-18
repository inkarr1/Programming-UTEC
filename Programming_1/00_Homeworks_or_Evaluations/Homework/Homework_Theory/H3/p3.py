import imageio
import numpy as np


def leer_imagen(ruta):
    np_array = np.array(imageio.v3.imread(ruta), dtype='int')
    lista_3d = np_array.tolist()
    return lista_3d


def guardar_imagen(ruta, lista_3d):
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))


def superposicion(img, img_2, x, y):
    img_3 = [row[:] for row in img_2]
    # ACÁ EMPIEZA TU SOLUCIÓN
    height_1 = len(img)
    width_1 = len(img[0])
    height_2 = len(img_2)
    width_2 = len(img_2[0])

    for i in range(height_1):
        for j in range(width_1):
            if 0 <= i + y < height_2 and 0 <= j + x < width_2:
                img_3[i + y][j + x] = img[i][j]
    # ACÁ TERMINA TU SOLUCIÓN
    return img_3


# Supongamos que las imágenes se llaman 'imagen1.png' y 'imagen2.png'
ruta_imagen = 'foto_utec.bmp'
ruta_imagen_2 = 'otra_foto_utec.bmp'

img = leer_imagen(ruta_imagen)
img_2 = leer_imagen(ruta_imagen_2)

# Supongamos que la posición P es (100, 150)
x = 310
y = 200

# Aplicamos la función superposicion
imagen_superpuesta = superposicion(img, img_2, x, y)

# Guardamos la imagen resultante en un archivo
ruta_imagen_superpuesta = 'foto_utec_superpuesta.bmp'
guardar_imagen(ruta_imagen_superpuesta, imagen_superpuesta)
