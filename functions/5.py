def sum_to_num (a):
    sum=0
    for i in range (a+1):
        sum+=i
    return sum

for i in range (1,6):
    num=int(input(f'enter {i} number: '))
    print(sum_to_num(num))