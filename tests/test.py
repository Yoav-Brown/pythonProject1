hisnum=12345
count=5
inverted=0
x=0
for i in range(count,0,-1):
    inverted+=((hisnum//10**(i-1))%10)*10**x
    x+=1
print (inverted)