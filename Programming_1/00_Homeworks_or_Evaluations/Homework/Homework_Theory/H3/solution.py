import imageio
import numpy as np

# UTILIZAR ESTAS FUNCIONES PARA COMPROBAR SI SU SOLUCIÓN ES CORRECTA.
# NO LO VAYAN A INCLUIR CUANDO SUBAN SU SOLUCIÓN A GRADESCOPE



def leer_imagen(ruta):
    """
    La función leer_imagen recibe un string con la ruta
    de una imagen en formato BMP y retorna una lista de
    tres dimensiones con el mapa de bits de la imagen.
    Asimismo, convertimos la lista de numpy a una lista
    común y corriente.
    """
    np_array = np.array(imageio.imread(ruta), dtype='int')
    # noinspection PyTypeChecker
    lista_3d = np_array.tolist()
    return lista_3d


def guardar_imagen(ruta, lista_3d):
    """
    La función guardar_imagen recibe una lista de 3
    dimensiones con el mapa de bits de la imagen
    y retorna la imagen en formato bmp.
    """
    return imageio.imwrite(ruta, np.array(lista_3d, dtype='uint8'))






# NO UTILICEN INPUTS NI PRINTS EN LA ENTREGA FINAL EN GRADESCOPE



class Solution:
    def color_alternativo(self, img):
        nw_img = [row[:] for row in img]
        #ACÁ EMPIEZA TU SOLUCIÓN
        rows = len(img)
        columns = len(img[0])
        channels = len(img[0][0])

        for i in range(rows):
            for j in range(columns):
                for channel in range(channels):
                    if 0 <= channel < 3:
                        nw_img[i][j][channel] = 255 - nw_img[i][j][channel]
        #ACÁ TERMINA TU SOLUCIÓN
        return nw_img


    def reflejar(self, img):
        new_img = [row[:] for row in img]
        #ACÁ EMPIEZA TU SOLUCIÓN
        for row in new_img:
            row.reverse()
        #ACÁ TERMINA TU SOLUCIÓN
        return new_img

    def superposicion(self, img, img_2, x,y):
        img_3 = [row[:] for row in img_2]
        #ACÁ EMPIEZA TU SOLUCIÓN

        height_1 = len(img)
        width_1 = len(img[0])
        height_2 = len(img_2)
        width_2 = len(img_2[0])

        for i in range(height_1):
            for j in range(width_1):
                if 0 <= i + y < height_2 and 0 <= j + x < width_2:
                    img_3[i + y][j + x] = img[i][j]

        #ACÁ TERMINA TU SOLUCIÓN
        return img_3




    def similitud(self, img, img_2, factor):
        porcentaje_similitud = 0
        #ACÁ EMPIEZA TU SOLUCIÓN

        pixeles_similares = 0
        total_de_pixeles = 0

        if len(img) != len(img_2) or len(img[0]) != len(img_2[0]):
            return porcentaje_similitud

        N = len(img)
        M = len(img[0])

        for i in range(N):
            for j in range(M):
                distancia = sum([(a - b) ** 2 for a, b in zip(img[i][j], img_2[i][j])]) ** 0.5
                if distancia < factor:
                    pixeles_similares += 1
                total_de_pixeles += 1

        porcentaje_similitud = round((pixeles_similares / total_de_pixeles) * 100)

        #ACÁ TERMINA TU SOLUCIÓN
        return porcentaje_similitud