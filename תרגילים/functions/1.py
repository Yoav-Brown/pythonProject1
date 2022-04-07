def sumdig(a, b, c, ):
    sum = a + b + c
    return sum


num=int(input('enter 3 digit number: '))
A=num%10
B=num//10%10
C=num//100
print(sumdig(A,B,C))