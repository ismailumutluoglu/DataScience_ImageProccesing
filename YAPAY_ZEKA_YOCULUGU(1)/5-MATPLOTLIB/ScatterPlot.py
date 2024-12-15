
import matplotlib.pyplot as plt

import pandas as pd

dataframe =  pd.read_csv("iris.csv")

dataframe1 = dataframe.drop(["Id"],axis = 1)
                            
setosa = dataframe[dataframe.Species == "Iris-setosa"]
versicolor = dataframe[dataframe.Species == "Iris-versicolor"]
virginica = dataframe[dataframe.Species == "Iris-virginica"]

                    

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm , color = "red" , label = "setosa")
plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm , color = "blue" , label = "versicolor")
plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm , color = "green" , label = "virginica")
plt.legend() #labelin gözükmesini sağlar
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot" , color = "black")
plt.show()
 