d1={10: 10, 2: 20, 30: 33, 4: 40, 5: 55}
for i in d1:
    if i%10==0:
        d1[i]*=2
print(d1)