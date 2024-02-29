import os

num1 = int(input('Digite o primeiro numero: '))
os.system('cls')
num2 = int(input('Digite o segundo numero: '))
os.system('cls')
op = input(('Digite a operação desejada(+,-,*,/):'))
os.system('cls')

if op=="+":
    resultado=num1+num2
elif op=="-":
    resultado=num1-num2
elif op=="*":
    resultado=num1*num2
elif op=="/":
    if (num1!=0)and(num2!=0):
        resultado=num1/num2
    else:
        resultado = "valor impossivel!"
else:
    resultado = "opção incorreta!"
print(f'O resultado é {resultado}') 