import imageio
import numpy as np


def leer_imagen(ruta):
    np_array = np.array(imageio.v3.imread(ruta), dtype='int')
    lista_3d = np_array.tolist()
    return lista_3d


def guardar_imagen(ruta, lista_3d):
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))


def reflejar(img):
    new_img = [row[:] for row in img]
    # ACÁ EMPIEZA TU SOLUCIÓN
    for row in new_img:
        row.reverse()
    # ACÁ TERMINA TU SOLUCIÓN
    return new_img

ruta_imagen = '/home/inkarri/GitHub/Programming-UTEC/Programming_1/00_Homeworks_or_Evaluations/Homework/Homework_Theory/H3/imagenes/foto_utec.bmp'
imagen = leer_imagen(ruta_imagen)

imagen_reflejada = reflejar(imagen)

ruta_imagen_reflejada = 'foto_utec_reflejada.bmp'
guardar_imagen(ruta_imagen_reflejada, imagen_reflejada)
