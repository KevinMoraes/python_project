from time import sleep
'''def maior(*num):
    print('-='* 30)
    print(f'Analisando valores passados... ')
    for k in num:
        print(f'{k} ', end='')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo.')
    mai = list()
    for k in num:
        mai.append(k)
        if num == 0:
            mai.append(0)
    m = mai[0]
    for k in mai:
        if m < k:
            m = k
    print(f'O maior valor digitado foi {m}.')
    print('-='*30)'''
def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ',end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()