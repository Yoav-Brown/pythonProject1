from random import *
username=input('enter username: ')
password=''
for i in range(6):
    password+=choice(username)
print(password)
