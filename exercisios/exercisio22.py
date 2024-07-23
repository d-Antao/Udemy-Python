

# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
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
    
    
