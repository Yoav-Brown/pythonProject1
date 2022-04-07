word1=input('enter first word: ')
word2=input('enter second word: ')
new=''
for i in word1:
    if i not in new:
        if i in word2:
            new+=i
print(len(new))

