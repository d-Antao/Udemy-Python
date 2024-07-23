import json


from exercisio23_a import EDD_FILE,Person,save


with open(EDD_FILE,'r',encoding='utf8') as file:
    persons = json.load(file)
    
    p1= Person(**persons[0])
    p2= Person(**persons[1])
    p3= Person(**persons[2])
    p4= Person(**persons[3])
    
print(p1.name)