#matplotlib görselleştirme kütüphanesi

import pandas as pd

dataframe =  pd.read_csv("iris.csv")

print(dataframe.columns)

print(dataframe.Species.unique())

print(dataframe.info())

print(dataframe.describe())

setosa = dataframe[dataframe.Species == "Iris-setosa"]
versicolor = dataframe[dataframe.Species == "Iris-versicolor"]

print(setosa.describe())
print(versicolor.describe())