def age_classification (a):
    if 0<=a<=18:
        return 'child'
    elif 19<=a<=60:
        return 'adult'
    elif 61<=a<=120:
        return 'senior'
for i in range (5):
    age=int(input('enter age: '))
    age_classification(age)
    print(age_classification(age))