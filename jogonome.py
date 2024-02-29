import os
import random


def principal():   
    nomes = ['Gilson' ,'Sued' ,'Leo' ,'Levi' ,'Mateus' ,'Fabio' ,'Amanda' ,'Emerson']
        
    print('Bem vindo ao jogo da adivinhação de Nomes')
    print('Tente adivinhar um nome')
    
    while True:
        palpite = input('Digite o nome: ').strip().capitalize()
        os.system('cls')
    
        if verificarnome(palpite, nomes):
           print('Parabéns você acertou o nome!!')
           break
           
        else:
           print('esse nome não existe, tente novamente:')
           
        
        
        
def verificarnome(palpite,nomes):
    
    if palpite in nomes:
        return True
    else:
        return False              


principal()