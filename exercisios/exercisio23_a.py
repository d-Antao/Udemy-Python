import json


EDD_FILE = 'exercisio23.json'

class Person:
    def __init__(self,name,age) :
        self.name = name
        self.age = age
        
p1 = Person(name='Isabel',age= 38)
p2 = Person(name='Filipa', age= 23)
p3 = Person(name='Antão' , age=24)
p4 = Person(name='Miguel',age=48)

dataBase = [p1.__dict__,vars(p2),vars(p3),p4.__dict__]

#print(*dataBase)

def save(edd,dataBase):
    with open(edd,'w',encoding='utf8') as file :
        json.dump(dataBase,file,ensure_ascii=False,indent=2)
        
if __name__ == '__main__':
    print('este e o main')
    save(EDD_FILE,dataBase)