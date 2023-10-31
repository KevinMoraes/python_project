import random
print('--------Escolha-------- \n1 - Pedra\n2 - Papel\n3 - Tesoura')
jogador = int(input('resposta:'))
jogo = ['Pedra', 'Papel', 'Tesoura']
escolhido = random.choice(jogo)
print(escolhido)
print('---------------------------------------------------------------')
if jogador == 1 and escolhido == 'Pedra':
    print('Empate')
elif jogador == 1 and escolhido == 'Papel':
    print('Papel engole pedra, PERDEU!')
elif jogador == 1 and escolhido == 'Tesoura':
    print('Pedra amassa tesoura, GANHOU!')

elif jogador == 2 and escolhido == 'Pedra':
    print('Papel engole pedra, GANHOU!')
elif jogador == 2 and escolhido == 'Papel':
    print('Empate')
elif jogador == 2 and escolhido == 'Tesoura':
    print('Tesoura corta papel, PERDEU!')

elif jogador == 3 and escolhido == 'Pedra':
    print('Pedra amassa tesoura, PERDEU!')
elif jogador == 3 and escolhido == 'Papel':
    print('Tesoura corta papel, GANHOU!')
elif jogador == 3 and escolhido == 'Tesoura':
    print('Empate')