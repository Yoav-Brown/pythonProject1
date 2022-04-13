from math import ceil
num=int(input('enter number: '))
while -9>num or num >9:
    if num<0:
        num = ceil(num/10)
    else:
        num=num//10
print(num)