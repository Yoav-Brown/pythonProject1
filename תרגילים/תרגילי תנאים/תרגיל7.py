score= int(input("please enter first number here: "))

if 0<=score<=100:
    if score>=70:
        print('you passed!!!')
    else:
        print('you failed :( ')
else:
    print('ERROR the number you have entered is not an eligible score ')
