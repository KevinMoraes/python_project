n = int(input('Digite o valor inicial: '))
n1 = int(input('Digite de quantos em quantos vai pular: '))

for c in range(n, n + (n1 * 10), n1):

    print(c, end=' ')
