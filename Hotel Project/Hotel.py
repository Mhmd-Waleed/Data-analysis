# ------------------------------------------------------------
#                       Hotel Bookings Project
# ------------------------------------------------------------
# Author: Mohammed Waleed
# Data : Hotel Bookings data
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
df = pd.read_csv(r'E:\Projects\18- Hotel\hotel_bookings.csv')
df.head()

#%% ask question
"""
1. Resort VS City (~61% City hotel & ~39% Resort hotel)
2. How many canceled (27, ~0.03)
3. Top 5 Agent (9.0)
4. Top 5 Country (PRT)
5. SUM ARD(~9292786)
6. No booking over time (Done) 
7. checked-out vs canceled vs no show (~72.5%, ~26.3%, ~1.2%)
8. cancel rate
"""
#%% clean data
missing = df.isnull().sum()
print(f'Columns:\n{missing[missing > 0]}')

duplicate = df.duplicated().sum()
print(f'Duplicated:\n{duplicate}')
df.drop_duplicates(inplace=True)

df.drop(columns=['company',
                 'arrival_date_year',
                 'arrival_date_month',
                 'arrival_date_week_number',
                 'arrival_date_day_of_month'], inplace=True)
df.fillna({'agent':'No agent',
           'country':'unknown',
           'children':df['children'].median()},
          inplace=True)

df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


#%% answer questions
no_hotel = df['hotel'].value_counts()
print(no_hotel)
plt.figure(figsize=(8,5))
plt.pie(no_hotel,
        autopct='%1.1f%%',                       
        startangle=90,                           
        labels=['City Hotel','Resort Hotel'],
        wedgeprops={'edgecolor': 'white'})
plt.title('Resort VS City', fontsize=14)
plt.legend(
    title='Hotel Type',
    loc='center left', 
    bbox_to_anchor=(1, 0, 0.5, 1)  
    )
plt.tight_layout()
plt.show()

canceled = (df[df['reservation_status']=='Canceled']
    .count()
    .shape[0]
    )
print(f'number of canceled:\n       {canceled}')

agent = df['agent'].value_counts().nlargest(5)
sns.barplot(x=agent.index, y=agent.values, palette='coolwarm')
plt.xlabel('agent')
plt.ylabel('count')
plt.title('Top 5 agent')
plt.tight_layout()
plt.show()

country = df.country.value_counts().nlargest(5)
sns.barplot(x=country.index,y=country.values, palette='plasma')
plt.xlabel('country')
plt.ylabel('count')
plt.title('Top 5 countries')
plt.tight_layout()
plt.show()

ADR = df['adr'].sum()
print(f'average revenue:\n   {ADR}')

df['year'] = df['reservation_status_date'].dt.year

bookings_per_year = df.groupby('year').count().sort_index()
plt.figure(figsize=(8,5))
plt.plot(bookings_per_year.index, bookings_per_year.values, 
         marker='o', linestyle='-', color='teal')

plt.title('Number of Bookings per Year', fontsize=14)
plt.xlabel('Year')
plt.xticks(bookings_per_year.index)
plt.ylabel('Number of Bookings')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

status_count = df['reservation_status'].value_counts()
print(status_count)

plt.figure(figsize=(7,5))
plt.pie(status_count,
        labels=status_count.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=['#00b894','#d63031','#fdcb6e'],
        wedgeprops={'edgecolor':'white'})
plt.title('Booking Status: Checked-Out vs Canceled vs No-Show')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show()

cancel_rate = (
    df.groupby('hotel')['reservation_status']
    .apply(lambda x: (x=='Canceled').mean() * 100)
)
print(cancel_rate)

rev_per_year = df.groupby('year')['adr'].sum()
plt.plot(rev_per_year.index, rev_per_year.values, marker='o', color='orange')
plt.title('Total Revenue per Year')
plt.xlabel('Year')
plt.xticks(rev_per_year.index)
plt.ylabel('Total ADR (€)')
plt.grid(True)
plt.tight_layout()
plt.show()

# ------------------------------------------------------------
#%% key insights:
#   ______________
# 
# city hotels represent ~61% of hotels
# Most agent work 9.0
# Most country PRT
# Sum of average revenue ~9292786 Euro
# Booking start increasing in 2016 and decrase again in 2017
# About ~27.5 of bookings success
# City hotel have higher cancellations (~28.6%)
# Revenue peaked in 2016 before dropping in 2017