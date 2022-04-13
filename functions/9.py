def pass_grade (a):
 if 70<=a<=100:
     return True
 else:
     return False



for i in range (5):
    grade= int(input('enter grade: '))
    if pass_grade(grade) :
        print('this is a passing grade')
    else:
        print('this is not a passing grade ')
