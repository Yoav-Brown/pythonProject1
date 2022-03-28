from random import *
first='_'
second='_'
third='_'

x= randint(1,5)
if x==1:
    x= 'was'
    one = 'w'
    two = 'a'
    three = 's'
elif x==2:
    x='run'
    one='r'
    two='u'
    three='n'
elif x==3:
    x='big'
    one = 'b'
    two = 'i'
    three = 'g'
elif x==4:
    x='had'
    one = 'h'
    two = 'a'
    three = 'd'
else:
    x='ace'
    one = 'a'
    two = 'c'
    three = 'e'
print(x)

guess= input('guess a letter: ')

while guess in x:
    if guess == one:
        first=guess
        print(first, second ,third)
        guess = input('guess a letter: ')

