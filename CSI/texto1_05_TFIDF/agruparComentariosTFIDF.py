import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

datos = pd.read_csv("comentarios.csv")
print("\nLos mensajes son: ")
print(datos)

vec = TfidfVectorizer()
x = vec.fit_transform(datos['texto'])

print("\nLa matriz TFIDF es: ")
print(x.toarray())

print("\nTotal de palabras: ")
print(len(vec.vocabulary_))

print("\nEl vocabulario es: ")
print(vec.vocabulary_.keys())

#Generar cabeceras para la matriz
cabeceras = sorted(vec.vocabulary_.keys())

#Agrupamiento
TablaTFIDF = pd.DataFrame(data=x.toarray(), columns=cabeceras)
km = KMeans(3)
grupo = km.fit_predict(TablaTFIDF)

TablaTFIDF['categoria'] = grupo
print(TablaTFIDF)

TablaTFIDF.to_csv("comentariosAgrupdos.csv")
