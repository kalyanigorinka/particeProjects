
'''students information excel  format using pandas'''


import pandas as pd

# Sample array of student data

students_data = [
    {"Name": "Kalyani",    "Age": 20,   "Telugu": 80, "Hindi": 85, "Maths": 95, "Science": 88 , "percentage%":"87.0"},
    {"Name": "Deepika",    "Age": 20,   "Telugu": 70, "Hindi": 65, "Maths": 85, "Science": 48 , "percentage%":"67.0"},
    {"Name": "Bhavani",    "Age": 20,   "Telugu": 70, "Hindi": 45, "Maths": 75, "Science": 38 , "percentage%":"57.0"},
    {"Name": "Pavani",     "Age": 20,   "Telugu": 60, "Hindi": 65, "Maths": 75, "Science": 78 , "percentage%":"69.5"},
    {"Name": "Pravallika", "Age": 20,   "Telugu": 50, "Hindi": 55, "Maths": 85, "Science": 68 , "percentage%":"63.75"},
    {"Name": "Suma",       "Age": 20,   "Telugu": 80, "Hindi": 85, "Maths": 45, "Science": 48 , "percentage%":"64.5"},
    {"Name": "Raadha",     "Age": 20,   "Telugu": 40, "Hindi": 65, "Maths": 65, "Science": 58 , "percentage%":"57.0"},
    {"Name": "Jaya",       "Age": 20,   "Telugu": 90, "Hindi": 95, "Maths": 75, "Science": 58 , "percentage%":"79.5"},
    {"Name": "Madhavi",    "Age": 20,   "Telugu": 40, "Hindi": 35, "Maths": 45, "Science": 48 , "percentage%":"42.0"}
]
# Create a DataFrame from the array
df = pd.DataFrame(students_data)


# Define the file path where you want to save the .csv file
#file_path = "students.csv"

# Write the DataFrame to a .csv file
#df.to_csv(file_path, index=False)
df.to_csv("student_scores.csv", index=False)


print("CSV file generated successfully.")


# Create a sample DataFrame
data = {'Column1': [80, 85, 95, 88],
        'Column2': [70, 65, 85, 48],
        'Column3': [70, 45, 75, 38],
        'Column4': [60, 65, 75, 78],
        'Column5': [50, 55, 85, 65],
        'Column6': [80, 85, 45, 48],
        'Column7': [40, 65, 65, 58],
        'Column8': [90, 95, 75, 58],
        'Column9': [40, 35, 45, 48]
}
        
df = pd.DataFrame(data)

# Calculate the average of 'Column1'
average_column1 = df['Column1'].mean()

# Calculate the average of 'Column2'
average_column2 = df['Column2'].mean()

# Calculate the average of 'Column3'
average_column3 = df['Column3'].mean()

# Calculate the average of 'Column4'
average_column4 = df['Column4'].mean()

# Calculate the average of 'Column5'
average_column5 = df['Column5'].mean()

# Calculate the average of 'Column6'
average_column6 = df['Column6'].mean()

# Calculate the average of 'Column7'
average_column7 = df['Column7'].mean()

# Calculate the average of 'Column8'
average_column8 = df['Column8'].mean()

# Calculate the average of 'Column9'
average_column9 = df['Column9'].mean()



print(f"Average of Column1: {average_column1}")
print(f"Average of Column2: {average_column2}")
print(f"Average of Column3: {average_column3}")
print(f"Average of Column4: {average_column4}")
print(f"Average of Column5: {average_column5}")
print(f"Average of Column6: {average_column6}")
print(f"Average of Column7: {average_column7}")
print(f"Average of Column8: {average_column8}")
print(f"Average of Column9: {average_column9}")


# Calculate the average of each row (along columns)
average_per_row = df.mean(axis=1)
print("Average per row:")
print(average_per_row)

