from Student import Student
from Course import Course

course_num=int(input('enter course num here: '))
course_name=input('enter course name here: ')
course_max_students=int(input('enter the max amount of students allowed in this course here: '))
course1=Course(course_num,course_name,course_max_students)

subject=input('enter a subject (if you finished entering subjects enter 0): ')
teacher=input(f'enter the teacher for {subject}: ')
while (subject or teacher)!=str(0):
    course1.subjects[subject]=teacher
    subject = input('enter a subject (if you finished entering subjects enter 0): ')
    if subject==str(0):
        break
    teacher = input(f'enter the teacher for {subject}: ')

list_of_student_id=[]
student_id=1
for i in range(course1.max_students):
    student_id = int(input('enter a student id (if you wish to stop enter 0): '))
    if student_id!=0:
        list_of_student_id.append(student_id)
    else:
        break
print(list_of_student_id)

for i in list_of_student_id:
    student_name= input(f'enter the student name for id {i}: ')
    student_age=int(input(f"enter {student_name}'s age: "))
    new_student=Student(i,student_name,student_age)
    for i in course1.subjects:
        grade=int(input(f"enter {student_name}'s grade for {i}: "))
        new_student.grades[i]=grade
    print(new_student)
    if course1.add_student(new_student)== False:
         break


print(course1)
