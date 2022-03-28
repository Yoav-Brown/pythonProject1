day= int(input("please enter day number here: "))
if 1>day or day>31:
    print('*ERROR* invalid day')
else:
    month= int(input("please enter month number here: "))
    if 1>month or month>12:
        print('*ERROR* invalid month')
    else:
        year= int(input("please enter year number here: "))
        if 1950>year or year>2020:
            print('*ERROR* invalid year')
        else:

            second = year%10
            first= year//10%10



            if day < 10:
                    day = '0' + str(day)
            if month < 10:
                    month = '0' + str(month)
            print(f'{day}/{month}/{first}{second}')


