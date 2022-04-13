def findlist (a:list, num,start=0):
    for i in a[start:]:
        if i== num:
            return a[start:].index(i) +start
list1=[1,3,5,6,3,6,734,234,64,234,3,23]
num1=int(input('enter number: '))
startpoint=int(input('enter where you want the search to begin: '))
print(findlist(list1,num1,startpoint))