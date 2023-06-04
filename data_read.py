import source_data
import os
import json
import pandas as pd


# create a file location and define it in a variable (source)
source_folder = source_data.source_folder

# create a file location and define it in a variable (destination)
destination_folder = source_data.destination_folder

os.chdir(source_folder)

df = pd.read_csv("BookingsReportingData.tsv", sep="\t")
print(df.head())
custom_fields = df[" Custom Fields"]
dCustom_fields = custom_fields.to_dict()
print(type(dCustom_fields))


"""
print(custom_fields)
print(type(custom_fields))

# cf_dictionary = custom_fields.to_dict()

print(len(custom_fields))
print(type(custom_fields))

for index in custom_fields:
    print(index)
"""
