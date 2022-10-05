import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

datos = pd.read_csv("mensajes.csv")
print(datos)

vec = CountVectorizer()
x = vec.fit_transform(datos['mensaje'])

print("\nLa matriz de frecuencia es: ")
print(x.toarray())

print("\nTotal de palabras: ")
print(len(vec.vocabulary_))

# GENERAR CABECERAS PARA LA MATRIZ
#sorted -> te ordena de forma numerica o vocabulario.
cabeceras = sorted(vec.vocabulary_.keys())

# AGRUPAMIENTO
matrizDeFrecuencias = pd.DataFrame(data=x.toarray(), columns=cabeceras)
km = KMeans(2)
grupo = km.fit_predict(matrizDeFrecuencias)

matrizDeFrecuencias['categoria'] = grupo

print(matrizDeFrecuencias)

matrizDeFrecuencias.to_csv("mensajesAgrupados.csv")