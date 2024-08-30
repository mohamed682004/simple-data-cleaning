import pandas as pd
import numpy as np
#import sklearn as sk

# Load the data
missy_data = pd.read_csv('/home/omran-xy/Workspace/MAIM/P1 clean/unclean_data.csv', encoding='latin1')

print(missy_data)

# Remove duplicates
cleaner_data = missy_data.drop_duplicates()
print(cleaner_data)

# Automatically get the mean of any numeric column that has missing values
columns_with_missing_data = cleaner_data.columns[cleaner_data.isna().any()]
print("Columns with missing data:", columns_with_missing_data)

# This line is for Python to identify that column as int not string
cleaner_data['DIRECTOR_facebook_likes'] = pd.to_numeric(cleaner_data['DIRECTOR_facebook_likes'].str.replace('"', '', regex=False), errors='coerce')
cleaner_data['DIRECTOR_facebook_likes'] = cleaner_data['DIRECTOR_facebook_likes'].fillna(0).astype(int)

# Calculate means of columns with missing data
means_of_missing_data_columns = cleaner_data[columns_with_missing_data].mean()
print("Means of columns with missing data:\n", means_of_missing_data_columns)

# For this line we used apply to use lambda little fun identifier to work with this DataFrame
cleaner_data[columns_with_missing_data] = cleaner_data[columns_with_missing_data].apply(
    lambda col: col.fillna(col.mean()) if col.name in columns_with_missing_data else col
)

# Receiving our precious clean data
cleaner_data.to_csv('/home/omran-xy/Workspace/MAIM/P1 clean/cleaned_data.csv', index=False)
