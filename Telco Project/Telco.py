# ==========================================================
#                       Telco-Customer Project
# ==========================================================
# Author: Mohammed Waleed
# Data : Telco-Customer data
# ==========================================================
# Step:
# ======
# 1. import libraries
# 2. load data
# 3. ask question
# 4. clean data
# 5. answer the questions
# ==========================================================
#%% import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

#%% load data
df = pd.read_csv(r'E:\Projects\19- Telco\Telco-Customer.csv')
df.head()

#%% ask questions
"""
1. Gender distribution (men represents ~50.4%)
2. Internet Service Distribution (Fiber represent ~44%)
3. Total Charges by Contract (16056168.7)
4. Payment Method distribution (Most payment Method Electronic check)
5. No. Who Have No Phone Service (Has ~90.3%)
6. There are relation betwwen charges and Multipleline (Moderate positive)
"""

#%% clean data

missing = df.isnull().sum()
print(f'missing values:\n{missing[missing > 0]}')

duplicate = df.duplicated().sum()
print(f'Duplicates: {duplicate}')

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df.fillna({'TotalCharges':df['TotalCharges'].mean()}, inplace=True)

plt.figure(figsize=(6,4))
sns.heatmap(df.isnull(), cmap='viridis', cbar=False)
plt.title('Heatmap of Missing Values')
plt.show()

#%% Answer The Questions
total = df['TotalCharges'].sum()
print(f'Total Charges: {total}')

gender = df['gender'].value_counts()
plt.bar(x=gender.index, height=gender.values)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

payment = df['PaymentMethod'].value_counts().sort_values(ascending=True)
plt.figure(figsize=(8,5))
plt.barh(payment.index, payment.values, color='skyblue')
plt.title('Payment Method Distribution')
plt.xlabel('Payment Method')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

internet = df['InternetService'].value_counts()
plt.figure(figsize=(8,5))
plt.pie(
        x=internet.values,
        labels=internet.index,
        wedgeprops={'edgecolor':'white'},
        autopct='%1.1f%%'
        )
plt.title('Internet Service')
plt.tight_layout()
plt.show()

service = df['PhoneService'].value_counts()
plt.pie(
        x = service.values,
        labels = service.index,
        wedgeprops={'edgecolor':'white', 'width':0.4},
        autopct='%1.1f%%',
        startangle=90,
        pctdistance=0.80
        )
plt.title('Phone Service')
plt.tight_layout()
plt.show()

le = LabelEncoder()
df['MultipleLines'] = le.fit_transform(df['MultipleLines'])

corr = df[['MultipleLines', 'TotalCharges']].corr()
sns.heatmap(corr, annot=True, fmt='0.2g', cmap='coolwarm')
plt.title('Correlation: Multiple Lines vs Total Charges')
plt.tight_layout()
plt.show()

#%% Key Insights
""" 
1. Men represent about 50.4% from clients
2. Fiber optic represent the most of internet service 44%
3. Total charges 16056168.7
4. Most Paymnet Method used Electronic check
5. There are ABout 10% don't have Phone service'
6. there are Moderate positive relation between
 multiple lines and Total Charges
"""
