def countlist(a:list, num):
    count1=0
    for i in a:
        if i==num:
            count1+=1
    return count1
list1=[1,435,64,2435,1,45356,7545,2355441,1,3452,31,41,14,1,313,1,54]
num=int(input('enter number: '))
print(countlist(list1,num))