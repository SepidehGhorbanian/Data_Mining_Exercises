"""

@author: UNISEPP
"""
# Sentiment scoring
# Little women

import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt
from afinn import Afinn

from nltk.tokenize import word_tokenize


data = pd.read_csv('Little_Women.txt' , sep='\t').dropna()
data['line'] = range(1,len(data) +1)
data.rename(columns = {'Little Women': 'text'}, inplace=True)
print(data.head())

# tokenize the data
def cleantext(text):
    text = text.lower()
    text = text.replace("'" , "")
    text= re.sub(r'[^\w]', ' ' , text)
    text= re.sub(r'\s+', ' ' , text)
    text=text.strip()
    return text
data['text'] = data['text'].map(cleantext)
data['text'] = data['text'].map(word_tokenize)
print(data.head())

df = data.explode('text').rename(columns = {'text' : 'token'})
print(df.head())

# Scoring
afinn = Afinn()
df['score'] = df['token'].map(afinn.score).astype(int)
df = df[df['score']!=0]

# Frequency Table
freq = df.score.value_counts().sort_index().to_frame('n')
print(freq)

# Avergae sentimate score for each 100 lines
score_arc = df.groupby(df['line']//100).score.mean().to_frame('score').rename_axis('section')
print(score_arc)

# Plotting the sentiment arc
ax = score_arc.plot.line(legend= False , grid = True , color = 'gray')
score_arc.rolling(10,min_periods=5).mean().plot.line(ax = ax , color = 'black')
plt.xlabel('section of 100 lines')
plt.ylabel('mean sentiment score')
plt.title('Little Women')
plt.axhline()







