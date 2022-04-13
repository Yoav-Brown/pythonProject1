from random import randint
#
# list1=[]
# for i in range(10):
#     list1.append(randint(1,100))
# print(list1)

# list2= [1,2,3,4,5,6,7,8,9,10]
# list3= list2[-3:]
# print(list3)
# for i in range(len(list2)):
#     print(list2[-1-i], end=' ')
# print(end='\n')
#8========================================================================================
# list2[6:9]=[int(input('enter number: '))]
# print(list2)
#10========================================================================================
# removed=[]
# for i in list2:
#     if i%3==0:
#         print(i, end=',')
#     else:
#         removed.append(i)
# print(removed)
#11========================================================================================
# list4=[1,1]
# for i in range(10):
#     list4.append(sum(list4))
# print(list4)
#13========================================================================================
# listrand=[]
# for i in range(20):
#     listrand.append(randint(1,100))
# print(listrand)
# x=int(input('enter the number you want removed: '))
# while x in listrand:
#     listrand.remove(x)
# print(listrand)
#14========================================================================================
# y=int(input('enter number: '))
# divlist=[]
# for i in range (1,y+1):
#     if y%i==0:
#         print(i,end=',')
#15========================================================================================
# z=int(input('enter number: '))
# fib=[1,1]
# for i in range(2,z+2):
#     fib.append(sum(fib[i-2:i]))
# print(fib)
# 16========================================================================================
# list5=[]
# list6=[]
# e= int(input('enter number of items in list: '))
# for i in range (e):
#     list5.append(randint(1,5))
# print(list5)
# list6=list5.copy()
# for i in list5:
#     if i in list6[list6.index(i)+1:]:
#         list6.remove(i)
# print(list6)
#17========================================================================================
# list7=[]
# list8=[]
# t=int(input('enter number for first list when finished enter 0: '))
# while t!=0:
#     list7.append(t)
#     t = int(input('enter number for first list when finished enter 0: '))
# r=int(input('enter number for second list when finished enter 0: '))
# while r!=0:
#     list8.append(r)
#     r = int(input('enter number for second list when finished enter 0 : '))
# print(list7)
# print(list8)
# for i in list7:
#     if i in list8:
#         print('they have a common member')
#         break
# else:
#     print('they do not have a common member')
#20========================================================================================
list9=[]
count=0
for i in range(5):
    list9.append(randint(1,100))
print(list9)
p= int(input('enter number: '))

if p in list9:
    for i in list9:
        if i==p:
            print('your number\'s index is', count )
        else:
            count+=1
else:
    print('number not in list')
