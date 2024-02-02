import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Francis']
scores = [random.randint(0, 100) for _ in range(6)]

#students_scores = { name:random.randint(0, 100)  for name in names }
#approved_students = { name: score for (name, score) in students_scores.items() if score >= 60}
#print(approved_students)

import pandas

print(scores)
students_df = pandas.DataFrame({ 'student': names, 'score': scores })
print(students_df)

for (index, row) in students_df.iterrows():
    print(f"{index}: {row.student} => {row.score}")