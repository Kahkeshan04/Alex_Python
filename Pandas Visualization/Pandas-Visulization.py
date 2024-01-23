import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt 

#Reading CSV file
df = pd.read_csv(r'Python\Pandas Visualization\Ice Cream Ratings.csv')

# Setting the index
df = df.set_index('Date')

# To see what different styles are avaible in the 'matplotlib'
print(plt.style.available)

# To chose different style for the charts
plt.style.use('tableau-colorblind10')

# To visualize anything in python we use plot(). By default it will be a line plot. THe following will the graph of all three columns
df.plot()

# To get a sperate graph for every individual column we can use 'subplots' parameter
df.plot(subplots=True)

# To add the Title to the Graph
df.plot(title='Ice Cream Ratings')

# To customize the label for X & Y axis
df.plot(title='Ice Cream Ratings', xlabel='Daily Ratings', ylabel='Scores')

# To can specify any other plot we use "kind" parameter and specify which kind of plot we want
df.plot(kind='bar')
df.plot(kind='bar', stacked=True)

# To specify the particular column for visualization
df['Flavor Rating'].plot(kind='bar', stacked=True)

# For Horizontal Bar chart
df.plot.barh(stacked = True)

# Scatter Plot: Only scatter() will give an error we need to specify X & Y axis
df.plot.scatter(x='Texture Rating', y='Overall Rating')

# To increase the size of the dots on the scatter plot use 's' (size)
df.plot.scatter(x='Texture Rating', y='Overall Rating', s=500)

# To change the color of the dots in scatter plot
df.plot.scatter(x='Texture Rating', y='Overall Rating', s=100, c='green')

# Histogram: They are best for distribution of the varibles
df.plot.hist()

# We can specify the size of the bar using 'bins'. By default bins size is 10. Bins represent how much a bar can spread on the chart. For Size 's=1' only one bar will be represented. For 's=5' only 5 bar will be represented. The distribution get smaller as the Size.
df.plot.hist(bins=50)

# Box Plot
df.boxplot()

# Area Plot
df.plot.area()

# FigSize in Area Plot. It just increase the size of the chart. figsize=(horizontal or length or xaxis size , vertical or breadth or yaxis size)
df.plot.area(figsize = (20,5))

# Pie Chart: 'pie()' will give error. We need to specify what column we're working with. We can not custmoize color in pie chart
df.plot.pie(y='Flavor Rating')


# The following command displays the plot in a separate window in VS
plt.show()