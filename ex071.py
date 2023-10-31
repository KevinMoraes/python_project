valor = 1
while valor != 0:
    valor = int(input('Digite o valor: '))
    tot50 = tot20 = tot10 = tot1 = 0
    if valor > 50:
        while valor > 50:
            valor = valor - 50
            tot50 += 1
    if valor > 20:
        while valor > 20:
            valor = valor - 20
            tot20 += 1
    if valor > 10:
        while valor > 10:
            valor = valor - 10
            tot10 += 1
    if valor > 0:
        while valor > 0:
            valor = valor - 1
            tot1 += 1
if tot50 != 0:
    print(f'{tot50} notas de R$50,00')
if tot20 != 0:
    print(f'{tot20} notas de R$20,00')
if tot10 != 0:
    print(f'{tot10} notas de R$10,00')
if tot1 != 0:
    print(f'{tot1} notas de R$1,00')
print('-' * 20)
print('Volte sempre ao BANCO DO BRABU')
