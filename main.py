import pandas as pd

# code that loads the dataset
file_path = '/Users/sagedrewke/Downloads/outbreaks.csv'
data = pd.read_csv(file_path)

# displays the first observations in the dataset
print("Original Data:")
print(data.head())



# to handle missing values, replaces them with median of the column
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())

# replace missing variables with mode of the column
categorical_cols = data.select_dtypes(include=['object']).columns
data[categorical_cols] = data[categorical_cols].apply(lambda x: x.fillna(x.mode()[0]))

# case for handling duplicates

# this will identify / remove any duplicate records
data = data.drop_duplicates()

# this is for the case of handling inconsistencies

# this will standerdize the 'Status' column in order to have consistent capitalization
data[ 'Status' ] = data[ 'Status' ].str.capitalize()

# this will standardize the state names ( assuming all of them should be in title case )
data[ 'State' ] = data[ 'State' ].str.title()

# this is for the normalization case ( if needed )

# this is going to normalize the column names to lowercase
data.columns = data.columns.str.lower()

# this will display the now cleaned dataset
print( "\nCleaned Data:" )
print( data.head() )

# this will save the cleaned dataset to a brand new CSV file
cleaned_file_path = '/path/to/save/cleaned_outbreaks.csv'  # this will update the path to the actual save location
data.to_csv( cleaned_file_path, index = False )

print( f"\nCleaned dataset saved to: { cleaned_file_path }" )
