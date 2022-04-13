from random import randint

num= randint(1,9)

guess=int(input('please guess a number between 1 and 9: '))

while num!= guess:
    if 1<=guess<=9:
        if num>guess:
            print('your number is lower than mine')
            guess = int(input('please guess a number between 1 and 9: '))
        else:
            print('your number is higher than mine')
            guess = int(input('please guess a number between 1 and 9: '))
    else:
        print('invalid number')
        guess = int(input('please guess a number between 1 and 9: '))

print("congradulation you have guessed correctly!!!")
