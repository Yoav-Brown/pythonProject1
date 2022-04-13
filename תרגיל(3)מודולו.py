num= int(input("please enter three digit number here: "))
first= num%10
second= num//10%10
third= num//100%10

print(f'{first}{second}{third}')