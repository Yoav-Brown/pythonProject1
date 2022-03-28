num1= int(input("please enter first number here: "))
num2= int(input("please enter second number here: "))
num3= int(input("please enter third number here: "))

if num1 > num2 and num1 > num3:
    print(num1)
if num2 > num1 and num2 > num3:
    print(num2)
if num3 > num2 and num3 > num1:
    print(num3)