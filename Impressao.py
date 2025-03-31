import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

color = os.system('color 4')

def main():
    
    color
    os.system('cls')
    print('\n')
    print('======================')
    print('Impressão de Arquivos ')
    print('======================')
    print('\n')
    print('1 - Imprimir arquivo')
    print('2 - Sair')
    print('\n')
    op = int(input('Selecione a opção desejada: '))
    os.system('cls')
    
    if op == 1:
        
        imprimir()
    
    elif op == 2:
        
        os.system('cls')
        print('\nSaindo...\n')
        os.system('pause')
        os.system('cls')
        
    else:
        
        os.system('cls')
        print('\nOpção inválida!\n')
        os.system('pause')
        os.system('cls')
        main()
        
 
def imprimir():
    
    color
    print('\nSelecione o arquivo: ')
    Tk().withdraw()
    filename = askopenfilename()

    os.system('cls')
    print(f'\nArquivo selecionado: {filename}\n')
    os.system('pause')
    os.system('cls')

    print('\n1 - Impressora Norte')
    print('2 - Impressora Sul\n')

    imp = int(input('Selecione a impressora: '))

    os.system('cls')

    if imp == 1:
        
        os.system('print /d:"\\\curfpfs01\RICOH_Lado_Norte" "{}"'.format(filename))
        os.system('pause')
        main()

    elif imp == 2:
        
        os.system('print /d:"\\\curfpfs01\RICOH_Lado_Sul" "{}"'.format(filename))
        os.system('pause')
        main()
        
    else:
        
        print('\nOpção inválida!\n')
        os.system('pause')
        os.system('cls')
        imprimir()

main()