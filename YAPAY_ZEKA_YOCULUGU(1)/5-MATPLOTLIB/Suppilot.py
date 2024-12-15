import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataframe =  pd.read_csv("iris.csv")

dataframe1 = dataframe.drop(["Id"],axis = 1)
                            
setosa = dataframe[dataframe.Species == "Iris-setosa"]
versicolor = dataframe[dataframe.Species == "Iris-versicolor"]
virginica = dataframe[dataframe.Species == "Iris-virginica"]


dataframe1.plot(grid = True , alpha = 0.9 ,subplots = True)
plt.show()

plt.subplot(2,1,1)
plt.plot(setosa.Id ,setosa.PetalLengthCm, color = "red" , label = "setosa  ")
plt.ylabel("setosa - PetalLengthCm ")
plt.title("Subplot", color = "black")

plt.subplot(2,1,2)
plt.plot(versicolor.Id ,versicolor.PetalLengthCm, color = "blue" , label = "versicolor  ")
plt.ylabel("versicolor - PetalLengthCm ")
plt.title("Subplot", color = "black")
plt.show()


dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],

              "AGE":[15,16,17,33,45,66],

              "MAAS": [100,150,240,350,110,220]}

dataFrame1 = pd.DataFrame(dictionary)