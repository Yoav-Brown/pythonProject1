def items (a:dict):
    list1=[]
    for i in a:
        t1=i,a[i]
        list1.append(t1)
    return list1




dict1={1:10,2:20,3:30,4:40}
print(items(dict1))