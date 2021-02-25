import pandas
import numpy
import geojson

## first, clean up the sample data file ##
# read in the file for cleaning
with open('sampleData.csv', 'r') as file_original:
    file_data = file_original.read()

# label first column
file_data = file_data.replace(',outcome,', 'id,outcome,')

# remove malformed lines
file_data = file_data.replace(',,,,\n', '')

# write out the cleaned data to a new file
with open ('sampleDataClean.csv', 'w') as file_new:
    file_new.write(file_data)


## use pandas to reorganize csv and add random data for other diseases ##
# read in sample data csv
df_sample_data = pandas.read_csv('sampleDataClean.csv')

# rename columns
df_sample_data.rename(columns = {'outcome':'sero', 'X':'long', 'Y':'lat'}, inplace = True)

# reorder columns
df_final_data = df_sample_data[['age', 'long', 'lat', 'sero']]

# fill new seroprevalence columns with random data
#df_final_data['seroB'] = numpy.random.randint(0,2, size=len(df_final_data))
#df_final_data['seroC'] = numpy.random.randint(0,2, size=len(df_final_data))

# print for visual confirmation, then save out to new file
print(df_final_data)
df_final_data.to_csv('seroData.csv')

# function to export the pandas dataframe to geojson
def data2geojson(df):
    features = []
    insert_features = lambda X: features.append(
        geojson.Feature(geometry=geojson.Point((X["long"],
                                                X["lat"])),
            properties=dict(id=X["id"],
                            age=X["age"],
                            sero=X["sero"])))
    df.apply(insert_features, axis=1)
    with open('seroData.geojson', 'w', encoding='utf8') as fp:
        geojson.dump(geojson.FeatureCollection(features), fp, sort_keys=True, ensure_ascii=False)

data2geojson(df_final_data)