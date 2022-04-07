from random import randint
list1=[]
for i in range(10):
    list1+= [randint(1,100)]
print(list1)
list1=tuple(list1)
num=input('enter number: ')
list1+=int(num),
print(list1)
tup2=list1[:4],list1[-4:]
print(tup2)
tup2=list1[1:]
print(tup2)