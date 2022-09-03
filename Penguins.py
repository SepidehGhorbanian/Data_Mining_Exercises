
"""

@author: UNISEPP
"""
# Clustering Exercise
# Hierarchical clustering on penguins dataset

# Loading and preparing the dataset
from palmerpenguins import load_penguins
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram , linkage

data = load_penguins()
data.drop(columns = {'sex' , 'year' , 'island'} , axis = 1 , inplace = True)
data.dropna(inplace = True)
data.rename(columns = {'species' : 'y'} , inplace = True)
print(data.head())

# Selecting a random sample
data = data.sample(n=50 , random_state = 1)

# Eliminating labels from the dataset
y = data.y
data.drop('y', axis =1 , inplace = True)
print(data.head())

# Using dendogram
hc1 = linkage(data ,method = 'ward')
fig = plt.figure()
fig1 = dendrogram(hc1 , leaf_label_func=lambda id : y.values[id])
plt.show()

# Fitting the Hierarchical algorithm to the dataset based on 2 features
data2 = data.iloc[:, [0,1]].values
hc2 = AgglomerativeClustering(n_clusters=3 , affinity= 'euclidean' , linkage= 'ward')
y_hc = hc2.fit_predict(data2)

# Visualizing
plt.scatter(data2[y_hc == 0, 0], data2[y_hc == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(data2[y_hc == 1, 0], data2[y_hc == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(data2[y_hc == 2, 0], data2[y_hc == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.title('Hierarchical Clustering')
plt.xlabel('bill_length_mm')
plt.ylabel('bill_depth_mm')
plt.show()
