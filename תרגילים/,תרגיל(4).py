name= input("please enter your name: ")
age= int(input("please enter your age: "))
year= int(input("please enter the current year: "))
fut= int(input("please enter a year in the future: "))
#the age in the future
x=(fut-year) +age

print(f"hi {name} you will be {x} years old in the year {fut}")