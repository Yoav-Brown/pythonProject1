x=[]
passed=[]
failed=[]
for i in range (1,6):
    x += [int(input(f'enter the {i} grade here: '))]
print(x)
for i in x:
    if i>=60:
        passed.append(i)
    else:
        failed.append(i)
print(f'passed {passed} \n failed {failed}')