from random import randint
'''print(randint(0, 9))'''
alea = randint(0, 10)
print('Olá, eu sou seu computador.\nEu estou pensando em um número entre 1 e 10, voce consegue adivinhar?')
player = int(input('Digite um valor: '))
cont = 1
acertou = False
while not acertou:
    print('Voce errou!')
    player = int(input('Digite um valor: '))
    cont += 1
    if player == alea:
        acertou = True
    else:
        if player < alea:
            print('Mais... tente novamente')
        elif player > alea:
            print('Menos... tente novamente')
print('Voce acertou! mas foi so na tentativa {}'.format(cont))