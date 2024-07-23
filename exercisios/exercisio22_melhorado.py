import os

def list(tasks):
    print()
    if not tasks:
        print('any task for list')
        print()
        return
    
    print('tasks: ')
    for task in tasks:
        print(f'\t{task}')
    print()
    
def undo(tasks,tasks_undo):
    print()
    if not tasks:
        print('any task for undo')
        print()
        return
    
    task = tasks.pop()
    tasks_undo.append(task)
    print()

def redo(tasks,tasks_undo):
    print()
    if not tasks_undo:
        print('any task for redo')
        print()
        return
    
    task = tasks_undo.pop()
    tasks.append(task)
    print()

def add(task,tasks):
    print()
    task = task.strip()
    tasks.append(task)
    print()
    

tasks = []
tasks_undo = []

while True :
    print('Comands : list , undo ,redo')
    task = input('write one task or comand: ')
    
    comands ={
        'list': lambda :list(tasks),
        'undo': lambda :undo(tasks,tasks_undo),
        'redo': lambda :redo(tasks,tasks_undo),
        'clear':lambda: os.system('cls'),
        'add':lambda: add(task,tasks)
    }
    comands = comands.get(task) if comands.get(task) is not None else comands['add']
    comands()
    
    #com o dicionario comands diminuinos o numero de condicionais oque clarifica e melhora a logica do programa.
    
    
    
    """
    if task == 'list':
        list(tasks)
        continue
       
    elif task == 'undo':
        undo(tasks,tasks_undo)
        list(tasks)
        continue
    
    elif task == 'redo':
        redo(tasks,tasks_undo)
        list(tasks)
        continue
    
    elif task =='clear':
        os.system('cls')
        continue
    
    else:
         add(task,tasks)
         list(tasks)
         continue
    """