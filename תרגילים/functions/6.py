def betweennumbers (a,b):
    if a<b:
        for i in range(a,b+1):
            print(i,end=' ')
    else:
        for i in range(b, a + 1):
            print(i, end=' ')



num1=int(input('enter first number: '))
num2=int(input('enter second number: '))
betweennumbers(num1,num2)