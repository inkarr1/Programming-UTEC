import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

datos = pd.read_csv("smogon.csv") #definivos el cav en esta variable
print("\n Los mensajes son: ")
print(datos)

vec = TfidfVectorizer(ngram_range=(3,4))#crea una matriz de funciones TFIDF ///n-gramas son secuencias continuas de palabras
x = vec.fit_transform(datos['moves'])

print("\nLa matriz TFIDF es: ")
print(x.toarray())

print("\nTotal de tokens: ")#cantidad de elementos de la la lista vocabulario
print(len(vec.vocabulary_))

print("\nEl vocabulario es: ")#muestra la lista de vocabulario
print(vec.vocabulary_.keys())

#Generar cabeceras para la matriz
cabeceras = sorted(vec.vocabulary_.keys())

#agrupamiento
TablaTFIDF = pd.DataFrame(data=x.toarray(), columns=cabeceras)
km=KMeans(18)#Cuantos clusters queremos definir para darle un valor a cada fila con valores similares, con centros aleatorios  ----- dividir los datos en grupos de 18 en este caso
grupo = km.fit_predict(TablaTFIDF)

TablaTFIDF['Tipos']=grupo#nombrar los 18 clusters en tipos de pokemones(agua,fuego,electrico)
print(TablaTFIDF)

TablaTFIDF.to_csv("Agrupacion_en_tipos.csv")



print("Nombrando los  indices de los cluster por tipos que van cambiando aleatoriamente")
TablaTFIDF.Tipos=TablaTFIDF.Tipos.replace([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
                                          ["Acero","Agua","Bicho","Dragon","Eléctrico","Fantasma",
                                           "Fuego","Hada","Hielo","Lucha","Normal","Planta","Psiquico",
                                           "Roca","Siniestro","Tierra","Veneno","Volador"])

columna_tipos=TablaTFIDF.Tipos
d=pd.concat([datos.Pokemon,columna_tipos],axis=1)
print(d)