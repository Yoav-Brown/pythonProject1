x = []
y=[]
for i in range (1,6):
    x+=[int(input(f'enter the {i} number here: '))]
print(f'here is your first list', x)

for i in range(5):
    y+=[int(input(f'enter the {i} number here: '))]
print('here is your second list', y)
x+=y

print('here are your lists combined', x, 'and the length of the list is', len(x))