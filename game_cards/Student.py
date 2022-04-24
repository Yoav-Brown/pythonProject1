class Student:
    def __init__(self, id:int, name, age:int, ):
        if type(id)!=int:
            raise TypeError('Id must be an integer')
        if type(name)!=str:
            raise TypeError('name must be string')
        if type(age)!=int:
            raise TypeError('age must be an integer')
        if age<0 or age>120:
            self.age=0
        else:
            self.age=age

        self.id=id
        self.name=name
        self.grades={}


    def add_grade(self,subject,grade:int):
        if type(subject) != str:
            raise TypeError('subject must be string')
        if type(grade)!=int:
            raise TypeError('grade must be an integer')

        self.grades[subject]=grade


    def __repr__(self):
        return f'{self.id},{self.name},{self.age},{self.grades}'


    def calc_factor(self,subject,percentage:int):
        if type(subject) != str:
            raise TypeError('subject must be string')
        if type(percentage)!=int:
            raise TypeError('percentage must be an integer')

        self.grades[subject]+=(percentage/100)*self.grades[subject]
        if self.grades[subject]>100:
            self.grades[subject]=100


    def average(self):
        # dont divide by zero
        if len(self.grades)!=0:
            avg=sum(self.grades.values())/len(self.grades)
            return avg
        else:
            print("this student does not have any grades")
            return False

    def __eq__(self, other):
        if type(other)!=Student:
            return False
        if self.id==other.id:
            return True
        else:
            return False

    def __gt__(self, other):
        if type(other)!=Student:
            raise TypeError('you can not compare these items because they are not the same type')

        if self.age>other.age:
           return True
        else:
            return False

if __name__=="__main__":
    # student_invalid_id=Student('asd','sdf',21)


    student1=Student(123,"yoav",21)
    student1.add_grade('sql',80)
    student1.add_grade('csharp',60)
    student1.add_grade('java',45)
    student1.add_grade('python',90)

    student2=Student(1234,"ido",24)
    student2.add_grade('sql',80)
    student2.add_grade('csharp',60)
    student2.add_grade('java',45)
    student2.add_grade('python',90)

    print(student1>student2)
    #
    # print(student1)
    # student1.calc_factor("sql",50)
    # print(student1)
    print(student1.average())