def fillstudents(liststudent:list,numstudents:int):
    for i in range(numstudents):
        scores=int(input(f'enter {i+1} score: '))
        liststudent.append(scores)
    return liststudent
num=int(input('enter number of students: '))
listscores=[]

print(fillstudents(listscores,num))
