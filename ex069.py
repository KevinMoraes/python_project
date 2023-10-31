idade = 0
sexo = ''
r = 't'
maior = homem = mulher = 0
while r not in 'Nn':
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
print(f'Total de pessoas maiorres de 18 anos : {maior}')
print(f'Total de homens cadastrados : {homem}')
print(f'Total de mulheres com menos de 20 anos : {mulher}')