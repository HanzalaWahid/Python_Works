
# Import necessary libraries
import numpy as np
import pandas as pd
import json

# Define a list of grades data
data = [50, 50, 47, 97, 49, 3, 53, 42, 26, 74, 82, 62, 37, 15, 70, 27, 36, 35, 48, 52, 63, 64]

# Create a numpy array from the list
grades = np.array(data)

# Display the original data and the numpy array
print(data)
print(grades)

# Perform operations on the data and the numpy array
print(type(data), 'x 2:', data * 2)
print('---')
print(type(grades), 'x 2:', grades * 2)

# Explore attributes of the numpy array
print(grades.shape)
print(grades[0])
print(grades.mean())

# Define an array of study hours
study_hours = [10.0, 11.5, 9.0, 16.0, 9.25, 1.0, 11.5, 9.0, 8.5, 14.5, 15.5,
               13.75, 9.0, 8.0, 15.5, 8.0, 9.0, 6.0, 10.0, 12.0, 12.5, 12.0]

# Create a 2D array (an array of arrays)
student_data = np.array([study_hours, grades])

# Display the 2D array
print(student_data)

# Access elements of the 2D array
print(student_data[0][0])

# Calculate mean values of each sub-array
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

# Print mean study hours and mean grade
print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))

# Create a DataFrame using pandas
df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie',
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem', 'Helena', 'Ismat', 'Anila', 'Skye', 'Daniel', 'Aisha'],
                            'StudyHours': student_data[0],
                            'Grade': student_data[1]})

# Display the DataFrame
print(df_students)

# Access data using DataFrame's loc and iloc
print(df_students.loc[5])
print(df_students.loc[0:5])
print(df_students.iloc[0:5])
print(df_students.iloc[0, [1, 2]])
print(df_students.loc[0, 'Grade'])

# Filtering data based on conditions
print(df_students.loc[df_students['Name'] == 'Aisha'])
print(df_students[df_students['Name'] == 'Aisha'])

# Read data from a JSON file into a DataFrame
with open("data.json") as file:
    req = json.load(file)
df_students = pd.read_json('data.json')
print(df_students.head())

# Handling missing values
print(df_students.isnull())
print(df_students.isnull().sum())
print(df_students[df_students.isnull().any(axis=1)])

# Fill missing values with the mean of StudyHours
df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())
print(df_students)

# Drop rows with any missing values
df_students = df_students.dropna(axis=0, how='any')
print(df_students)

# Calculate mean study hours using column names
mean_study = df_students['StudyHours'].mean()
mean_grade = df_students.Grade.mean()
print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))

# Filtering and adding a new column based on a condition
passes = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

# Display the DataFrame with the new column
print(df_students)

# Grouping and aggregating data
print(df_students.groupby(df_students.Pass).Name.count())
print(df_students.groupby(df_students.Pass)[['StudyHours', 'Grade']].mean())

# Sorting the DataFrame by Grade in descending order
df_students = df_students.sort_values('Grade', ascending=False)

# Display the sorted DataFrame
print(df_students)
