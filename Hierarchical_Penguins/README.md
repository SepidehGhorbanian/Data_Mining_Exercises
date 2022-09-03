Using the Hierarchical algorithm from clustering algorithms (unsupervised)

The code is in Python and it is using the Scikit-learn (Sklearn) library and scipy library

Dataset: The Penguins dataset from loading the palmerpenguins package 

Step 1: Importing and understanding the dataset.The data includes the following features: species, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g

Step 2: Renaming the label (species to y) and saving it in another variable to use later for dendrogram, then eliminating it from the dataset

Step 3: Plotting the dendrogram (Dendrogram can be used to find the best number of clusters in datasets that don't have labels)

Step 4: Preparing the data by selecting 2 chosen features (bill_length_mm, bill_depth_mm)

Step 5: Fitting the AgglomerativeClustering algorithm to the selected data 

Step 6: Plotting and visualizing the result
