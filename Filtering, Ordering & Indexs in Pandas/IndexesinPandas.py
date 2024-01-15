import pandas as pd

df = pd.read_csv("Python\Filtering, Ordering & Indexs in Pandas\world_population.csv")

# To make any column from the dateset as index
df = pd.read_csv("Python\Filtering, Ordering & Indexs in Pandas\world_population.csv", index_col = 'Country')

# To rest the index to defaut number
df.reset_index(inplace=True)

# Setting column as index in different way
df.set_index('Country', inplace=True)

# As we have already set the index as column before running the code for 'Multiple index' we need to set it back to normal first
# If there is an index column already set then 'Multiple index' will not work
df.reset_index(inplace=True)

# Making multiple columns as Index
df.set_index(['Continent','Country'], inplace=True)

# If we want the indexs sortted after running multiple index function then we can use 'sort_index()' function

# In Jupiter the following code works fine but not in VS
# df.sort_index()

# In VS we either need to assign the result back to the DataFrame for the changes to take effect or you can use the 'inplace' parameter
# df.sort_index(inplace=True)

# For ascending & descending of the column in Jupiter the following works
# df.sort_index(ascending=False)

# For ascending & descending of the column in VS 'inplace=True' must be added
df.sort_index(inplace=True, ascending=[False, True])

pd.set_option('display.max.rows',235)
pd.set_option('display.max.columns',4)

# The following is used to see a sepcific row values of all columns
# In 'loc' we can sepcify index value or any row value
# loc = location (location of any value or string given in parameter)

# After setting the column index we must be careful if we are using 'loc' or 'iloc' because they search according the order of the index.
# If the list contains only one value then by default it will search in the first index column 
# ex: The following has the value as 'Albania' so it will search in the first column which is 'Continent' in this example. But as the value is not present in the first index it will retrun error
# df.loc['Albania']

# The following has values in the list with respect to the index column set 
df.loc['Oceania', 'Guam']

# 'iloc' will only look into index values
# iloc = integer location (location of only integer) 

# Multi index will not effect the search of 'iloc', this will still search accroding to initial index or integer based index
df.iloc[1]

# print(df)
