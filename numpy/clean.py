
import pandas as pd
import numpy as np
df=pd.read_csv('/Users/umesh/Desktop/numpy/laptopData.csv')
print(df.head())

print('missing values in each column')
print(df.isnull().sum())

df['Price'].fillna(df['Price'].mean(),inplace=True)
df.drop_duplicates(inplace=True)

df['Price']=np.where(df['Price']<0,df['Price'].mean(),df['Price'])
print(df)
df.to_csv('cleaned_data',index=False)
