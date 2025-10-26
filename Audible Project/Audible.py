# ------------------------------------------------------------
#                       Audible Project
# ------------------------------------------------------------
# Author: Mohammed Waleed
# Data : Audible data
# ------------------------------------------------------------
#   Step:
# __________
# 
# 1. import libraries
# 2. load data
# 3. ask question
# 4. clean data
# 5. answer the questions
# ------------------------------------------------------------
#%% import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%% load data
df = pd.read_csv(r'E:\Projects\21- Audible\audible_uncleaned.csv')
df.head()

#%% ask questions
"""
Top 5 Author 
Top 5 Narrator
count of books over time
Top 5 Languages 
Relation between Rating and price
"""

#%% clean data
df.info()

df['price'] = df['price'].str.replace(',','').str.replace('Free','0')
df['price'] = pd.to_numeric(df['price'])

df['releasedate'] = pd.to_datetime(df['releasedate'], format='%d-%m-%y', errors='coerce')

df['narrator'] = df['narrator'].str.replace('Narratedby:','')
df['author'] = df['author'].str.replace('Writtenby:','')

splitted = df['time'].str.split(' ', expand=True)
splitted.drop(columns=[1,2,4], axis=1, inplace=True)

df = pd.concat([df, splitted], axis=1)

df.fillna({3:0}, inplace=True)

df.replace({
    0:{'Less':'0'},
    3:{'minute':'1'}
    }, inplace=True)

df[0] = pd.to_numeric(df[0])
df[3] = pd.to_numeric(df[3])

df['time'] = (df[0]*60) + df[3]
df.drop(columns=[0,3], inplace = True)

df['rating'] = (
    df['stars']
    .astype(str)
    .str.extract(r'(\d+(?:\.\d+)?)')
    .astype(float)
    .fillna(0)
)

df.drop(columns='stars', inplace=True)

df.info()

#%% Save cleaned file

df.to_csv(r'E:\Projects\21- Audible\Audible_cleaned.csv', index=False)

#%% answers
#%% Top 5 Author 
author = df['author'].value_counts().nlargest(5).sort_values(ascending=True)
print(author)
plt.barh(y = author.index, width= author.values, color='green')
plt.title('Top 5 Author')
plt.xlabel('Count')
plt.ylabel('Author')
plt.tight_layout()
plt.show()

#%% Top 5 Narrator
narrator = df['narrator'].value_counts().nlargest(5).sort_values(ascending=True)
print(narrator)
plt.barh(y = narrator.index, width= narrator.values, color='skyblue')
plt.title('Top 5 narrator')
plt.xlabel('Count')
plt.ylabel('narrator')
plt.tight_layout()
plt.show()

#%% count of books over time
df['year'] = df['releasedate'].dt.year
book_time = df.groupby('year')['name'].count()
print(book_time)
plt.figure(figsize=(10,5))
plt.plot(book_time.index, book_time.values, color='#f98258')
plt.title('Book over Time')
plt.xlabel('Year')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

#%% Top 5 Languages 
language = df['language'].value_counts().nlargest(5).sort_values(ascending=True)
print(language)
plt.barh(y = language.index, width= language.values, color='#A2598A')
plt.title('Top 5 language')
plt.xlabel('Count')
plt.ylabel('language')
plt.tight_layout()
plt.show()


#%% Relation between Rating and price

corr = df[['rating','price']].corr()
sns.heatmap(corr, fmt='.2g', annot=True, cmap='coolwarm')
plt.title('Rating & Price')
plt.tight_layout()
plt.show()

sns.scatterplot(x='rating', y='price', data=df, alpha=0.6)
plt.title('Price vs Rating')
plt.show()
