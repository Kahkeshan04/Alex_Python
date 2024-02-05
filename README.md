# Python Data Analysis and Visualization

This repository contains Python scripts for various data analysis and visualization tasks. Below are detailed descriptions of each script:

## 1. File Sorting (File Transfer)

### Overview
The File Transfer script automates the organization of files based on their extensions into respective folders. It scans a directory for files, creates folders for each unique file extension, and moves files to their corresponding folders.

### Packages Used
os: For interacting with the operating system and file operations.
shutil: For high-level file operations such as moving files.

### Functionality
1. **File Discovery**: The script searches a specified directory for files.
2. **Folder Creation**: It creates folders for each unique file extension found.
3. **File Movement**: Files are moved to their respective folders based on their extensions.

## 2. Web Scraping

### Overview
The Web Scraping script extracts data from a Wikipedia page containing a list of the largest companies in a specific country. It utilizes BeautifulSoup to parse HTML and retrieve table data, which is then saved to a CSV file.

### Packages Used
requests: For making HTTP requests to retrieve web pages.
BeautifulSoup: For parsing HTML and extracting data from web pages.
pandas: For data manipulation and saving to CSV.

### Functionality
1. **HTTP Request**: The script sends an HTTP request to fetch the web page.
2. **HTML Parsing**: BeautifulSoup parses the HTML content to extract table data.
3. **Data Saving**: Extracted data is saved to a CSV file for further analysis.

## 3. Reading Files in Pandas

### Overview
The Reading Files in Pandas script demonstrates reading various file formats (CSV, TXT, JSON, Excel) into Pandas DataFrames. It covers different file reading methods, handling headers, and formatting data.

### Packages Used
pandas: For reading and manipulating data from different file formats.

### Functionality
1. **File Reading**: The script reads data from different file formats using Pandas.
2. **Header Handling**: It demonstrates reading files with and without headers and specifying custom column names.
3. **Data Formatting**: Various file reading methods and options for formatting data are showcased.

## 4. GroupBy

### Overview
The GroupBy script focuses on data analysis and grouping using Pandas. It demonstrates grouping data by specific columns and performing aggregate operations such as mean, count, min, max, and sum.

### Packages Used
pandas: For data manipulation and grouping operations.

### Functionality
1. **Grouping Data**: The script groups data by specified columns.
2. **Aggregate Operations**: It performs aggregate operations such as mean, count, min, max, and sum on grouped data.
3. **Statistical Analysis**: Grouped data with aggregate statistics is generated for further analysis.

## 5. Merging, Joining, and Concatenating

### Overview
The Merging, Joining, and Concatenating script demonstrates merging, joining, and concatenating dataframes using Pandas. It covers different types of joins (inner, outer, left, right, cross) and concatenation operations.

### Packages Used
pandas: For merging, joining, and concatenating dataframes.

### Functionality
1. **Data Combination**: The script combines multiple dataframes using merge, join, and concatenate operations.
2. **Join Types**: Different types of joins (inner, outer, left, right, cross) are illustrated.
3. **Data Integration**: Merged dataframes are generated based on specified operations and keys.

## 6. Pandas Visualization

### Overview
The Pandas Visualization script focuses on data visualization using Pandas, Seaborn, and Matplotlib. It covers various plotting techniques such as line plots, bar plots, scatter plots, box plots, histograms, and pie charts.

### Packages Used
pandas: For data manipulation and visualization.
seaborn: For statistical data visualization.
matplotlib.pyplot: For creating visualizations.

### Functionality
1. **Data Visualization**: The script utilizes Pandas, Seaborn, and Matplotlib for data visualization.
2. **Plotting Techniques**: Various plotting techniques are showcased, including line plots, bar plots, scatter plots, and more.
3. **Visualization Customization**: Options for customizing plot styles, labels, and other attributes are demonstrated.

## 7. Data Cleaning

### Overview
The Data Cleaning script demonstrates data cleaning and preprocessing techniques using Pandas. It covers tasks such as removing duplicates, handling missing values, formatting data, and categorizing data.

### Packages Used
pandas: For data cleaning and preprocessing.

### Functionality
1. **Data Cleaning**: The script performs various data cleaning tasks, including removing duplicates, handling missing values, and formatting data.
2. **Preprocessing**: Data preprocessing techniques such as formatting phone numbers, categorizing addresses, and handling categorical variables are showcased.

## 8. Exploratory Data Analysis (EDA)

### Overview
The Exploratory Data Analysis (EDA) script focuses on exploring and analyzing data using Pandas, Seaborn, and Matplotlib. It covers descriptive statistics, correlation analysis, grouping data, and various visualization techniques.

### Packages Used
pandas: For data manipulation and analysis.
seaborn: For statistical data visualization.
matplotlib.pyplot: For creating visualizations.

### Functionality
1. **Descriptive Statistics**: The script calculates descriptive statistics and explores data distributions.
2. **Correlation Analysis**: Correlation between variables is analyzed using a correlation heatmap.
3. **Data Visualization**: Various visualization techniques such as line plots, scatter plots, histograms, and box plots are used for data exploration.
