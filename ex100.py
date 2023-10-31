import random
def sorteio(lista):
    n = 5
    print('Sorteando 5 valores da lista:', end='')
    while n != 0:
        r = random.randint(1, 10)
        print(f' {r} ', end='')
        lista.append(r)
        n -= 1
    print('PRONTO!')


def SomaPar(lista):
    par = 0
    for valor in lista:
        if valor % 2 == 0:
            par += valor
    print(f'Somando os valores pares temos {par}.')

numeros = []
sorteio(numeros)
SomaPar(numeros)