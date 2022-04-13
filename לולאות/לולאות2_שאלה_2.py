# password= input('please enter password: ')
# passtest= input('please reenter password: ')
#
# if passtest != password:
#     for i in range(4):
#         if passtest != password:
#             print('you did not enter properly, please try again: ')
#             password = input('please enter password: ')
#             passtest = input('please reenter password: ')
#         else:
#             print('your password has been registered')
#             break
#
#     else: print('too many tries!!!!')
# else:
#     print('your password has been registered')
#
# [print('===============================================================')
password= input('please enter password: ')
passtest= input('please enter verification password: ')
count=0
while password!=passtest:
    count+=1
    if count<5:
        passtest = input('please enter verification password: ')
    else:
        print('too many tries')
        break
else:
    print('your password has been registered')