 Using the K_Means algorithm from clustering algorithms (unsupervised)

The code is in Python and it is using the Scikit-learn (Sklearn) library

Dataset: The iris dataset

Step 1: Importing and understanding the dataset The data includes the following features:sepal.length, sepal.width, petal.length, petal.width , variety (the label)

Step 2: Eliminating the label column ('vareity') and saving it in another list to use later for the name of the clusters

Step 2: Preparing the data by selecting 2 chosen features (sepal.length, sepal.width)

Step 3: Finding the optimal number of K for k_means using the elbow curve: The best value of k appears when the value of 'WCSS' slowly stops decreasing
( It shows that the calculated number for best k is obviously equal to the the number of different labels )

Step 4: Fitting the algorithm to the dataset

Step 5: Plotting and visulazing to show the result
