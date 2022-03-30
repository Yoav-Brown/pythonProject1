score= int(input('enter score: '))
high=0
sum=0
low=100
count=0
while 0<=score<=100:
    count+=1
    sum+=score
    if score>high:
        high=score
    if score<low:
        low=score
    score = int(input('enter score: '))
print(f'the highest score is: {high} \nthe difference between lowest score and highest is {high-low}\nand the average of the socres is {sum/count}')