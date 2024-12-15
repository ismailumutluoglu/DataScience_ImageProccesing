
import matplotlib.pyplot as plt

import pandas as pd

dataframe =  pd.read_csv("iris.csv")

dataframe1 = dataframe.drop(["Id"],axis = 1)
                            
setosa = dataframe[dataframe.Species == "Iris-setosa"]
versicolor = dataframe[dataframe.Species == "Iris-versicolor"]
virginica = dataframe[dataframe.Species == "Iris-virginica"]

plt.hist(setosa.SepalLengthCm , bins = 15)
plt.xlabel("SepalLengthCm values ")
plt.ylabel("frekans")
plt.title("Histogram", color = "black")
plt.show()
