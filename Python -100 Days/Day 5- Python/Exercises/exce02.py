# student scores 

student_marks = input("Enter student marks?").split()
print(student_marks)

for n in range(0,len(student_marks)):
    student_marks[n] = int(student_marks[n])

# find highest marks of students
max_marks = student_marks[0]
for student_mark in student_marks:
    if student_mark > max_marks:
        max_marks = student_mark
print(f"My Name is Amit and scored {max_marks}")


