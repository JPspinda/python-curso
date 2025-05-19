import os

def print_lista(lista):
    for itens in lista:
        print(itens)

lista = []
produto = []

while True:
    print('\nComandos: listar, desfazer, refazer')
    tarefa_comando = input('Digite um comando ou uma tarefa: ')
    
    if tarefa_comando.lower() == 'listar':
        print('\nTAREFAS: ')
        print_lista(lista)
        
    elif tarefa_comando.lower() == 'desfazer':
        produto = [i for i in lista]
        del lista[-1]
    
    elif tarefa_comando.lower() == 'refazer':
        lista.append(produto[-1])
        
    elif tarefa_comando.lower() == 'sair':
        break
        
    elif tarefa_comando.lower() == 'clear':
        os.system('cls')    
        
    else:
        lista.append(tarefa_comando)    
