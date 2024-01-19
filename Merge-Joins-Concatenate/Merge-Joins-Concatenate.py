import pandas as pd

df1 = pd.read_csv(r'Python\Merge-Joins-Concatenate\LOTR.csv')

df2 = pd.read_csv(r'Python\Merge-Joins-Concatenate\LOTR 2.csv')

# Meger - combine two Data Frame or CSV or tables
# Here as we have specify df1 first, so by default it will become left table and df2 as mentioned later will be right table. As nothing is explicitly mention it will be a inner join by default.
# In Inner Join will display only the column/values which are same in both the table
df1.merge(df2)

# What the merge does as kind of a default is when you are only joining on a fellowship ID we have this right data frame with Fellowship ID, the left data frame with the fellowship ID - if you're just joining on these(Fellowship ID, of Left & Right) and you're not joining on the first name (Left table) and the first name (Right table) then it's going to separate those into an underscore X and an underscore Y and even though they have the exact same values since we are not merging on that (First Name) column it automatically separates that into two separate columns so we can see the values within each of those columns
df1.merge(df2, how = 'inner', on = 'FellowshipID' )


# If we make a list & add 'First Name' to it, then it's going to look exactly like it did before for 'Inner Join'
df1.merge(df2, how = 'inner', on = ['FellowshipID','FirstName'])

# 'Outer Join' give us all of the Uniques values from both table. If a cell doesnt have a value then it will show 'NAN'.
# Outer joins are kind of the opposite of inner joins they're going to return everything from both tables, if there is overlapping data it won't be duplicated
df1.merge(df2, how = 'outer')

# 'Left Join' is going to take everything from the Left table or the Left data frame, if there is any overlap. It will compare Right DF to Left DF and take values from Right DF which matches Left DF values and the remaining values from Left DF will be given as its Left Join
df1.merge(df2, how = 'left')

# 'Right Join' is basically the exact opposite of the left in the fact that now we're only looking at the right hand DF and then if there's something that matches in Left data frame one then it will pull that
df1.merge(df2, how = 'right')

# 'Cross Join' takes each value from the left data frame and Compares it to each value in the right data frame. It will take a value from Left DF and then to the each value of Right DF. So the result table will be Left DF rows x Right DF rows
df1.merge(df2, how = 'cross')

pd.set_option('display.max.columns',7)
# joins are pretty similar to the merge function. But unlike Merge the we need to explicitly mention suffix for "Join" to work. Join are best to work with Index
df1.join(df2, lsuffix = '_Left', rsuffix = '_Right')
df1.join(df2, on = 'FellowshipID', how = 'outer', lsuffix = '_Left', rsuffix = '_Right')

df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_Left', rsuffix = '_Right')
df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = '_Left', rsuffix = '_Right', how = 'outer')

pd.concat([df1, df2])
pd.concat([df1, df2], join = 'inner')
pd.concat([df1, df2], join = 'outer')
pd.concat([df1, df2], join = 'outer', axis = 1)
# df = df1.append(df2)
#print(df) 