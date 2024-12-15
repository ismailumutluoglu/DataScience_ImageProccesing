
import matplotlib.pyplot as plt

import pandas as pd

dataframe =  pd.read_csv("iris.csv")

dataframe1 = dataframe.drop(["Id"],axis = 1)

# dataframe1.plot()
# plt.show()



setosa = dataframe[dataframe.Species == "Iris-setosa"]
versicolor = dataframe[dataframe.Species == "Iris-versicolor"]
virginica = dataframe[dataframe.Species == "Iris-virginica"]


plt.plot(setosa.Id ,setosa.PetalLengthCm, color = "red" , label = "setosa  ")
plt.plot(versicolor.Id ,versicolor.PetalLengthCm, color = "blue" , label = "versicolor  ")
plt.plot(virginica.Id ,virginica.PetalLengthCm, color = "green" , label = "virginica  ")
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.title("Line Plot" , color = "black")
plt.legend()
plt.show()



dataframe1.plot(grid = True )
plt.show()

dataframe1.plot(grid = True , linestyle = ":")
plt.show()

dataframe1.plot(alpha = 0.7)
plt.show()

