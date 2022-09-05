Predicting whether a patiant has breast cancer or not

Using the KNN algorithm from Classification algorithms (Supervised)

The code is in Python and it is using the Scikit-learn (Sklearn) library

Dataset: The Breast Cancer Wisconsin Dataset from https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/

Preparing the data: After importing the dataset and understanding the features, first we drop the id column, then we rename the columns to 'xi' and the last column to 'y' which is the labels.
after that we change the type of column x5 from object to numeric and lastly we drop the rows that have NULL values.
We split the data into training and testing

Implementing the algorithm: We fit the 'KNeighborsClassifier' to the training dataset and then we can show the predicted values for the testing dataset
Then we calculate the accuracy of the algorithm with the chosen 'k' by the use of 'score' function

Optimizing: We can use the 'Gridsearch' method to find the best number for k and then use it to fit the data and have the best knn algorithm
Then we calcaulate the accuracy and we can see the improvement

Confusion Matrix: At the end we can use the 'Confusion Matrix' to visualize the performance of the best knn with the actual labels that we had in the dataset.




