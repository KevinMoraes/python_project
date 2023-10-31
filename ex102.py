
def fatorial(num = 1, show = False):
    '''
    -> Calcula o fatorial de um número.
    :param num: número a ser calculado.
    :param show: (opicional= True/False) Mostra ou não mostra a conta.
    :return: O valor do Fatorial de um número n.
    '''
    f = 1
    for c in range(num, 0, -1):
        if show == True:
            print(f'{c} ', end='')
            if c > 1:
                print(f'x ', end='')
        f *= c
    if show == True:
        print('= ', end='')
    print(f'{f}')

fatorial(12, True)
help(fatorial)
