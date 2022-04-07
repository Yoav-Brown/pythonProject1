word=input('enter word: ')
letter= input('enter letter: ')
count=0

for i in word:
    if letter==i:
        print(count)
        break
    else:
        count+=1
else:
        print('-1')
