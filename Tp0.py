import pandas as ps
import matplotlib.pyplot as plt
import numpy as np

#Question 1 création du dataframe df_p
df_p=ps.DataFrame([])

data={
    "Pays":["Etas-Unis","Chine","Inde","Japon"],
    "Population":[331002651,1439323776,1380004385,126476461],
    "Superficie":[9629091,9640011,3287263,377972],
    "Taux de croissance annuel":[0.6,0.4,1.1,-0.2]
}

df_p=ps.DataFrame(data)
print(df_p)

#Question 2 transformation en dict_pays
print("******transformation******")
dict_pays=dict(df_p)
print(dict_pays)

#Question 3 Tri des éléments du dictionnaire par ordre croissant de la population
print("*****Tri******")
sorted_values={}
keys=dict_pays.keys()
sorted_keys=sorted(keys)
for key in sorted_keys:
  sorted_values[key]=dict_pays[key]
print(sorted_values)

#dictTrie = sorted(dict_pays.items(), key=lambda x: x[1]['Population'])
#print(dictTrie)



#Question 4 graphiques a barres
x=df_p["Pays"]
y=df_p["Population"]
plt.bar(x,y)
plt.xlabel("Pays")
plt.ylabel("Population")
plt.show()

#Question 5 graphiques en nuages de points
x=df_p["Superficie"]
y=df_p["Taux de croissance annuel"]
plt.scatter(x,y)
plt.xlabel('Superficie')
plt.ylabel('Taux de croissance annuel')
plt.show()