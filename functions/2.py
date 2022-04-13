def legal_num(a):
    if 99 < a < 1000:
        return True
    else:
        return False


num=int(input('enter 3 digit number: '))
print(legal_num(num))