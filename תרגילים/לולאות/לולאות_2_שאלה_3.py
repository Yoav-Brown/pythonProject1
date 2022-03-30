num= int(input('eneter number:' ))
sumdigit=0
while num!=0:
    sumdigit+=num%10
    num=num//10
print(sumdigit)