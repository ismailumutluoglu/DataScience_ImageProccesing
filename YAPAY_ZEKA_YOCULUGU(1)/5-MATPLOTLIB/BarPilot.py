import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataframe =  pd.read_csv("iris.csv")

dataframe1 = dataframe.drop(["Id"],axis = 1)
                            
setosa = dataframe[dataframe.Species == "Iris-setosa"]
versicolor = dataframe[dataframe.Species == "Iris-versicolor"]
virginica = dataframe[dataframe.Species == "Iris-virginica"]


x = np.array([1,2,3,4,5,6,7])
a = ["turkey","usa","ırak","german","british","dubai","mısır"]
y = x*2+5


# plt.bar(x,y)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Bar Pilot", color = "black")
# plt.show()
 

plt.bar(a,y,color = "red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Bar Pilot", color = "black")
plt.show()
