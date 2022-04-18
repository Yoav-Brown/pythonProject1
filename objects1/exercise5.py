class hardisk:

    def __init__(self,used_space:int,num_documents:int):
        self.space=100
        self.used_space=used_space
        self.num_documents=num_documents

    def __str__(self):
        return f'{self.space},{self.used_space},{self.num_documents}'

    def free_space(self):
        return self.space-self.used_space

    def add_file(self,file_size):
        if file_size<= self.free_space():
            self.used_space+= file_size
            self.num_documents+=1
            return True
        else:
            return False

    def del_file(self,file_size):
        self.used_space-=file_size
        if self.used_space<0:
            self.used_space=0
        self.num_documents-=1

hardisk1=hardisk(0,0)

file_sizes=int(input('enter designated added file size: '))

for i in range(5):
    if hardisk1.add_file(file_sizes):
        pass
    else:
        break
    file_sizes = int(input('enter designated added file size: '))
print(hardisk1)
file_sizes=int(input('enter designated deleted file size: '))
hardisk1.del_file(file_sizes)

print(hardisk1)