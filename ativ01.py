funcionario = "marcio"

salario_bruto = 9876
#desconto

IR = salario_bruto*0.08
INSS = salario_bruto*0.05
Plano= 150


salario = salario_bruto-IR-INSS-Plano


print(funcionario, "seu salario final é de:", salario )