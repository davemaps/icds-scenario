import pandas
import numpy

# read in data
df = pandas.read_csv('seroData.csv')

df2 = df[['Age']]

hist = df2.hist()
print(hist)