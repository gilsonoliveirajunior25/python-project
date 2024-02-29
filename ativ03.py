nome = input('Digite seu nome: ')

salario_bruto = float (input('Digite o seu salario: '))
#desconto

ir = salario_bruto*0.08

INSS = salario_bruto*0.05

AC = salario_bruto*3



if salario_bruto>=3200:
    print(f'{nome} seu salario é tem acrescimo de 8% é {salario}: ')
    salario = salario_bruto-INSS-ir
    
elif salario_bruto<3200:
    print(f'{nome} seu salario é insento {salario}: ')
    salario = salario_bruto-INSS
    
elif salario_bruto<1500:
    print(f'{nome} seu salario tem acrescimo salario familia de +3% {salario} : ')
    salario = salario_bruto-INSS-AC
