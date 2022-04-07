word=input('enter word:')
new=''
for i in word:
    if i not in new:
        if word.count(i)>1:
            new+=i
print(new)