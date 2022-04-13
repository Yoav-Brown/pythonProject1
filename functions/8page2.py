def values (a:dict):
    list1=[]
    for i in a:
        list1.append(a[i])
    return list1




dict1={1:10,2:20,3:30,4:40}
print(values(dict1))