Tempo = float(input('Digite o tempo: '))
Velocidade = float(input('Digite a velocidade média durante a viagem: '))
litros = float(input('Digite quantos litros foram gastos: '))

distancia = Velocidade * Tempo
Km = distancia / 12
print(f'A distância percorrida foi de: {distancia}, km/h e a quantidade de litros é: {Km:_.3f}L')
