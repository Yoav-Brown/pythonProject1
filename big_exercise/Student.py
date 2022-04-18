class Student:
    def __init__(self, id:int, name, age:int, ):
        self.id=id
        self.name=name
        self.age=age
        self.grades={}

    def add_grade(self,subject,grade:int):
        self.grades[subject]=grade

    def __repr__(self):
        return f'{self.id},{self.name},{self.age},{self.grades}'

    def calc_factor(self,subject,percentage:int):
        self.grades[subject]+=(percentage/100)*self.grades[subject]
        if self.grades[subject]>100:
            self.grades[subject]=100

    def average(self):
        avg=sum(self.grades.values())/len(self.grades)
        return avg


    def __eq__(self, other):
        if self.id==other.id:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.age>other.age:
           return True
        else:
            return False

if __name__=="__main__":

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