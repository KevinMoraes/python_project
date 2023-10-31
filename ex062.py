n1 = int(input('Digite i termo inicial: '))
n2 = int(input('Digite quanto em quanto vai pular: '))
cont = 0
n = 10
contatermo = 0
while  cont < n:
    print('{}'.format(n1), end=' ')
    cont += 1
    n1 += n2
    contatermo += 1
rep = 2
while rep != 0:
    rep = int(input('\nQuantos termos você quer mostrar a mais?: '))
    cont = 0
    while cont < rep :
        print('{}'.format(n1), end=' ')
        cont += 1
        n1 += n2
        contatermo += 1
print('Progressâo finalizada com {} termos'.format(contatermo))
