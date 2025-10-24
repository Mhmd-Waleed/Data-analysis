# ==========================================================
#                       Netflix Project
# ==========================================================
# Author: Mohammed Waleed
# Data : netflix titles data
# ==========================================================
# Step:
# ======
# 1. import libraries
# 2. load data
# 3. understand data
# 4. ask question
# 5. clean data
# 6. answer the questions
# ==========================================================
#%% import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#%% load data
df = pd.read_csv(r'E:\Projects\16- Netflix Project\netflix_titles.csv')
df.head()
#%% understand data
# ==========================================================
# Columns:
# =========
# show_id --> unique value 
# type --> type the work (Movie, Series)
# title --> name of work
# director --> Name who made the work
# cast --> Actress
# country --> The country which made the work
# date_added --> Date of 
# release_date --> the year of this work
# rating --> Rate of the work
# duration --> the time of work
# listed_in --> category of the work
# description --> summary of the work
# ==========================================================

#%% Ask Questions
"""
1. most director write works   (Done)
2. most country made film   (Done)
3. types of work   (Done)
4. most category   (Done)
5. Rating   (Done)
6. films over time   (Done)
"""
#%% Clean Data
missing = df.isnull().sum()
print(f'Null Values:\n{missing[missing > 0]}')

duplicate = df.duplicated().sum()
print(f'No Duplicate:{duplicate}')

df.fillna({'director':'Unknown','cast':'Unknown',
           'Country':'Unknown','rating':'Unknown',
           'country':'Unknown'}, inplace=True)
df.dropna(subset=['date_added','duration'], inplace=True)



#%% Answer Questions
dir_count = df['director'].value_counts().head(6).sort_values(ascending=False)
dir_count = dir_count[1:]
plt.figure(figsize=(10,8))
plt.bar(dir_count.index, dir_count.values, color='skyblue')
plt.xlabel('Director')
plt.ylabel('Count')
plt.title('Top 5 Director')
plt.show()

country_count = df['country'].value_counts().head().sort_values(ascending=False)
plt.figure(figsize=(10,8))
plt.bar(country_count.index, country_count.values, color='salmon')
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('Top 5 Country')
plt.show()

type_count = df['type'].value_counts()
plt.figure(figsize=(6,5))
plt.bar(type_count.index, type_count.values, color='lightgreen')
plt.xlabel('Type')
plt.ylabel('Count')
plt.title('Types of Work')
plt.show()

gener_count = (df['listed_in']
               .dropna()
               .str
               .split(',', expand=True)
               .stack()
               .value_counts()
               .head(5)
               )
plt.figure(figsize=(10,10))
plt.bar(gener_count.index, gener_count.values, color='teal')
plt.xlabel('Gener')
plt.ylabel('Count')
plt.title('Gener Count')
plt.show()

rat_count = df['rating'].value_counts()
explode = [0.01] * len(rat_count)

plt.figure(figsize=(7,7))
plt.pie(
    rat_count.values,
    labels=rat_count.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=plt.cm.Paired.colors,
    explode=explode
)
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()         
fig.gca().add_artist(centre_circle)

plt.title('Rating Distribution', fontsize=14)
plt.tight_layout()
plt.show()

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')


df['year'] = df['date_added'].dt.year


df = df.dropna(subset=['year'])


year_type_count = df.groupby(['year', 'type']).size().unstack(fill_value=0)

plt.figure(figsize=(10,6))
plt.plot(year_type_count.index, year_type_count['Movie'], marker='o', label='Movies', color='red')
plt.plot(year_type_count.index, year_type_count['TV Show'], marker='o', label='TV Shows', color='blue')

plt.title('Movies vs TV Shows Over Time on Netflix')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
#%%
# Key Insights:
# ==============
# - Most directors: Rajiv Chilaka.
# - Most country producing titles: United States.
# - Movies dominate Netflix content.
# - Top genres include: Dramas, Comedies, and Documentaries.