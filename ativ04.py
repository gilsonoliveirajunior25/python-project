import os
import random
 

def jogo_adivinhacao():
    numero_secreto = random.randint(i, 100)
    tentativas = 0
    
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 100.")
    
    while True:
        palpite = int(input("Digite seu palpite: "))
        
        tentativas +=1
        
        if (palpite < numero_secreto):
            print("Seu palpite é muito baixo. Tente novamente.")
        
        elif (palpite > numero_secreto):
            print("Seu palpie é muito alto. Tente novamente:")
            
        else:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
            