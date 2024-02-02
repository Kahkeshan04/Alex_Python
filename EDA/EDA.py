import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

df = pd.read_csv(r"Python\EDA\world_population.csv")

pd.set_option('display.max.columns',17)

# To change how many decimal point we are looking at
pd.set_option('display.float_format', lambda x: '%.2f' % x)

# OR

# pd.set_option('display.float_format', '{:.2f}'.format) 
# pd.set_option('display.float_format', lambda x: f"{x:.2f}".format) 

# Infromation of the table
df.info()

# High level overview with all -> count, mean, std, min, 25%, 50%, 75%, max values
df.describe()

# To find how many values are missing or null values
df.isnull().sum()

# To find the unique values
df.nunique()

# To see the top rang population country. head() will show the top 5 values. The following will sort from lowest to highest
df.sort_values(by = "2022 Population").head()

# By add ascending = False, it will show the largest values
df.sort_values(by = "2022 Population", ascending = False).head()

# We can sepcify the number of values we want in head(num)
df.sort_values(by = "2022 Population", ascending = False).head(10)

# Correlation -> It will comparing every column to every other column and looking at how closely correlated they are
df.corr(numeric_only = True) 

# Heat Map -> To visulize the above correlation
sns.heatmap(df.corr(numeric_only = True),annot=True)

# To increase the size of the heat map
plt.rcParams['figure.figsize']=(20,7)
plt.show()


# Grouping -> This will combine all the same values rows of Continent (column which is mentioned)
df.groupby('Continent').mean(numeric_only=True)

# Grouping the 'Continent' and sorting the values based on the '2022 Population'. It will display all the columns
df.groupby('Continent').mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)


#  All the column names in the list. This will dispaly only all 'Population' Columns. This will display the columns in ascending order, like 1970 Population, 1980 Population, 1990 Population,..... 2022 Population
# df = df.groupby('Continent')[df.columns[12:4:-1]].mean(numeric_only=True).sort_values(by='2022 Population', ascending=False)

# OR

# df = df.groupby('Continent')[df.columns[5:13][::-1]].mean(numeric_only=True).sort_values(by='2022 Population', ascending=False)

# OR

#  Just simply add ".sort_index()" on the "df3 = df2.transpose()", so that we don't have to manually rearrange the columns. 
# df.transpose().sort_index() 

# OR

# An easier way to reverse order of rows:
# df.transpose().loc[::-1] 

# This will display the columns in ascending order, like 2022 Population, 2020 Population, 2015 Population,..... 1970 Population
df2 = df.groupby('Continent')[df.columns[5:13]].mean(numeric_only=True).sort_values(by='2022 Population', ascending=False)

# To reverse. To change from column to row  & row to column
df2 = df2.transpose()
df.plot()

# Boxplot is very useful for Outliers - a number in the data set which is completely different from the dataset. This can be completely highest or loweset values

df.boxplot(figsize=(20,20))
plt.show()


# To look at the row which contains sepcific value in a particular column. Example in the following line we are looking at 'Continent' column which has 'Oceania' Values, it will display all the rows which has that value
df[df['Continent'].str.contains('Oceania')]

# To see columns & row of a particularly data type
df.select_dtypes(include='number')
df.select_dtypes(include='object')
df=df.select_dtypes(include='float')


print(df)