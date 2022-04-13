num= int(input('enter number here: '))

for i in range(2,num):
    if num%i==0:
        print('your number is a composite number')
        break
else:
    print('your number is a prime number')