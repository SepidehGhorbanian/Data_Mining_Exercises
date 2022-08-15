
"""

@author: UNISEPP
"""

# Clustering Exercise
# Hierarchical clustering on penguins dataset

from palmerpenguins import load_penguins
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram , linkage

data = load_penguins()
data.drop(columns = {'sex' , 'year' , 'island'} , axis = 1 , inplace = True)
data.dropna(inplace = True)
data.rename(columns = {'species' : 'y'} , inplace = True)
# print(data.head())

data = data.sample(n=75 , random_state = 1)
y = data.y
data.drop('y', axis =1 , inplace = True)
# print(data.head())

hc = linkage(data ,method = 'ward')
fig = plt.figure()
fig1 = dendrogram(hc , leaf_label_func=lambda id : y.values[id])