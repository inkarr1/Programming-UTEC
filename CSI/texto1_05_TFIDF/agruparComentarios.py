import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

datos = pd.read_csv("comentarios.csv")
print("\nLos mensajes son: ")
print(datos)

vec = CountVectorizer()
x = vec.fit_transform(datos['texto'])

print("\nLa matriz de frecuencias es: ")
print(x.toarray())

print("\nTotal de palabras: ")
print(len(vec.vocabulary_))

print("\nEl vocabulario es: ")
print(vec.vocabulary_)

#Generar cabeceras para la matriz
cabeceras = sorted(vec.vocabulary_.keys())

#Agrupamiento
TablaFrecuencias = pd.DataFrame(data=x.toarray(), columns=cabeceras)
km = KMeans(3)
grupo = km.fit_predict(TablaFrecuencias)

TablaFrecuencias['categoria'] = grupo
print(TablaFrecuencias)

TablaFrecuencias.to_csv("comentariosAgrupdos.csv")
