'''
print(df[['id', 'first_name', 'hs_gpa']])
print(df['hs_gpa'].mean())
print(df['hs_gpa'].max())
print(df['hs_gpa'].min())

print(df['hs_gpa'].mean())
print(df['hs_gpa'].min())
print(df[['id', 'first_name', 'hs_gpa']])
print(df.shape)
print(df.head(3))
print(df.tail(3))
print(df[2:6])
print(df.columns)
print(type(df['hs_gpa']))
print(df.describe())

dp = df[["first_name",'last_name']][df.hs_gpa <= df['hs_gpa'].mean()]
print(dp)
print(df.loc[111114])



def countary(cell):
    if cell == "United States of America":
        return "U.S.A."
    return cell


def pro_duct(cell):
    if cell == "Montana":
        return "Merowana"
    return cell


fpp = pd.read_excel("data.xlsx", "Sheet1", index_col=False, converters={
    'Country': countary,
    'Product': pro_duct
})
fpp.set_index("Segment", inplace=True)
fpp.to_excel("data.xlsx", sheet_name='Sheet1', index=False)
print(fpp)
with pd.ExcelWriter("myfilr.xlsx") as writer:
    df.to_excel(writer, sheet_name='s1')
    fpp.to_excel(writer, sheet_name='s1',startrow=11)

print(df.to_markdown())
dpp = df.interpolate()                  #it interpolates the values linearly by default
ddt = df.dropna()                       #skip the rows having Nan
print(ddt.to_markdown())

print(df.to_markdown())
dpt = df.replace({
    'Country': 'USA',
    'Product': 'Montana',
    'Units Sold': 1513,
    'Manufacturing Price': '$3.00'
}, np.NaN)
print(dpt.to_markdown())

dpp = df.replace({"Product": '[A-Za-z]'},"", regex=True)
with pd.ExcelWriter("myfilr1.xlsx") as writer:
    dpp.to_excel(writer, sheet_name='s1')
print(np.NaN)

print(df.to_markdown())
gdf = df.groupby('Country')
print(gdf)
for Country, Country_df in gdf:
    print(Country)
    print(Country_df)

print(gdf.get_group('Mexico'))
print(gdf.max())
print(gdf.mean())
print(gdf.describe())
'''