nome = str(input('Digite seu nome: '))
salario = float(input('Digite seu salario fixo: '))
vendas = float(input('Digite a quantidade de vendas no mês em dinheiro:'))


comissao = 15/100 * vendas
valor = comissao + salario
print(f'Olá {nome} \n Sua comissao total foi de R$ {valor}')
    