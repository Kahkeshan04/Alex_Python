import pandas as pd

df = pd.read_csv(r'D:\DA\Python\GroupBy\Flavors.csv')

group_by_frame = df.groupby('Base Flavor')

pd.set_option('display.max.columns',9)

# To get mean of all of the columns that has integers
# '.mean()' used to work properly but now 'numeric_only = True' should be added in '.mean'
group_by_frame.mean(numeric_only = True)

# To get mean of all aggregate function
group_by_frame.mean(numeric_only = True)

# To get the COUNT in each column after grouping
group_by_frame.count()

# To get the MIN & MAX values

# In the following example for 'Chocolate - Base Flavour' - 'Chocolate' - 'C' has the minimum value and for 'Vanilla - Base Flavour' - 'Cake Batter' - 'C' has the minimum value.
# It will display the MIN or MAX value of each column irrespective to the row 
group_by_frame.min()
group_by_frame.max()

# The SUM function as the name goes it SumUp the values of all the columns respectively
# It works with or without 'numeric_only = True'. If parameter is provided then it will SumUp all the numeric values else it will also SumUp alphabetic values
group_by_frame.sum()
group_by_frame.sum(numeric_only = True)

# To perform all the Aggregate functions on the particular column at once
group_by_frame.agg({'Flavor Rating':['mean','max','count','sum']})

# To perform all the Aggregate functions on multiple columns at once
group_by_frame.agg({'Flavor Rating':['mean','max','count','sum'], 'Texture Rating':['mean','max','count','sum']})

# Till now we grouped only one column ('Base Flavor), but now we can group multiple column
df.groupby(['Base Flavor','Liked']).mean(numeric_only = True)

# To perform all the Aggregate functions on multiple columns Goruped together at once
df.groupby(['Base Flavor','Liked']).agg({'Flavor Rating':['mean','max','count','sum']})

# To preform all the Aggregate function on all the columns. In this we will get all the aggregate function like - count, mean, standard deviation (std), min, 25%....75%, max. 
gf = group_by_frame.describe()

# Display the result
print(gf)
