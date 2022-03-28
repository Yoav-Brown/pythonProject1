num1= int(input("please enter first number here: "))
num2= int(input("please enter second number here: "))
sum = num1+num2

print(num1,num2,sum)
if sum!=0:
    if sum%2==0:
        print("even number")
    else:
        print('odd number')
else:
    print('number is 0')