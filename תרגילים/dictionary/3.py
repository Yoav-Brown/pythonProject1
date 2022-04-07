num=int(input('enter number: '))
dictionary1={}
i=0
add={i:i*i}
for i in range(1,num+1):
    dictionary1[i]=i*i
print(dictionary1)