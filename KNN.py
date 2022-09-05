
"""

@author: UNISEPP
"""
# KNN Classification on breast cancer dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import plot_confusion_matrix

#importing data
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data')

#preparing the data
print(data.describe())
print(data.info())
data.drop('1000025' , axis = 1 ,inplace = True)
data.columns = ['x' + str(i) for i in range (0,len(data.columns) - 1)] + ['y']
data['x5']=pd.to_numeric(data['x5'],errors='coerce')
data.dropna(inplace = True)
print(data.head())

#splitting the data
x_trn , x_tst , y_trn , y_tst = train_test_split(data.filter(regex = '\d') , data.y , test_size= 0.3 , random_state = 1 , shuffle = True)
# We filter the data with regex = '\d' to get the data where the string contains digits (x0 to x8)

#fitting
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_trn , y_trn)
predicted = knn.predict(x_tst)

#calculating acuuracy
print(knn.score(x_tst , y_tst))

#finding the best k 
param = range(3,10,2)
grid = GridSearchCV(knn, {'n_neighbors': param})
best_knn = grid.fit(x_trn , y_trn).best_estimator_
print(best_knn.get_params())
# shows that the best number of neighbors is 3

#optimized knn
knn2= KNeighborsClassifier(n_neighbors = 3)
knn2.fit(x_trn , y_trn)
acc2 = knn2.score(x_tst , y_tst)
print(acc2)

#testing 
diagnosis = ['bengin' , 'malignant']
plot_confusion_matrix(knn2 , x_tst , y_tst, display_labels = diagnosis  , normalize ='true')
print(knn2.score(x_tst,y_tst))
