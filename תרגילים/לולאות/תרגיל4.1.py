num1=int(input('enter first number: '))
num2=int(input('enter second number: '))

if num1%2==0:
    for i in range(num1,num2+1,2):
        print(i)
else:
    for i in range(num1+1,num2+1,2):
        print(i)