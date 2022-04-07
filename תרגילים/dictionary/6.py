d1={10: 10, 2: 20, 30: 33, 4: 40, 5: 55}
key1=int(input('enter key: '))

if key1 in d1:
    del d1[key1]
print(d1)