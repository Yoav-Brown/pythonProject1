age= int(input('please enter your age here: '))
while 0<=age<=120:
    if 0<=age<=18:
        print('you are a child')
    if 19<=age<=60:
        print('you are an adult')
    if 61<=age<=120:
        print('you are a senior')
    age = int(input('please enter your age here: '))
print('*ERROR* invalid age')