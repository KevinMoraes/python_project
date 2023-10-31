dados = [[[], [], []], [[], [], []], [[], [], []]]
matriz = []
pares = []
'''for c in range(1, 10):
    n =(int(input('Digite um valor: ')))
    if c <= 3:
        for p in range(0,2):
            dados[0][p].append(n)
    if c > 3 and c <= 6:
        for p in range(0, 2):
            dados[1][p].append(n)
    if c > 6 and c <= 9:
        for p in range(0, 2):
            dados[2][p].append(n)
matriz.append(dados[:])
dados.clear()'''
for l in range (0, 3):
    for c in range(0, 3):
        dados[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='* 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{dados[l][c]:^5}]', end='')
    print()

'''print(f'{dados[0][0]} {dados[0][1]} {dados[0][2]}\n'
      f'{dados[1][0]} {dados[1][1]} {dados[1][2]}\n'
      f'{dados[2][0]} {dados[2][1]} {dados[2][2]}')'''
