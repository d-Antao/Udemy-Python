import os
import json

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
 
 
def read(tasks,edd_arq):
    data = []
    try:
        with open(edd_arq,'r',encoding='utf8') as arq:
            data = json.load(arq)
            
    except FileNotFoundError:
        print('Arq not found')
        save(tasks,edd_arq)
    return data
    
       
def save(tasks,edd_arq):
    dados = tasks
    with open(edd_arq,'w',encoding='utf8') as arq:
            dados = json.dump(tasks, arq, indent=2, ensure_ascii=False)
    return dados

EDD_ARQ = 'exercisio22_melh.json'
tasks = read([],EDD_ARQ)
tasks_undo = []

while True :
    print('Comands : list , undo ,redo')
    task = input('write one task or comand: ')
    
    comands ={
        'list': lambda :list(tasks),
        'undo': lambda :undo(tasks,tasks_undo),
        'redo': lambda :redo(tasks,tasks_undo),
        'clear':lambda: os.system('clear'),
        'add':lambda: add(task,tasks)
    }
    
    comand = comands.get(task) if comands.get(task) is not None else \
        comands['add']
    comand()
    save(tasks,EDD_ARQ)
