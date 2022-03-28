num= int(input('enter three digit number: '))

while 99<num<1000:
    first= num%10
    second=num//10%10
    third= num//100%10
    print(first+second+third)
    num = int(input('enter three digit number: '))

print('*ERROR* invalid number')