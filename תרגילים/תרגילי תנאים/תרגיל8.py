num1= int(input("please enter a double digit number here: "))
first= num1//10
second= num1%10


if 0<(num1//10)<=10:
    if num1%7==0 or (first==7 or second==7):
        print('lucky number!!!')
    else:
        print('this is not a lucky number')
else:
    print('*ERROR* this is not a double digit number')
