tot = alto = menor = maior = cont =  0
nome = ' '
while True:
    prod = str(input('Nome do produto: '))
    preco = float(input('Preço:R$ '))
    r = ' '
    cont += 1
    if preco > 0 :
        tot += preco
    if preco > 1000:
        alto += 1
    if cont == 1:
        maior = menor = preco
    if menor > preco:
        menor = preco
        nome = prod
    while r not in 'SN':
        r = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'O valor total da compra é R${tot}')
print(f'Temos {alto} produto(s) com o valor acima de R$1000')
print(f'Produto mais barato foi {nome} que custa {menor}')
print('Acabou')