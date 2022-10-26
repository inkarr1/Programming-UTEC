import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

datos = pd.read_csv("smogon.csv")
print("\n Los mensajes son: ")
print(datos)

vec = TfidfVectorizer(ngram_range=(3,4))
x = vec.fit_transform(datos['moves'])

print("\nLa matriz TFIDF es: ")
print(x.toarray())

print("\nTotal de tokens: ")#cantida de elementos de la la lista vocabulario
print(len(vec.vocabulary_))

print("\nEl vocabulario es: ")#muestra la lista de vocabulario
print(vec.vocabulary_.keys())

#Generar cabeceras para la matriz
cabeceras = sorted(vec.vocabulary_.keys())

#agrupamiento
TablaTFIDF = pd.DataFrame(data=x.toarray(), columns=cabeceras)
km=KMeans(18)
grupo = km.fit_predict(TablaTFIDF)

TablaTFIDF['Tipos']=grupo
print(TablaTFIDF)

TablaTFIDF.to_csv("Agrupacion_en_tipos.csv")


