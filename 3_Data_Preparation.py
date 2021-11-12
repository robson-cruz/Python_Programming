##->Data Preparation
#
## import library
import pandas as pd

## Extract and Read Data With Pandas
df = pd.read_csv('./data/zoo.csv', header=0, sep=',')           ## Load dataset

print(df)                                                       ## Print out the data set

# Tip: If you have a large CSV file, you can use the head() function to only show the top 5 rows:
print(df.head())

# Remove NA values
# axis=0 means that we want to remove all rows that have a NaN value:
df.dropna(axis=0, inplace=True)
print(df)

## List the data types within our data set
print(df.info())

### Analyze the Data
print(df.describe())