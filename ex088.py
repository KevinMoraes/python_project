import random
from time import sleep
rand = 0
igua = 0
print('-'*30)
print('      JOGO DA MEGA SENA')
print('-'*30)
n = int(input('Quantos jogos voce quer sortear?: '))
print(f'-=-=-=  SORTEANDO {n} JOGOS  -=-=-=')
listanum = []
cds = []
for c in range(0, n):
    for p in range(0,6):
        rand = random.randint(0,60)

        if rand in listanum:
            igua = rand
            while igua == rand:
                rand = random.randint(0, 60)
            listanum.append(rand)
        else:
            listanum.append(rand)
    listanum.sort()
    cds.append(listanum[:])
    listanum.clear()
for c, p in enumerate(cds):
    print(f'jogo {c+1}: {p}')
    sleep(1)

