import os


nome = input('Digite o seu Nome: ')
os.system('clear')
peso =  int(input('Digite o seu peso: '))
os.system('clear')
altura = float(input('Digite a sua altura: '))
os.system('clear')
imc = round(peso/(altura*altura),2)



#Estrutura de condição

if imc<=15 and 18.5 :
    print(f'{nome} o valor do seu IMC é: {imc:.2f} sua situação abaixo do peso !')
        
elif imc>=18.6 and imc<24.9:
    print(f'{nome} o valor do seu IMC é: {imc:.2f} sua situação uma pessoa normal !')
    
elif imc>=25 and imc<=29.9:
    print(f'{nome} o valor do seu IMC é: {imc:.2f} sua situação esta acima do peso !')
elif imc>=29.9 and imc<=34.9:
    print(f'{nome} o valor do seu IMC é: {imc:.2f} sua situação é pessoa obesidade Grau 1 !')
    
else: 
    print(f'{nome} o valor do seu IMC é: {imc:.2f} sua situação uma pessoa obesidade Grau 2 !')
    