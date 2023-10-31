lista = []
dados = [[], []]
dados1 = []
dados2 = []
for c in range(1, 8):
    n = int(input(f'Digite p {c}o. valore: '))
    if n % 2 == 0:
        dados[1].append(n)
    else:
        if n % 2 == 1:
            dados[0].append(n)
'''dados.append(dados1)
dados.append(dados2)'''
print('-='*30)
print('Os valores pares digitados foram:', end='')
print(sorted(dados[1]))
print('Os valores impares digitados foram: ', end='')
print(sorted(dados[0]))
