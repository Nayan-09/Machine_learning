# ************* importing the library ****************
import pandas as pd
import numpy as np
from sklearn import linear_model

# *********** Taking the path of the file of dataset ***********

file1=input("Enter your file path in forward backslash format, file should be csv format")

# ******** so i will call pandas function, which will read the csv file
df = pd.read_csv(file1)
new_df = df.drop('price',axis='columns')

model=linear_model.LinearRegression()
model.fit(new_df,df.price)

file2=input("Enter your file path, the pediction you want")
area_df = pd.read_csv(file2)
p=model.predict(area_df)
area_df['prices']=p
area_df.to_csv("preictions1.csv")
