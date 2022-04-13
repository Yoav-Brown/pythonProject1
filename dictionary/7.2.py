d1={1:10,2:20}
x=int(input('enter key: '))
for i in d1:
    if x == i:
        print('its here')
        break
else:
    print('its not here')