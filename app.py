import os
import json
import shutil
from datetime import date
import source_data

print(os.getcwd())
today = date.today()

# create a file location and define it in a variable (source) 
source_folder = source_data.source_folder

# create a file location and define it in a variable (destination) 
destination_folder = source_data.destination_folder

#change to the source file
os.chdir(source_folder)

#check the new location
print(os.getcwd())

#list all the files
source_files = (os.listdir(source_folder))

#split the file name and ext type
for file in source_files:
  file_name, file_ext = os.path.splitext(file)
  if file_ext == '.tsv':
    shutil.move(file, destination_folder)


os.chdir(destination_folder)
print(os.getcwd())
destination_files = (os.listdir(destination_folder))
for destination_file in destination_files:
  d_file_name, d_file_ext = os.path.splitext(destination_file)
  if d_file_ext == '.tsv':
    new_file =  os.rename(destination_file, d_file_name + '_' + str(today) + '.csv')