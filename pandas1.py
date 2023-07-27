import pandas as pd
import numpy as np
import matplotlib.pyplot as mpt
from openpyxl.workbook import Workbook

print("")
'''
#reading CSV file
df = pd.read_csv("data.csv")

#reading excel File
df2= pd.read_excel("sample-xls-file-for-testing.xls","Sheet1")

#replacing NaN values by zero
df.fillna(0, inplace=True)
df2.fillna(0, inplace=True)


#setting index as segment column
df2.set_index('Segment', inplace=True)

print(df)
print(df2)

#printing selected columns
print(df[['id', 'first_name', 'hs_gpa']])
print(df2[['Segment', 'Product', 'Units Sold']])

#calculating Statistics
print(df['hs_gpa'].mean())
print(df['hs_gpa'].max())
print(df['hs_gpa'].min())

print(df2['Profit'].mean())
print(df2['Profit'].max()) 
print(df2['Profit'].min()) 

print(df.shape)                          #print no. of rows, columns
print(df.head(3))                        #print dataframes from starting
print(df.tail(3))                        #print dataframes from ending
print(df[2:6])                           #print dataframes between a and b
print(df.columns)                        #print column cells of dataset
print(type(df['hs_gpa']))                #print type of datasets
print(df.describe())                     #print all statistical values

#conditional print of dataframes
dp = df[["first_name",'last_name']][df.hs_gpa <= df['hs_gpa'].mean()]
print(dp)

#print all column values in the row of passed argument
print(df.loc[111114])

#to replace particular values in dataframe

def countary(cell):
    if cell == "United States of America":
        return "U.S.A."
    return cell

def pro_duct(cell):
    if cell == "Montana":
        return "Merowana"
    return cell


fpp = pd.read_excel("data.xls", "Sheet1", index_col=False, converters={
    'Country': countary,
    'Product': pro_duct
})
fpp.set_index("Segment", inplace=True)

#writing new excel file
fpp.to_excel("data.xlsx", sheet_name='Sheet1', index=False)
print(fpp)

#Combining two dataframe to single excel file
with pd.ExcelWriter("myfilr.xlsx") as writer:
    df.to_excel(writer, sheet_name='s1')
    fpp.to_excel(writer, sheet_name='s1',startrow=11)

print(df.to_markdown())                  #to print dataframes with table format
dpp = df.interpolate()                   #it interpolates the values linearly by default
ddt = df.dropna()                        #skip the rows having Nan
print(ddt.to_markdown())

print(df.to_markdown())                  #replacing values with NaN
dpt = df.replace({
    'Country': 'USA',
    'Product': 'Montana',
    'Units Sold': 1513,
    'Manufacturing Price': '$3.00'
}, np.NaN)
print(dpt.to_markdown())

#removing alphabetic values
dpp = df.replace({"Product": '[A-Za-z]'},"", regex=True)
with pd.ExcelWriter("myfilr1.xlsx") as writer:
    dpp.to_excel(writer, sheet_name='s1')
print(df.to_markdown())

#grouping data under particular category
gdf = df.groupby('Country')
print(gdf)

#groupwise printing grouped data
for Country, Country_df in gdf:
    print(Country)
    print(Country_df)

#getting data of particular group 
print(gdf.get_group('Mexico'))
print(gdf.max())
print(gdf.mean())
print(gdf.describe())

#concatining two datasets
df3 = pd.read_csv("book1.csv")
df3.set_index('Segment', inplace=True)
dpp = pd.concat([df, df3], keys=["frst", "second"])
with pd.ExcelWriter("myfilr2.xlsx") as writer:
    dpp.to_excel(writer, sheet_name='s1')
print(dpp)
print(dpp.loc['second'])

#merging two datasets on column
df4 = pd.DataFrame({
    'weather': ['Sunny', 'Rainy', 'Cloudy'],
    'Temperature':[41,32,37]
})
df5 = pd.DataFrame({
    'weather': ['Cloudy', 'Rainy', 'Sunny'],
    'Wind Speed':[11,9,7]
})
print(pd.merge(df4,df5, on='weather'))

#if columns are not same then merging will be according set intersection method(common ones will be merged)
df4 = pd.DataFrame({
    'weather': ['Sunny', 'Rainy', 'Cloudy', 'dry'],
    'Temperature': [41, 32, 37, 45]
})
df5 = pd.DataFrame({
    'weather': ['Cloudy', 'Rainy', 'Thunderstorm'],
    'Wind Speed': [11, 9, 15]
})
print(pd.merge(df4, df5, on='weather'))

#merging with union operation
df4 = pd.DataFrame({
    'weather': ['Sunny', 'Rainy', 'Cloudy', 'dry'],
    'Temperature': [41, 32, 37, 45]
})
df5 = pd.DataFrame({
    'weather': ['Cloudy', 'Rainy', 'Thunderstorm'],
    'Wind Speed': [11, 9, 15]
})
print(pd.merge(df4, df5, on='weather', how='outer'))

#to add suffixes to data
df4 = pd.DataFrame({
    'weather': ['Sunny', 'Rainy', 'Cloudy', 'dry'],
    'Temperature': [41, 32, 37, 45],
    'Wind Speed': [11, 9, 12, 15]
})
df5 = pd.DataFrame({
    'weather': ['Cloudy', 'Rainy', 'Thunderstorm'],
    'Temperature': [41, 32, 45],
    'Wind Speed': [11, 9, 15]
})
print(pd.merge(df4, df5, on='weather', indicator=True, suffixes=('_4', '_5')))

#to reshape the table
print(df2.pivot(index='Country', columns='Product'))
print(df2.pivot_table(index='Country', columns='Product'))
print(df2.pivot_table(index='Country', columns='Product', aggfunc='count'))

'''

df2 = pd.read_excel("sample-xls-file-for-testing.xls", "Sheet1")
print(df2.pivot_table(index='Country', columns='Product', aggfunc='diff'))
