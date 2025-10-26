# ==========================================================
#                       HR-Employee-Attrition Project
# ==========================================================
# Author: Mohammed Waleed
# Data : HR-Employee-Attrition data
# ==========================================================
# Step:
# ======
# 1. import libraries
# 2. load data
# 3. ask questions
# 4. clean data
# 5. answer the questions
# ==========================================================
#%% import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#%% load data
df = pd.read_csv(r'E:\Projects\22- HR\HR-Employee-Attrition.csv')
df.head()

#%% ask questions
"""
1. Gender Distribution 
2. average salary for job role
3. Attrition distribution
4. Bussines Travel distribution
5. average daily rate for job role
6. department distribution
7. job role distribution
"""

#%% clean data

df.info()

missing = df.isnull().sum()
print(f'missing values:\n{missing[missing > 0]}')

duplicate = df.duplicated().sum()
print(f'Duplicates:{duplicate}')
df.drop_duplicates(inplace=True)

df.dtypes

#%% answers 
#%% 1. Gender Distribution
gender = df['Gender'].value_counts()

sns.set_theme(style="whitegrid")
plt.figure(figsize=(8,5))
plt.bar(x=gender.index, height=gender.values, color='skyblue')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

#%% 2. average salary for job role
sa_job = (df
         .groupby('JobRole')['MonthlyIncome']
         .mean()
         .sort_values(ascending=True)
         )

sns.set_theme(style="whitegrid")
plt.figure(figsize=(8,5))
plt.barh(y=sa_job.index, width=sa_job.values)
plt.title('Average Salary by job')
plt.ylabel('Job role')
plt.xlabel('Average Salary')
for index, value in enumerate(sa_job.values):
    plt.text(value, index, f'{value:.0f}', va='center')
plt.tight_layout()
plt.show()

#%% 3. Attrition distribution
Attrition = df['Attrition'].value_counts()

sns.set_theme(style="whitegrid")
plt.figure(figsize=(8,5))
plt.pie(x=Attrition,
        labels=Attrition.index,
        wedgeprops={'width':0.4, 'edgecolor':'white'},
        autopct='%1.1f%%',
        pctdistance=0.80,
        startangle = 90)
plt.title('Attrition Distribution')
plt.tight_layout()
plt.show()

#%% 4. Business Travel distribution
tra = df['BusinessTravel'].value_counts()

sns.set_theme(style="whitegrid")
plt.figure(figsize=(8,5))
plt.pie(
        x=tra,
        labels = tra.index,
        wedgeprops = {'width':0.4,'edgecolor':'white'},
        autopct = '%1.1f%%',
        pctdistance = 0.80,
        startangle = 90
        )
plt.title('Business Travel Distribution')
plt.tight_layout()
plt.show()

#%% 5. average daily rate for role job
rate_job = (df.groupby('JobRole')['DailyRate'].mean()
            .sort_values(ascending=True)
            .reset_index()
            )

sns.set_theme(style="whitegrid")
plt.barh(y=rate_job['JobRole'], width=rate_job['DailyRate'], color='green')
plt.title('Daily Rate for Job Role')
plt.ylabel('Job Role')
plt.xlabel('Daily Rate')
for index, value in enumerate(rate_job['DailyRate']):
    plt.text(value, index, f'{value:.0f}', va='center')
plt.tight_layout()
plt.show()

#%% 6. department distribution
dep = df['Department'].value_counts()

sns.set_theme(style="whitegrid")
plt.pie(
        x = dep,
        labels = dep.index,
        autopct = '%1.1f%%',
        pctdistance = 0.80,
        wedgeprops = {'width':0.4,'edgecolor':'white'},
        startangle = 90
        )

plt.title('Department Distribution')
plt.tight_layout()
plt.show()

#%% 7. job role distribution
job = df['JobRole'].value_counts()

plt.pie(
        x = job,
        labels = job.index,
        autopct = '%1.1f%%',
        pctdistance = 0.80,
        wedgeprops = {'width':0.4,'edgecolor':'white'},
        startangle = 90
        )

plt.title('Job Role Distribution')
plt.tight_layout()
plt.show()

#%% Key Insights

print("🔍 Insights Summary:")
print(f"- Total Employees: {len(df)}")
print(f"- Attrition Rate: {Attrition['Yes'] / len(df) * 100:.2f}%")
print(f"- Highest Paying Role: {sa_job.idxmax()} (${sa_job.max():.0f})")



