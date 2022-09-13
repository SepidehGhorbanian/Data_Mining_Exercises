Text mining: Sentiment scoring

Data: The 'Little Women' book written by Louisa May Alcott

We want to graph the narrative arc of the story

We use the afinn library for sentiment values, nltk library for text functions and re library for regular expressions

After adding line numbers, we tokenize the text and collect it in a series.

Then we use the afinn to score the sentiments (-5 to +5). We can print the frequency table and see that the words with -5 and +5 values are very few and the words with -2 and +2 values are the most commen. It shows that the writer preferred to use moderate sentiments.

We can see the change in sentiments throughout the story by plotting the sentiment arc after making sections of 100 lines.

We can see that the little women book has a positive story and it ends happily.

