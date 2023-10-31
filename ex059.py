from time import sleep
nota = 0
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = 0
nota = int(input('   [1] Somar\n   [2] Multiplicar\n   [3] Maior\n   [4] Novos números\n   [5] Finalizar programa\nResposta: '))
while nota != 5:
    if nota == 1:
        n3 = n1 + n2
        print('A soma de {} e {} fica {}'.format(n1, n2, n3))
    elif nota == 2:
        n3 = n1 * n2
        print('A multiplicação de {} e {} fica {}'.format(n1, n2, n3))
    elif nota == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 < n2:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Os dois numeros sao iguais!')
    elif nota == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif nota != 5 or nota != 4 or nota != 3 or nota != 2 or nota != 1:
        print('Valor inválido! Tente novamente...')
    nota = int(input('   [1] Somar\n   [2] Multiplicar\n   [3] Maior\n   [4] Novos números\n   [5] Finalizar programa\nResposta: '))
print('Finalizando...')
sleep(1)
print('Fim do programa!')
