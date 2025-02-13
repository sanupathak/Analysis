import pandas as pd

#Dataset  ko CSV se  Load Karna
df=data=pd.read_csv("train.csv")
print(df.head())

#Dataset shape cheack(Row & Column)
print("Data_Shape:",df.shape)

#Data Columns Name
print("Columns:",df.columns)

#Data Type & Missing Value Check Karna
print(df.info())
print(df.isnull().sum())

#Statical summery
print(df.describe())

#Outlier Visulitions
import seaborn as sn
import matplotlib.pyplot as plt

#Box plot for Fare
plt.figure(figsize=(10,5))
sn.boxplot(x=df['Fare'])
plt.title('Box plot For Fare')

#Box plot for Age
plt.figure(figsize=(10,5))
sn.boxplot(x=df['Age'])
plt.title('Box plot for Age')
plt.show()

#Dropping Cabin Column
df.drop(columns=['Cabin'],inplace=True)

#Outlier by IQR Method
Q1=df['Fare'].quantile(0.25)
Q2=df['Fare'].quantile(0.75)
IQR=Q2-Q1

lower_bond=Q1-1-5*(IQR)
Upper_bond=Q1+1-5*(IQR)

Outlier= df[(df['Fare'] < lower_bond) | (df['Fare'] >  Upper_bond)]

#Handling/Fill_in  Age & Embarked  Column Missing Value
df['Age']=df['Age'].fillna(df['Age'].median())
df['Embarked']=df['Embarked'].fillna(df['Age'].median())

#Insight Analysis
# 1. Survival Rate Check Karna – Kitne log survive hue aur kitne nahi?
# objectives;
# cheack Karna ki kitne log survive hue aur kitne nahi
# percentage wise compare karna
# Bar Plot Banana(Graphically Show Karna)

# cheack Karna ki kitne log survive hue aur kitne nahi
print(df['Survived'].value_counts())

# percentage wise compare karna
print(df['Survived'].value_counts(normalize=True)*100)

# Bar Plot Banana(Graphically Show Karna)
import seaborn as sns
import matplotlib.pyplot as plt
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.xlabel("Survived(1=Yes, 0=No)")
plt.ylabel("Count")
plt.show()

#2.Gender-wise Survival Rate 
#  Kya female passengers ka survival rate zyada tha?

#2.Gender-wise Survival Rate 
gender_survival_rate=df.groupby('Sex')['Survived'].mean()
print(gender_survival_rate)

# Kya female passengers ka survival rate zyada tha?
#Using Bar Plot
sns.barplot(x=gender_survival_rate.index, y=gender_survival_rate.values)
plt.title("Gender Wise Survival Rate")
plt.xlabel("Gender")
plt.ylabel("Survival Rate")
plt.show()

#3. Class-wise Survival Analysis – Kis class (1st, 2nd, 3rd) me survival chance zyada tha?
class_survival_rate=df.groupby('Pclass')['Survived'].mean()*100
print(class_survival_rate)

#visualiation Class-wise Survial Rate using Bar plot
sns.barplot(x='Pclass',y='Survived', data=df)
plt.title('class_survival_rate')
plt.xlabel('Pclass (1st, 2nd, 3rd)')
plt.ylabel('survival Rate (%)')
plt.show()

4. Fare Distribution – Kitna variation tha fares me?
                                                                                                   
fare_Summary=df['Fare'].describe()
print(fare_Summary)

#Fare Distribution by Histrogram
sns.histplot(df['Fare'], bins=30, kde=True)
plt.title('Fare Distrubution')
plt.xlabel('Fare')
plt.ylabel('Count')
plt.show()


#Fare box distribution
sns.boxplot(x=df['Fare'])
plt.title('Fare Boxplot')
plt.xlabel('Fare')
plt.show()


#Fare distrubution by P CLass-wise
sns.boxplot(x=df['Pclass'],y=df['Fare'])
plt.title('Fare Distrubution by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Fare')
plt.show()

#Log Tranformation to reduce skewness
import numpy as np
df['Fare_log']= np.log1p(df['Fare'])
sns.histplot(df['Fare_log'], bins=30, kde=True)
plt.title('Fare Distrubution')
plt.xlabel('Log Fare')
plt.ylabel('passenger Count')
plt.show()

#5. Age-wise Analysis – Kis age group ka survival chance zyada tha?

#Define the age categories (bins)
bins=[0,10,20,30,40,50,60,100]
labels=['0-10','11-20','21-30','31-40','41-50','51-60','61+']

#Bine the Age column into these categories
df['Age_group']=pd.cut(df['Age'],bins=bins,labels=labels,right=False)

# Age-wise Analysis
Age_Survival_rate = df.groupby('Age_group', observed=False)['Survived'].mean()*100
Age_Survival_rate=Age_Survival_rate.sort_values(ascending=False)
print(Age_Survival_rate)

#visualize survial rate bye
sns.barplot(x=Age_Survival_rate.index, y=Age_Survival_rate.values)
plt.title('Survival Rate per Age Group')
plt.xlabel('Age Group')
plt.ylabel('Survival Rate (%)')
plt.show()