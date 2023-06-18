# FILTROS
## E1 - Filtro alternativo
Para este ejercicio, alternaremos los colores de cada pixel 
de la imagen. Para ello, por cada canal (R,G,B) de cada pixel de la
imagen realizaremos la operacion 255 - canal.

_pixel[i][j][c] = 255 - pixel[i][j][canal]_ 0 <= canal <= 3


## E2 - Reflejar imagen
Para este problema, lo que deseamos hacer es realizar un reflejo 
de la imagen original, de manera que los pixeles de la izquierda 
se coloquen a la derecha y viceversa.

## E3 - Superposicion
Para este ejercicio, recibiremos dos imagenes y una posicion P. La primera imagen se 
colocará encima de la segunda imagen, donde la posicion del pıxel que se encuentra en la 
esquina superior izquierda de la primera imagen debe coincidir con P.

## E4 - Similitud de imagenes
El objetivo del ejercicio es conocer el porcentaje de similitud entre dos imagenes. Para
esto, tendremos de entrada dos imagenes y un factor de similitud. Se considera que dos pixeles
son similares si su distancia euclideana es menor que el factor de similitud.

Sean las imagenes de dimensiones NxM imagen_1 e imagen_2, el pixel i,j de ambas imagenes se 
consideran similares si y solo si se cumple la siguiente condicion:

```
dist(img[i][j]),img_2[i][j]) < factor ∀i, j ∈ Z 0 ≤ i < N ∧ 0 ≤ j < M
```

Considere que cada vez que se cumple esta condicion la variable `pixeles_similares` aumenta en 1.
Finalmente, para conocer el porcentaje de similitud entre las dos imagenes usaremos la siguiente formula:

```
porcentaje_de_similitud = round((pixeles_similares/total_de_pixeles) * 100)
```

Note que la `variable_pixeles` esta dado por el producto de `N * M`.

Nota:
- Utilizar la funcion round de Python.
- Las dimensiones de ambas imagenes son iguales
- Si deseas probar tu solucion, utiliza las imagenes `foto_utec.bmp` y `foto_utec_r.bmp`
