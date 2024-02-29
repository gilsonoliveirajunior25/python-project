distancia = int(input('Digite a distancia da sua Viagem: ')) 
consumo = int (input('Digite o consumo do seu Veiculo: '))
preço = float(input('Digite o preço do Combustivel: '))


resultado = round((distancia/consumo)*preço,2)

print(f'valor para essa Viagem sera de R$ {resultado}')

