import pandas as pd
import numpy as np

// load in data
diabetes_data = pd.read_csv('diabetes_data.csv')
print(diabetes_data.head())

// print number of columns
print(len(diabetes_data.columns))

// print number of rows
print(len(diabetes_data))

// find whether columns contain null values
print(diabetes_data.isnull().sum())

// perform summary statistics
print(diabetes_data.describe())  

// replace instances of 0 with NaN
diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']] = diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.NaN)

// find whether columns contain null values after replacements are made
print(diabetes_data.isnull().sum())

// print rows with missing values
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

// print data types using .info() method
print(diabetes_data.info())

// print unique values of Outcome column
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype('int64')
print(diabetes_data['Outcome'])







  
