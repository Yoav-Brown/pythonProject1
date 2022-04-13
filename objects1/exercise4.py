class circle:
    pi=3.14
    def __init__(self,radius:int):
        self.radius=radius
    def area (self):
        return (self.radius*self.pi*self.radius)

    def circumference (self):
        return (2*self.radius*self.pi)

radius1=int(input('enter radius: '))
circle1=circle(radius1)
print('area',circle1.area())
print('circumference',circle1.circumference())