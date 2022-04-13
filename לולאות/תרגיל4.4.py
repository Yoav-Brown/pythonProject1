from random import randint
numguess= 0
num= int(input('enter your number between 1 and 100: '))
while num<0 or num>100:
    print('invalid number')
    num = int(input('enter your number between 1 and 100: '))
guess= randint(1,100)
while num!=guess:
    if guess> num:
        guess-=1
        numguess+=1
    else:
        guess+= 1
        numguess+=1

print('your number was' ,guess)
print('it took me', numguess ,'guesses')