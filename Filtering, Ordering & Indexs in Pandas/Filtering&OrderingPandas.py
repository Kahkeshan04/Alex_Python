import pandas as pd

df = pd.read_csv(r"D:\DA\Python\Filtering, Ordering & Indexs in Pandas\world_population.csv")

# To get compelete columns in the output we can use 'set_option' function and pass the parameter of how many row we want to get displayed. By default the output will display the first 5 and the last 5 column.
pd.set_option('display.max.columns',40)

# Filteration by column
df[df['Rank'] <= 10]

# Finding specific values in a column using 'isin' function
sepcific_countries = ['Bangladesh','Brazil']
df[df['Country'].isin(sepcific_countries)]


# To search for a specific string in the value of a column
df[df['Country'].str.contains('United')]  

# Setting Customize index in place of default index (1,2,3.....)
df2 = df.set_index('Country')

# To select specific columns
df2.filter(items = ['Continent', 'CCA3'])

# We can specify in which axises we want to search 
# axis = 0 → Right direction
# axis = 1 ↓ Downward direction
df2.filter(items = ['Zimbabwe'], axis = 0)

# Similar function to the above
df2.filter(like = 'United', axis = 0)

# loc will only look at value or name not its position
# we get all the columns for United States and value of them
df2.loc['United States']

df2.iloc[3]

# Sorting by any column by default it will be ascending
df[df['Rank'] <= 10].sort_values(by = 'Rank')

# Sorting by Ascending or Descending, the list of 'by' works in order. Whatever the first value is placed will be priotize 
df[df['Rank'] <= 10].sort_values(by = ['Rank', 'Country'], ascending = False)
df[df['Rank'] <= 10].sort_values(by = ['Continent','Country'], ascending = False)

# We can decide which value to be sort in which order
# If the continent value of 'ascending' parameter is True then it will give the values in ascending order
# Then based on the continent values the country values will also be sorted according to the value assign to 'ascending' parameter
# ex: Aisa (continent value), we have multiple country values, so here it will sort the country value of the that aisa in ascending order 
print( df[df['Rank'] <= 10].sort_values(by = ['Continent','Country'], ascending = [True, False]))
# print(df)