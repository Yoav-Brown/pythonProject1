sentence= input('enter sentence: ')
word=input('enter word: ')
indexes=''
listsentence=sentence.split(' ')
for i in range (len(listsentence)):
    if listsentence[i] == word:
        indexes+= str(i)+ ','


print(indexes)