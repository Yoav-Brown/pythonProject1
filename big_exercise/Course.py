from Student import Student

class Course:
    def __init__(self,num:int, name, max_students:int=10):
        self.num=num
        self.name=name
        self.subjects={}
        self.students=[]
        self.max_students=max_students


    def __repr__(self):
        return f'{self.num},{self.name}\n' \
               f'{self.subjects}\n' \
               f'{self.students},max students= {self.max_students}'

    def add_student(self,student:Student):
        if len(self.students)<self.max_students:
            self.students.append(student)
            return True
        else:
            return False

    def add_factor(self,subject,factor):
        for i in self.students:
            if subject in i.grades:
                i.calc_factor(subject,factor)
            else:
                pass
    def del_student(self,student:Student):
        if student in self.students:
            QA.students.remove(student)
        else:
            print('student is not in this course')



    def averages(self):
        averages = []
        for i in self.students:
            avg_student= i.average()
            averages.append(avg_student)
        return averages

    def weak_students(self):
        list_avgs=self.averages()
        lowest_grade=min(list_avgs)
        num_weak_students=list_avgs.count(lowest_grade)
        if num_weak_students > 1:
            indexes=[]
            # takes all the indexes of the lowest students and puts them in a list "indexes"
            for i in range(num_weak_students):
                indexes.append(list_avgs.index(lowest_grade))
                list_avgs[list_avgs.index(lowest_grade)]='taken'
            return indexes
        else:
            return list_avgs.index(lowest_grade)




if __name__=="__main__":

    student1=Student(111,"yoav",21)
    student1.add_grade('sql',80)
    student1.add_grade('csharp',60)
    student1.add_grade('java',45)
    student1.add_grade('python',90)

    student2=Student(222,"ido",24)
    student2.add_grade('sql',60)
    student2.add_grade('csharp',32)
    student2.add_grade('java',78)
    student2.add_grade('python',56)

    student3=Student(333,"tomer",15)
    student3.add_grade('sql',60)
    student3.add_grade('csharp',32)
    student3.add_grade('java',78)
    student3.add_grade('python',56)

    student4=Student(444,"jack",45)
    student4.add_grade('sql',56)
    student4.add_grade('csharp',67)
    student4.add_grade('java',90)
    student4.add_grade('python',100)

    QA=Course(101,"QA", 5)
    QA.subjects={'sql':'dave','csharp':'leo','java':'michal','python':'orly'}
    # print(QA)

    QA.add_student(student1)
    QA.add_student(student2)
    QA.add_student(student3)
    QA.add_student(student4)
    print(QA)


    # QA.add_factor("sql",50)
    # print(QA)


    # QA.del_student(student1)
    # print(QA)

    print(QA.averages())

    print(QA.weak_students())



    # QA.add_student('yoav')
    # QA.add_student("dan")
    # print(QA.add_student("lily"))
    # print(QA.add_student("gil"))
    # print(QA)
