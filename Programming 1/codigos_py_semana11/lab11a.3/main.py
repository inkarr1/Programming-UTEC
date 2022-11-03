import requests
import pandas as pd
"""
api = "https://raw.githubusercontent.com/jmcastagnetto/covid-19-peru-data/main/datos/covid-19-peru-camas-uci.csv"
result = requests.get(api)
file = open('covid-19-peru-camas-uci.csv', "w")
file.write(result.text)
file.close()
"""



df = pd.read_csv("covid-19-peru-camas-uci.csv")
#print(df.head())


#print(df[0:3])
#print(df[["fecha","estado","minsa"]])

filter = df['estado'] == "en uso"
df_enuso = df.where(filter)
#print(df_enuso)

grouped_data = df.groupby('estado')
#print(grouped_data.describe())

minsa = df.groupby('estado')['minsa']
#print(minsa.describe())



import matplotlib.pyplot as plt

minsa_resume=df.groupby('estado')['minsa'].mean()
minsa_resume.plot(kind='bar')
plt.show()

