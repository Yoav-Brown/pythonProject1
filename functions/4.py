def sum_to_num (a):
    sum=0
    for i in range (a+1):
        sum+=i
    return sum



num=int(input('enter number: '))
print(sum_to_num(num))