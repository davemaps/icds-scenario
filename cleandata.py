import pandas
import numpy


## First, clean up the sample data file ##
# read in the file for cleaning
with open('sampleData.csv', 'r') as file_original:
    file_data = file_original.read()

# remove malformed lines
file_data = file_data.replace(',,,,\n', '')

# write out the cleaned data to a new file
with open ('sampleDataClean.csv', 'w') as file_new:
    file_new.write(file_data)


## Use Pandas to reorganize csv and add random data for other diseases ##
# read in sample data csv
df_sample_data = pandas.read_csv('sampleDataClean.csv')

# rename columns
df_sample_data.rename(columns = {'outcome':'A Seroprevalence', 'age':'Age', 'X':'Longitude', 'Y':'Latitude'}, inplace = True)

# reorder columns
df_final_data = df_sample_data[['Age', 'Longitude', 'Latitude', 'A Seroprevalence']]

# fill new seroprevalence columns with random data
df_final_data['B Seroprevalence'] = numpy.random.randint(0,2, size=len(df_final_data))
df_final_data['C Seroprevalence'] = numpy.random.randint(0,2, size=len(df_final_data))

# print for visual confirmation, then save out to new file
print(df_final_data)
df_final_data.to_csv('seroData.csv')