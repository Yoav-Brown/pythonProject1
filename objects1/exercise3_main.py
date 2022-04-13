from exercise3_class import *
name1=input('enter your name: ')
age1=int(input('enter your age: '))
child1=int(input('enter the number of children you have: '))
person1= person(name1,age1,child1)
person1.show()
if person1.haschildren():
    print('you have children')
else:
    print('you do not have children.')
print(person1.agegroup())