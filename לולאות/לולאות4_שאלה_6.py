num = int(input('enter number: '))
hisnum=num
count=0
inverted=0
x=0
while num>0:
    count+=1
    num=num//10

for i in range(count,0,-1):
    inverted+=((hisnum//10**(i-1))%10)*10**x
    x+=1
print(f'here is the inversion of your number {inverted}\nand here is your number inverted and doubled {inverted*2}')