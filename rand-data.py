# fill csv with random data for seroprevalence for two other diseases

import pandas
import numpy

df = pandas.read_csv('sampleData.csv', index_col='id')

df['ser2'] = numpy.random.randint(0,2, size=len(df))
df['ser3'] = numpy.random.randint(0,2, size=len(df))

print(df)
df.to_csv('serData.csv')