num=int(input('enter number: '))
high=0
while num!=0:
    if num>high:
        high=num
    num = int(input('enter number: '))

if high==0:
    print('all your numbers where below 0')
else:
    print('the highest number is', high)