def listable (a):
    list1=[]
    if type(a) is int:
        return print('not listable')
    else:
        for i in  a:
            list1.append(i)
        return list1, type(list1)

t1=(5,2,5,123,5345,2)
str1='dfgrtbs'
dict1={4:'df',7:'23','dfg':43,34:24,}
set1={2,34,5,6,43,2}
int1=3
print(listable(t1))
print(listable(set1))
print(listable(str1))
print(listable(dict1))
print(listable(int1))
