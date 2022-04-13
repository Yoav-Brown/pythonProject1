class student:
    def __init__(self,id:int, name:str, grade:int ):
        self.id= id
        self.name= name
        self.grade= grade

    def checkpass (self):
        if self.grade>=70:
            return True
        else:
            return False


    def updategrade (self, factor):
        updated_grade=self.grade+(self.grade*factor/100)
        if updated_grade<=100:
            self.grade=updated_grade
        else:
            self.grade= 100

    def show (self):
        print(f'{self.id} {self.name}, {self.grade}')

id1=input('enter student id: ')
name1=input('enter student name: ')
grade1=int(input('enter student grade: '))

student1= student(id1,name1,grade1)
if student1.checkpass():
    print('you passed!!!')
else:
    print('you failed!!!')
percentage= int(input('enter the factor in percentages: '))
student1.updategrade(percentage)
student1.show()