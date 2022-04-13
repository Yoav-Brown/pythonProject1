from random import randint

num1= randint(1,100)
num2= randint(1,100)
print(num1,num2)
print(f"whole number:{num1//num2}\n "
      f"decimal: {num1/num2}\n"
      f"only leftover: {num1%num2}")