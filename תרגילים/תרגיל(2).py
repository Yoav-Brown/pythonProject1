day= int(input("please enter a day: "))
month= int(input("please enter a month: "))
year= int(input("please enter the current year: "))

first_year = year%10
second_year = year//10%10
print(f'{day}/{month}/{second_year}{first_year}')