num1= int(input("please entera three digit number number here: "))
third= num1%10
second= num1//10%10
first= num1//100%10
sum= first+second+third


#print(first,second,third,sum)
if 99<num1<1000:
    print(sum)
else: print("\nERROR the number you have entered is not a three digit number")