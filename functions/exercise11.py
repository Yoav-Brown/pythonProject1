from random import randint
def fill (a:list):
    for i in range (20):
        a.append(randint(1,100))
    return
def countnum (a: list, num):
    return a.count(num)
lis1=[]
fill(lis1)
print(lis1)
num1=int(input('enter number: '))
print(countnum(lis1,num1))