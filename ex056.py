somamedia = 0
media = 0
hmv = ''
ihmv = 0
m = 0
for p in range(1, 5):
    print('-----------------Pesoa numero {} -----------------'.format(p))
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[F/M]: ')).upper()
    if sexo == 'M' and idade > ihmv :
        hmv = nome
        ihmv = idade
    else:
        if sexo == 'F' and  idade < 20:
            m += 1

    somamedia += idade
    media = somamedia / p
print('A media de idade do grupo é {}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(ihmv, hmv))
print('Ao todo sao {} mulheres com menos de 20 anos'. format(m))