#nome = input('Digite o seu nome:').strip().capitalize()


#if nome.startswith('G'):
   #print('seu Nome começa com G')
#else:
    #print('seu nome não começa com G')
    
import os

nomes = []


for x in range(5):
    nome = input('Digite o seus nome: ').strip().capitalize()
    nomes.append(nome)

for nome in nomes:
    if nome.startswith('F'):
      print(f'Seus nomes com letra F são: ',nome)

