import pandas as pd

# Load the dataset
file_path = '/path/to/your/outbreaks.csv'  # Update this path to your actual file location
data = pd.read_csv( file_path )

# Display the first few rows of the dataset to understand its structure
print( "Original Data:" )
print( data.head() )

# Handling Missing Values

# Fill missing numeric values with the median of the column
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())

# Fill missing categorical values with the mode of the column
categorical_cols = data.select_dtypes(include=['object']).columns
data[categorical_cols] = data[categorical_cols].apply(lambda x: x.fillna(x.mode()[0]))

# Handling Duplicates

# Identify and remove duplicate records
data = data.drop_duplicates()

# Handling Inconsistencies

# Standardize the 'Status' column to have consistent capitalization
data['Status'] = data['Status'].str.capitalize()

# Standardize state names (assuming all should be in title case)
data['State'] = data['State'].str.title()

# Normalization (if necessary)

# Normalize the column names to lowercase
data.columns = data.columns.str.lower()

# Display the cleaned dataset
print("\nCleaned Data:")
print(data.head())

# Save the cleaned dataset to a new CSV file
cleaned_file_path = '/path/to/save/cleaned_outbreaks.csv'  # Update this path to your actual save location
data.to_csv(cleaned_file_path, index=False)

print(f"\nCleaned dataset saved to: {cleaned_file_path}")


