import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

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

