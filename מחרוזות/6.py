word=input('enter word: ')
lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i  in lower:
    if i== word[0]:
        word=upper[lower.index(i)]+word[1:]
        break
print(word)
