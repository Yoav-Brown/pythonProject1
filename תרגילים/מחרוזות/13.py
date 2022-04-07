sentence=input('enter sentence: ')
letter=input('enter letter: ')
listsentence=list(sentence)
for i in range(len(sentence)):
    if sentence[i]==letter:
        listsentence[i]=listsentence[i].upper()


newsentence = ''
for i in listsentence:
    newsentence += i
print(newsentence)