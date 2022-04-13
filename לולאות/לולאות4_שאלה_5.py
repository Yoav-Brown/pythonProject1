count=0
place=0
high=0
for i in range(7):
    num = int(input('enter number: '))
    count+=1
    if num>high:
        high=num
        place=count

print(f'the highest number is {high} and its place was {place}')