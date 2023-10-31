cont = 0
nomemin = []
nomemax = []
min = max = 0
lista = []
dados = []
while True:
    '''dados.append(str(input('Nome: ')))
    dados.append(str(input('Peso: ')))'''
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        min = max = dados[1]
    else:
        if dados[1] > max:
            max = dados[1]
        if dados[1] < min:
            min = dados[1]
    lista.append((dados[:]))
    dados.clear()
    r = str(input('Quer continuar?[S/N] ')).upper()
    if r == 'N':
        break
    cont += 1
'''for c in dados:
    if c[1] >= 0:
        pesmin.append(lista[0][1][:])
        pesmax.append(lista[0][1][:])
        print(pesmax)'''
'''for c in dados:
    if c <= 70:
        abaixo.append(dados[c])

    elif c >= 100:
        acima.append(dados[c])'''
print(f'Ao todo, foram cadastradas {cont+1} pessoas.')
print(f'O maior peso foi de {max} Kg, das pessoas', end='')
for  p in lista:
    if p[1] == max:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {min} Kg, das pessoas', end='')
for l in lista:
    if l[1] == min:
        print(f'[{l[0]}] ', end='')