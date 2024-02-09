import numpy as np
import pandas as pd
import json

# Define the grades list
data = [50, 50, 47, 97, 49, 3, 53, 42, 26, 74, 82, 62, 37, 15, 70, 27, 36, 35, 48, 52, 63, 64]
print("Original Grades Data:")
print(data)

# Create a NumPy array from the grades list
grades = np.array(data)
print("\nNumPy Array from Grades:")
print(grades)

# Show the type of the original list and the NumPy array multiplied by 2
print('\nType of original list x 2:', type(data), 'x 2:', data * 2)
print('---')
print('\nType of NumPy array x 2:', type(grades), 'x 2:', grades * 2)

# Display the shape, first element, and mean of the grades array
print('\nShape of Grades Array:', grades.shape)
print('First Element of Grades Array:', grades[0])
print('Mean of Grades Array:', grades.mean())

# Define an array of study hours
study_hours = [10.0, 11.5, 9.0, 16.0, 9.25, 1.0, 11.5, 9.0, 8.5, 14.5, 15.5,
               13.75, 9.0, 8.0, 15.5, 8.0, 9.0, 6.0, 10.0, 12.0, 12.5, 12.0]

# Create a 2D array (an array of arrays) combining study hours and grades
student_data = np.array([study_hours, grades])

# Display the 2D array
print("\nStudent Data Array:")
print(student_data)

# Show the first element of the first element in the 2D array
print('\nFirst Element of the First Element in 2D Array:', student_data[0][0])

# Calculate the mean value of study hours and grades
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

# Display the average study hours and grade
print('\nAverage Study Hours: {:.2f}\nAverage Grade: {:.2f}'.format(avg_study, avg_grade))

# Create a DataFrame using pandas with student data
df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie',
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours': student_data[0],
                            'Grade': student_data[1]})

# Display the DataFrame
print("\nStudent DataFrame:")
print(df_students)

# Get data for the student with index 5
print("\nData for Student at Index 5:")
print(df_students.loc[5])

# Get rows with index values from 0 to 5
print("\nRows with Index Values from 0 to 5:")
print(df_students.loc[0:5])

# Get data in the first five rows
print("\nData in the First Five Rows:")
print(df_students.iloc[0:5])

# Access and print specific elements in the DataFrame
print("\nSpecific Elements in the DataFrame:")
print(df_students.iloc[0, [1, 2]])
print(df_students.loc[0, 'Grade'])
print(df_students.loc[df_students['Name'] == 'Aisha'])
print(df_students[df_students['Name'] == 'Aisha'])
print(df_students.query('Name=="Aisha"'))
print(df_students[df_students.Name == 'Aisha'])

# Load data from a JSON file (assumed "data.json" exists in the current working directory)
with open("data.json") as file:
    req = json.load(file)
    print("\nData Loaded from JSON File:")
    print(req)

# Load data from a CSV file (assumed "grades.csv" exists in the current working directory)
df_students = pd.read_json('data.json')
print("\nData Loaded from json File:")
print(df_students.head())
print("\nNull Values in DataFrame:")
print(df_students.isnull())
print("\nSum of Null Values in Each Column:")
print(df_students.isnull().sum())
print("\nRows with Any Null Values:")
print(df_students[df_students.isnull().any(axis=1)])

# Fill missing values in the StudyHours column with the mean value
df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())

# Drop rows with any missing values
df_students = df_students.dropna(axis=0, how='any')

# Calculate the mean study hours and grade
mean_study = df_students['StudyHours'].mean()
mean_grade = df_students.Grade.mean()

# Display the mean study hours and grade
print('\nMean Study Hours: {:.2f}\nMean Grade: {:.2f}'.format(mean_study, mean_grade))

# Get students who studied for the mean or more hours
print("\nStudents Who Studied for Mean")
