from random import randint
x = [int(input('enter numer here, if you want tostop enter 0: '))]
while x[-1]!=0:
  x+= [int(input('enter numer here, if you want tostop enter 0: '))]
del x[-1]
print( f'{max(x)}, {min(x)}, {sum(x)/len(x)} '  )
print(x)


