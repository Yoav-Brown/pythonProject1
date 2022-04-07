list1=[1,2,3,4,5,6,7,8,9,10]
reverse3= list1[-1:-4:-1]
print(reverse3)
print(list1[1::2])
odd= list1[0::2]
print(odd)
# a= int(input('enter first number: '))
# b= int(input('enter second number: '))
# c= int(input('enter third number: '))

# list1[3:5]=[a,b,c]
# print(list1)
list2=list1.copy()
for i in range(len(list2)):
    list2[i]*=2
print(list2)
list3=[]
list3.append(list1[0])
list3.append(list1[9])
print(list3)