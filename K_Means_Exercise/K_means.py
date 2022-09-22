"""
@author: UNISEPP
"""
#Clustering Exercise
# K_Means clustering on iris data set

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Preparing the data
data = pd.read_csv('iris.csv')
y = data['variety']
x=data.drop('variety' , axis = 1 ) #deleting the labels
x= pd.DataFrame(StandardScaler().fit_transform(x) , columns = x.columns)
print(x.head())

# Finding the best k
wcss=[]
for i in range(1,11):
    opt_km = KMeans(n_clusters = i , init='k-means++' , n_init = 10 , random_state=1)
    opt_km.fit(x)
    wcss.append(opt_km.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
# The best k is 3

# Setting up k-means
km = KMeans(n_clusters = 3 , init='k-means++' , n_init = 10 , random_state=1)
# Fitting the model to the data
km.fit(x)

# Visualizing
sns.scatterplot(data = x , x = 'sepal.length' , y='sepal.width' , hue = y, style = km.labels_)
# Adding cluster centers
plt.scatter(km.cluster_centers_[:,0] , km.cluster_centers_[:,1] , marker = 'x' , c = 'red')
plt.show()
