listanum = []
maior = 0
menor = 0
cont1 = []
cont2 = []
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c} : ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] > maior:
            maior = listanum [c]
        if listanum[c] < menor:
            menor = listanum[c]
print(f'voce digitou os valores {listanum}')
print(f'o maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i + 1}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i+1}...', end='')
print()

'''for c, v in enumerate(num):
    if num[c] > maior:
        maior = num[c]
        #cont1.append(c)
    if num[c] < menor:
        menor = num[c]
        #cont2.append(c)
print(f'Você digitou os valores {num}')
print(f'encontrei o maior valor {maior} ', end='')

#for p in cont1:
    #print(f'{p}...', end='')
print(f'\nencontrei o menor valor {menor} ', end='')
for menor in cont:
    print(f'{cont}....')
#for s in cont2:
    #print(f'{s}...', end='')'''
