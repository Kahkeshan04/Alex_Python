import pandas as pd

# To read the CSV file
pd.read_csv(r"D:\DA\Python\Reading Files in Pyton\countries of the world.csv")

# If there are no header or when we want to externally sepcify the headers

# The below code will assume that there are no headers as we specified "header = None", so in place of the header index value will be displayed
pd.read_csv(r"D:\DA\Python\Reading Files in Pyton\countries of the world.csv", header=None)

# The below code will use the name for headers which are mentioned "names = ['Countries','Region']" in the place of index values
# df is just a vairable which store the value, df(data frame)
df = pd.read_csv(r"D:\DA\Python\Reading Files in Pyton\countries of the world.csv", header=None, names=['Countries', 'Region'])

# To read the txt file.

# "sep" is used as the text file will not be usually formated correctly. In the text file whichever char is used seprate two the text will be place in "sep" parameter ex: sep = '\t
df = pd.read_csv(r"Python\Reading Files in Pyton\countries of the world.txt", sep = '\t')

# The proper way to read a txt file is using read_table where there is no need of "sep" parameter
df = pd.read_table(r"Python\Reading Files in Pyton\countries of the world.txt")

# Using read_table we can also read csv file but need the "sep" as csv are the comma seprated file so in "sep" parameter we should sepcify ',' -> sep=','
df = pd.read_table(r"Python\Reading Files in Pyton\countries of the world.csv", sep = ',')

# To read the json file.
df = pd.read_json(r"Python\Reading Files in Pyton\json_sample.json")

# To read the Excel file.

# The below code will read the very first sheet
df = pd.read_excel(r"D:\DA\Python\Reading Files in Pyton\world_population_excel_workbook.xlsx")

# The below code will read the sepcified sheet name
df = pd.read_excel(r"D:\DA\Python\Reading Files in Pyton\world_population_excel_workbook.xlsx", sheet_name='Sheet1')

# By default the output will display the first 5 and the last 5 rows. To get compelete rows in the output we can use 'set_option' function and pass the parameter of how many row we want to get displayed
pd.set_option('display.max.rows',235)

# For column
pd.set_option('display.max.columns',40)

# To get the information about the file. It will display the all the column and their data types, number of Null & Non-values values 
df.info()

# To get to know about the number of rows and columns. output - (234,4) rows - 234, columns - 4
df.shape

# By default it will dispaly first 5 values but we sepcify how many rows we want to see
df.head()
df.head(15)

# By default it will dispaly last 5 values but we sepcify how many rows we want to see
df.tail()
df.tail(15)

# To get a sepcific column, it will display all the values of that row
df['Rank']

# The following is used to see a sepcific row values of all columns
# In 'loc' we can sepcify index value or any row value
# loc = location (location of any value or string given in parameter)
df.loc[223]
df.loc['Uzbekistan']

# 'iloc' will only look into index values
# iloc = integer location (location of only integer) 
df.iloc[223]