dados = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz = []
par = tcol = maior = 0

for l in range (0, 3):
    for c in range(0, 3):
        dados[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='* 30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{dados[l][c]:^5}]', end='')
        if dados[l][c] %2 == 0:
            par += dados[l][c]

    print()
for c in range(0, 3):
    tcol += dados[c][2]
maior = dados[1][0]
for c in dados[1]:
    if c > maior:
        maior = c
print(f'A soma dos valores pares digitados é: [{par}].')
print(f'A soma dos valores da terceira coluna é: [{tcol}].')
print(f'O maior valor da terceira coluna é: [{maior}].')