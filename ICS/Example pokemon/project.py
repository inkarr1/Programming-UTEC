import pandas as pd
from sklearn.cluster import KMeans

dataset = pd.read_csv("Pokemon.csv")
dataset.drop(['#', 'Type 1', 'Type 2', 'Generation', 'Legendary'], 1, inplace=True)

km = KMeans(n_clusters=3)
grupo = km.fit_predict(dataset[['Total', 'HP', 'Attack', 'Defense', 'Sp. Atck', 'Sp, Def', 'Speed']])

dataset['nueva'] = grupo

print(dataset)
