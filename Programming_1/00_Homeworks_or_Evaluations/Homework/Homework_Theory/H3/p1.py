import numpy as np
import imageio


def leer_imagen(ruta):
    np_array = np.array(imageio.v3.imread(ruta), dtype='int')
    lista_3d = np_array.tolist()
    return lista_3d


def guardar_imagen(ruta, lista_3d):
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))


def color_alternativo(img):
    nw_img = [row[:] for row in img]
    # ACA EMPIEZA TU SOLUCION

    rows = len(img)
    columns = len(img[0])
    channels = len(img[0][0])

    # Iterar sobre cada píxel y canal de color
    for i in range(rows):
        for j in range(columns):
            for channel in range(channels):
                if 0 <= channel < 3:
                    #Aplicar la operación 255 - canal
                    nw_img[i][j][channel] = 255 - nw_img[i][j][channel]

    #ACA TERMINA TU SOLUCION
    return nw_img


# Cargar la imagen utilizando la función leer_imagen(ruta)
ruta_imagen = '/home/inkarri/GitHub/Programming-UTEC/Programming_1/00_Homeworks_or_Evaluations/Homework/Homework_Theory/H3/imagenes/foto_utec.bmp'
imagen = leer_imagen(ruta_imagen)

# Aplicar el método color_alternativo() a la imagen cargada
imagen_modificada = color_alternativo(imagen)

# Guardar la imagen modificada utilizando la función guardar_imagen(ruta, lista_3d)
ruta_imagen_modificada = 'foto_utec_color_alternativo.bmp'
guardar_imagen(ruta_imagen_modificada, imagen_modificada)
