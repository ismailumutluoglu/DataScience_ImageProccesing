# 1-pandas hizli ve etkili for data frames
# 2-csv ve text dosylarini açıp inceleyip sonuclarımızı bu dosyalara rahat bir şekilde kaydedebiliriz
# 3-pandas kolaylaştırır for missing data
# 4-reshape yapıp datayı daha etkili bir şekilde kullanabiliriz
# 5-slicing and indexin are easy
# 6-time series data analysında yardımcı olur
# 7-en önemlisi hız pandas hız açısından optimize edilmiş hızlı bir libraray

"""
DATA FRAMES

isim   soyisim      yas   medeni durum
ismail umutluoglu   20       bekar
ismail umutluoglu   20       bekar
ismail umutluoglu   20       bekar
ismail umutluoglu   20       bekar
ismail umutluoglu   20       bekar

bunlara data frame denir. Excel dosyası şeklinde yapılar
"""

import pandas as pd 

dictionary = {"Name":["Ismail","Ahmet","Kenan","Hilal","Ayse","sila","büsra","selin"],
              "Age":[15,22,55,62,45,14,15,17],
              "Salary":[1000,2000,3000,4000,5000,6000,7000,8000]}

dataframe1 = pd.DataFrame(dictionary)

#datanın içeriğinde ne olduğunu anlamak için (ön inceleme)
head = dataframe1.head() #dataframe içindeki bastan 5 veriyi gösterir

tail = dataframe1.tail() #dataframe içindeki sondan 5 veriyi gösterir

#%%
#PANDA BASIC METHODS

print(dataframe1.columns)

print(dataframe1.info())

print(dataframe1.dtypes)

print(dataframe1.describe()) #numeric features = columuns  (age,salary)

#%%

#PANDAS INDEXING AND SLICING

print(dataframe1["salary"])
print(dataframe1.salary)

dataframe1["year"] = [2024,2023,2022,2021,2020,2019,2018,2017] #yeni feature ekleme

print(dataframe1.loc[:,"salary"])

print(dataframe1.loc[:3,"salary"]) #pandasta 3 dahil numpyda degil

print(dataframe1.loc[:3,"Name":"salary"])

print(dataframe1.loc[:3,["Name","salary"]])

print(dataframe1.loc[::-1,:])

print(dataframe1.loc[:,:"salary"])

print(dataframe1.loc[:,"Name"])

print(dataframe1.iloc[:,1]) #i = int demek age verilerini verdi



#%%
#FILTRELEME 


filtre1 = dataframe1.salary > 3000
filtrelenmis_data = dataframe1[filtre1]

filtre2 = dataframe1.iloc[:,1] < 30 

dataframe1[filtre1 & filtre2]

print(dataframe1[dataframe1.iloc[:,1] > 30])
print(dataframe1[filtre1 & filtre2])


#%% list comprehensions

ortalama_maas = dataframe1.salary.mean()

dataframe1["Maas_Seviyesi"] = ["yüksek" if ortalama_maas < each else "dusuk" for each in dataframe1.salary]

dataframe1.columns

dataframe1.columns = [each.lower() for each in dataframe1.columns]

# dataframe1.columns = [each.split()[0] + "_" + each.split()[1] if len(each.split() > 1 ) else each  for each in dataframe1.columns]

#%%
#  DROP AND CONCATENATING DATA

dataframe1.drop(["Age "],axis = 1 ,inplace = True)


data1 = dataframe1.head()
data2 = dataframe1.tail()


#verticel
data_concat = pd.concat([data1,data2],axis = 0)

#horizental

Salary = dataframe1.Salary
Name = dataframe1.Name

data_h_concat = pd.concat([Salary,Name] , axis = 1 )

#%%
#TRANSFORMING DATA

dataframe1["yeni_feature"] = [each*2 for each in dataframe1.Salary]

#apply

def multiply(Salary):
    return Salary*2

dataframe1["apply_metodu"] = dataframe1.Salary.apply(multiply)