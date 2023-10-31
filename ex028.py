from random import randint
comp = randint(0, 5)
print('-=-' * 20)
resp = int(input('Adivinhe o numero de 0 a 5: '))
print('-=-' * 20)
if resp == comp:
    print('Parabéns você acertou!!!')
else:
    print('Você errou feio skskskksks, a resposta certa era {}'.format(comp))