# for loop 
# Input the heights
student_heights = input("Ener the heights of students").split()

for n in range (0,len(student_heights)):

    student_heights[n] = int(student_heights[n])
    #print(student_heights)
   
    # Find average = total height of students /number of students

    total = 0
    count_no_students = 0 

    for student_height in student_heights:
        total += int(student_height) 
        count_no_students +=1 


print("Average:",round(total/count_no_students))
print("Total:", count_no_students)



