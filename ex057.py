sexo = str(input('Digite o seu sexo[F/M]: ')).strip().upper()[0]
while sexo not in 'FfMm':
    print('Dados inválidos!')
    sexo = str(input('Digite o seu sexo[F/M]: '))
print('O Dado {} foi registrado com sucesso!'.format(sexo))
'''f = m = 0
c = ''
while c != 'F' and c != 'M':
    c = str(input('Digite seu sexo[F/M]: ')).upper()
    if c != 'F' and c != 'M':
        print('Valor incorreto!')
print('Fim')'''