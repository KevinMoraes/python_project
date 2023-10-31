km = float(input('Digite a distancia da viagem em Km: '))
preço = 0
if km <= 200:
    preço = km * 0.50
    print('Sua viagem é de curta distância, saindo com o preço de R${}'.format(preço))
else:
    preço = km * 0.45
    print('Sua viagem é de longa distância, saindo com o preço de R${}'.format(preço))
