class person:
    def __init__(self,name:str,age:int,numchilds:int):
        self.name=name
        self.age=age
        self.numchilds=numchilds

    def show (self):
        print(f'{self.name},{self.age},{self.numchilds}')

    def haschildren(self):
        if self.numchilds>0:
            return True
        else:
            return False

    def agegroup(self):
        if 0<=self.age<=18:
            return 'Child'
        elif 19<=self.age<=60:
            return 'Adult'
        else:
            return 'Senior'

