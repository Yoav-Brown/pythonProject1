set1={1,2,3,4,5,6,7,8,9}
set2={1,2,3,4,9,56,34}
set3=set()
set3.update(set2)
set3.update(set1)
print(type(set3))
print(set3)
print(set3.pop())
print('max',max(set3))
print('min',min(set3))
print('length',len(set3))
set4=set()
set4.update(set3)
set4.add(3241231231)
set4.add(324122)
set4.add(3332)
print(set4)