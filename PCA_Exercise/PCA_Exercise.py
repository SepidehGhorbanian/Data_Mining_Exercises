
"""

@author: UNISEPP
"""
# Combining dimentions using PCA, on swiss dataset

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

data = pd.read_csv('swiss.csv')
data.drop(columns ='Location' , inplace= True)
print(data.head())

pca = PCA()
data_tf = pca.fit_transform(data)
vis1=plt.plot(pca.explained_variance_ratio_)  # We can see that we have a 2 component solution
plt.show()
vis2=sns.scatterplot(x = data_tf[: , 0] , y = data_tf[: , 1]) # We can see a clean seperation
