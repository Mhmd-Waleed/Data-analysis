# ==========================================================
#                       DS-Jobs Project
# ==========================================================
# Author: Mohammed Waleed
# Data : DS-Jobs data
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
df = pd.read_csv(r'E:\Projects\17- ds-jobs project\ds_salaries.csv')
df.head()
df.columns

#%% understand data
# =============================================================================
# Columns:
# Unamed: 0 --> Index (Remove)
# work_year --> The year the salary was paid
# experience_level --> Level of experience (junior, senior,...)
# employment_type --> Type work (Full time, freelance, part,.. )
# job_title --> Name the job
# salary --> The amount paid
# salary_currency --> Type of currency
# salary_in_usd --> Convert salary from differnt types to USD
# employee_residence --> Primary country of employee
# remote_ration --> The overall amount of work done remotely
# company_location --> The location of company
# company_size --> Size of company (s, m, l)
# =============================================================================

#%% ask questions
"""
1. Top 5 jobs by salary (Done)
2. Top 5 companies location by salary (Done)
3. distribution of companies size (Done)
4. salary over work_year (Done)
6. there are relation between experience_level & slary (Done)
"""
#%% clean data
df.drop(columns='Unnamed: 0', inplace=True)

missing = df.isnull().sum()
print(f'Missing Values:\n{missing[missing > 0]}')

duplicate0 = df.duplicated().sum()
print(f'Duplicated:\n{duplicate0}')
df.drop_duplicates(inplace=True)
duplicate1 = df.duplicated().sum()
print(f'Duplicated:\n{duplicate1}')

#%% answer the questions
df.dtypes
job_salary = (df.groupby('job_title')['salary_in_usd'].mean()
              .head()
              .reset_index()
              .sort_values(by='salary_in_usd', ascending=False)
              )
plt.figure(figsize=(10,8))
sns.barplot(data=job_salary, x='job_title', y='salary_in_usd', palette='colorblind')
plt.xlabel('job title')
plt.ylabel('Salary (USD)')
plt.title('Top 5 Job By salary')
plt.show()

dis_size = df['company_size'].value_counts().reset_index()
dis_size.columns = ['company_size', 'count']
plt.pie(
    dis_size['count'],
    labels=dis_size['company_size'],
    autopct='%1.1f%%',      
    startangle=90,          
    wedgeprops={'edgecolor': 'white'}
)

plt.title('Company Size Distribution')
plt.tight_layout()
plt.show()

com_salary = (
    df.groupby('company_location')['salary_in_usd'].mean()
    .reset_index()
    .sort_values(by='salary_in_usd', ascending=False)
    .head()
    )
com_salary.columns = ['company_location', 'salary']

plt.figure(figsize=(8,5))
sns.barplot(data=com_salary,
            x='company_location',
            y='salary',
            palette='Blues'
            )
plt.xlabel('Company Location')
plt.ylabel('Salary')
plt.title('Top 5 Companies by Salary')
plt.show()

year_salary = (df.groupby('work_year')['salary_in_usd'].mean()
               .reset_index()
               .sort_values(by='work_year', ascending=False)
               )
plt.figure(figsize=(8,5))
plt.plot(
    year_salary['work_year'],
    year_salary['salary_in_usd'],
    color='green',
    linestyle='--',
    marker='o'
)
plt.xlabel('Year')
plt.ylabel('Average Salary (USD)')
plt.title('Salary Over Time')
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.show()

sns.boxplot(data=df, x='experience_level', y='salary_in_usd')
plt.title('Salary Distribution by Experience Level')
plt.show()
#%%
# ============================================================
# Key Insights:
# ==============
# 1. Highest job salary is Applied Data Science
# 2. Russia Companies Hisghest salary
# 3. 51.3% medium comapny
# 4. From 2021 The salary in increasing
# 5. Yes Entry level has lowest salary and
#    Expert Has Highest Salary
# ============================================================
