import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

datos = pd.read_csv("mensajes.csv")
print(datos)

vec = CountVectorizer()
x = vec.fit_transform(datos['mensaje'])

# print("\nLa matriz de frecuencia es: ")
# print(x.toarray())

# print("\nTotal de palabras: ")
# print(len(vec.vocabulary_))

# print("\nEl vocabulario es: ")
# print(vec.vocabulary_)

# print(vec.vocabulary_.keys())
# print(vec.vocabulary_.values())

# AGRUPAMIENTO
matrizDeFrecuencias = pd.DataFrame(data=x.toarray())
km = KMeans(2)
grupo = km.fit_predict(matrizDeFrecuencias)

matrizDeFrecuencias['categoria'] = grupo

print(matrizDeFrecuencias)
