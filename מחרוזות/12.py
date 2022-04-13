sentence=input('enter sentence: ')
listsentence=list(sentence)
listsentence[0]=listsentence[0].upper()
for i in range(len(listsentence)):
    if listsentence[i]==' ':
        listsentence[i+1]=str(listsentence[i+1]).upper()

newsentence=''
for i in listsentence:
    newsentence+=i
print(str(newsentence))