import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

datos = pd.read_csv("mensajes.csv")
vec = CountVectorizer()
x = vec.fit_transform(datos['mensaje'])

print(x.toarray())

tablaFrecuencias = pd.DataFrame(data=x.toarray())

#agrupamiento:
km = KMeans(n_clusters=2)
grupo = km.fit_predict(tablaFrecuencias)

#proxima clase:
tablaFrecuencias['cluster'] = grupo
print(tablaFrecuencias)