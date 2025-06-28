import pandas as pd

df = pd.read_csv('students.csv')

def calculate_grade(marks):
    if marks >= 85:
        return 'A'
    elif marks >= 70:
        return 'B'
    elif marks >= 50:
        return 'C'
    else:
        return 'F'

df['Grade'] = df['Marks'].apply(calculate_grade)

df.to_csv('student_results.csv', index=False)
print("Grade sheet generated.")
