Time Series Decomposition Algorithm

Dataset: Air passengers dataset
The data contains the number of passengers each month throughout different years from 1949 untill 1960
First thing to do is understanding and analyzing the data
By plotting the data (image: 'Dataset_plot') we can see that there is a pattern for the number of passsengers over time: The number is increasing over time but we have a dramatic seasonal shift

We want to be able to predict patterns

Decomposition: We want to seperate the linear trend going up from the seasonal variation. We use the seasonal_decompose function from the statsmodel library

Additive model: As we see on the plot (image: 'Plot_additive') , the idea in additive model is for a given year you take the dot from the trend and add it to the seasonal and then residual and the sum is the original data.
We can see that the data is spreading over time therefore it might be better to use the multiplicative model (image: 'Plot_multiplicative')

