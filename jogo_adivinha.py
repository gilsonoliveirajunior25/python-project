import os
import random

nsorteado = random.randint(1,100)

while True:
    palpite = int(input('Digite um número entre 1 e 100: '))
    os.system('cls')
    
    if palpite == nsorteado:
        print(f"Parabéns !! você acertou Miserável!!:{nsorteado}")
        break        
    elif palpite<nsorteado:
         print('Digite um numero maior !!')
    else:
         print('Digite um numero menor!!')
