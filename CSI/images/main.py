import pandas as pd
import sklearn import datasets

digits = datasets.load_digits()

# La cantidad de imagenes que hay:
print(len(digits.target))

#print(digits.data)
#imprime la informacion de los 64 pixeles de cada

print(digits.images[0])

print(digits.taget[15])

print(digits.data[15])

df = pd.DataFrame(data=digits.images[0])

df_blank = pd.DataFrame(data=[[0,0,0,0,0,0,0,0]])

df= pd.concat([df,df_blank], ignore_index=True)
#print(df)
'''
df2 = pd.DataFrame(data=digits.images[1])

#Concatenarlos
#Posible: df3 = pd.concat([df, df2]) pero trabajaremos en el mismo df
df = pd.concat([df, df2], ignore_index = True)
df = pd.concat([df,df_blank], ignore_index=True)
print(df)
'''

i = 1

while i < 1797:
    df2 = pd.DataFrame(data=digits.images[i])
    df = pd.concat([df, df2], ignore_index=True)
    df = pd.concat([df, df_blank], ignore_index=True)
    i =+ 1
print(df)


#Agregar el target ocho veces en una misma imagen.

# Meter las imagenes en un data frame
# Las cabeceras poner las categorias
# Agregar un cluster(columnas) como target

# Agregar un algoritmo que esta mejor concatenar