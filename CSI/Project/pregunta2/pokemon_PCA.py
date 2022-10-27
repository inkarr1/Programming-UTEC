import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

datos = pd.read_csv("Agrupacion_en_tipos.csv")
#imprimimos todo el dataset (incluye el índice de el dataframe anterior)
#también incluye el cluster que no queremos
print(datos)

#eliminaremos la tipos
print("eliminando la columna tipos:")
datos.drop(['Tipos'], axis=1, inplace=True)
print(datos)

#eliminaremos la columna indice repetida
print("eliminando la columna índice que venía repetida:")
datos.drop(datos.columns[0], axis=1, inplace=True)
print(datos)

pca=PCA(n_components=10)
pca.fit(datos)
print("Se alimentó")

x_pca=pca.transform(datos)
print("se comprimió")
print(x_pca)


print("Tamaño de datos originales:")
print(datos.shape)
print("Tamaño de datos reducidos:")
print(x_pca.shape)

#agruamiento:
cabeceras = ["PCA1", "PCA2", "PCA3","PCA4","PCA5","PC6","PC7","PCA8","PCA9","PCA10"]
tablaTFIDF_PCA  = pd.DataFrame(data=x_pca, columns=cabeceras)
print(tablaTFIDF_PCA)

km = KMeans(18)
cluster = km.fit_predict(tablaTFIDF_PCA[["PCA1", "PCA2", "PCA3","PCA4","PCA5","PC6","PC7","PCA8","PCA9","PCA10"]])
tablaTFIDF_PCA["tipos_comprimidos"] = cluster

print(tablaTFIDF_PCA)

tablaTFIDF_PCA.to_csv("Tipos_agrupados_PCA.csv")

print()
print("Nombrando los  indices de los cluster del PCA por tipos que van cambiando aleatoriamente")
tablaTFIDF_PCA["tipos_comprimidos"]=tablaTFIDF_PCA["tipos_comprimidos"].replace([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
                                          ["Acero","Agua","Bicho","Dragon","Eléctrico","Fantasma",
                                           "Fuego","Hada","Hielo","Lucha","Normal","Planta","Psiquico",
                                           "Roca","Siniestro","Tierra","Veneno","Volador"])

columna_tipos=tablaTFIDF_PCA["tipos_comprimidos"]
print(columna_tipos)
'''d_PCA=pd.concat([datos.Pokemon,columna_tipos],axis=1)
print(d_PCA)'''

