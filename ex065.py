r = 'S'
cont = media = soma = n = maior = menor = 0
while r != 'N':
    n = int(input('Digite um valor: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
    r = str(input('Quer continuar?[S/N]: ')).upper()
media = soma/ cont
print('Voce digitou {} números e a media entre eles foi {}'.format(cont, media))
print('O menor valor foi {} e o maior foi {}'.format(menor, maior))