import pandas as pd

df = pd.read_excel(r"D:\DA\Python\Data Cleaning\Customer Call List.xlsx")

# To remove duplicate
df = df.drop_duplicates()

# To drop the specific column
df = df.drop(columns = "Not_Useful_Column")

# Mention column name so that the effect of the function will be restricted to only that particular column. 'lstrip' take from the Left side & 'rstrip' take from the Right side. By default it will remove only white spaces'strip()'. 
df["Last_Name"].str.strip()

pd.set_option('display.max.columns',10)

# We need to specify the value we want to take out
df["Last_Name"] = df["Last_Name"].str.strip(".../_")
# or Method - 2
df["Last_Name"]= df["Last_Name"].str.replace("[./_]","" ,regex= True)

# 'replace('[^a-zA-Z0-9]','')' The function will try to match or catch everything except these charater metioned as regex, and then it will replace those value (the values which are not '^a-zA-Z0-9') with a blank - From tutorial 
df['Phone_Number'] = df['Phone_Number'].astype(str).str.replace('[^a-zA-Z0-9]', '', regex=True)

# To format the number correctly. Adding '-' in between. We need to make sure that the values are in string format inorder to add '-'
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: str(x))
df['Phone_Number'] = df['Phone_Number'].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

# To remove 'Nan'
df['Phone_Number'] = df['Phone_Number'].str.replace('nan--','')
df['Phone_Number'] = df['Phone_Number'].str.replace('Na--','')

# To categrozie the Address
df[['Street_Address','State','Zip_Code']] = df['Address'].str.split(',', n=2, expand=True)

# To make the column values similar. We are changing all the Yes & No to Y & N of the columns - 'Paying Customer' & 'Do_Not_Contact'
df['Paying Customer'] = df['Paying Customer'].str.replace('Yes', 'Y') 
df['Paying Customer'] = df['Paying Customer'].str.replace('No', 'N') 

df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('Yes', 'Y') 
df['Do_Not_Contact'] = df['Do_Not_Contact'].str.replace('No', 'N') 

# Method - 2, but with this method fillna() is not working for N/a
df[['Paying Customer','Do_Not_Contact']] = df[['Paying Customer','Do_Not_Contact']].replace({'Y': 'Yes', 'N': 'No'}, regex=False)

# Fill Null Values : To get rid of Nan & N/a all together.
df = df.fillna('')

# To remove the rows where the people sepecifical mentioned not to call i.e., Rows which have values as 'Y' in 'Do_Not_Contact' column and also the blank vlaues of 'Phone_Number'
# In the following line we are looking at each index values
for x in df.index:
    # In the following line we are looking at the values of the sepcified column at each index. 
    # loc->location, 
    # x-> index value from the 'for loop'
    # Do_Not_Contact -> Column name in which the changes has to be made
    if df.loc[x, 'Do_Not_Contact'] == 'Y' or df.loc[x, 'Phone_Number'] == '':
        # The following line will remove all the row where the condition is satisfied
        df.drop(x, inplace= True)

# Other way of deleting the whole row where the vlaue in a specific column is empty
# df = df.dropna(subset=['Phone_Number'], inplace=True)

# Method - 2
# Remove rows where 'Do_Not_Contact' is 'Y'
df = df[df['Do_Not_Contact'] != 'Yes']

# Remove rows where 'Phone_Number' is empty
df = df[df['Phone_Number'] != '']


# To set the index values right. 
df = df.reset_index(drop=True)

# Check data type
# print("Data type of 'Phone_Number' column:", df['Phone_Number'].dtype)

# print(df)