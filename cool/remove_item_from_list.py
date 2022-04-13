def removevalue(a:list, removed):
    if removed in a:
        deleted = 0
        for i in range(len(a)):
            if (i-deleted)< len(a):
                if a[i-deleted]== removed:
                    del a[i-deleted]
                    deleted+=1
                    # return
            else:
                return
    else:
        return print('item not in list')

num1=int(input('enter what you want removed: '))
list1=[1,23,45,54,23,234,23,3224,3545342]
removevalue(list1,num1)
print(list1)