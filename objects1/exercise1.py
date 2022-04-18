class course:
    def __init__(self,num,name,applicants:int,max_applicants:int):
        self.num=num
        self.name=name
        self.applicants=applicants
        self.max_applicants=max_applicants

    def __str__(self):
        return f'{self.num},{self.name},{self.applicants},{self.max_applicants}'

    def open_spots(self):
        return self.max_applicants-self.applicants

    def add_applicants(self,amount):
        if amount<=self.open_spots():
            self.applicants+= amount
            return self.applicants
        else:
            print('sorry there are not enough spots in the course for the requested amount')

course1=course(123,'math',5,10)
print(course1)
course1.add_applicants(6)
course1.add_applicants(4)
print(course1)