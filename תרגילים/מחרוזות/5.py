word= input('enter word: ')
letter= input('enter letter: ')
count=0
for i in word:
    if letter==i:
        count+=1
print(count)