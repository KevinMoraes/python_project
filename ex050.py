rest = 0
soma = 0
for c in range(1, 6+1):
    n = int(input('Digite um valor: '))
    rest = n % 2
    if rest == 0:
        soma += n
print('Os valores pares somados sao {}'.format(soma))
