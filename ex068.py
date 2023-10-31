import random
cont = 0
while True:
    j = int(input('Digite um valor: '))
    pi = str(input('Par ou Inpar?[P/I}: ')).strip().upper()[0]
    while pi not in 'PI':
        pi = str(input('Par ou Inpar?[P/I}: ')).strip().upper()[0]

    pc = random.randint(0,10)
    soma = j + pc
    rest = soma %2
    pe = 'T'
    ri = 'g'
    if  pi == 'P':
        pe = 'I'
    elif pi == 'I':
        pe = 'P'

    if rest == 0:
        print(f'A soma de {j} e {pc} deu {soma}, Par.')
        ri = 'P'
    else:
        print(f'A soma de {j} e {pc} deu {soma}, Impar.')
        ri = 'I'

    if pe == ri:
        print('-'*20)
        print('Voce perdeu!')
        print('-' * 20)
        break
    elif pi == ri:
        print('-'*20)
        print('Voce Ganhou')
        print('-' * 20)
        cont += 1
print('*'*30)
print(f'Voce conseguiu ganhar {cont} vezes.')
print('*'*30)