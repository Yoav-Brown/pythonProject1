def maximum(a:list):
    max1=0
    for i in a:
        if i>max1:
            max1=i
    return max1
list1=[1,24,243,42,4342,134231,13131213131,1,344,4,2,4122,413422124123212,31,342,123]
print(maximum(list1))