n1 = int(input('Digite o número que voce quer fatorar: '))
n2 = n1 - 1
n3 = 0
n3 = n1 * n2
cont = n1
while n2 > 1:
    n2 -= 1
    n3 = n3 * n2
print('Calculando {}!'.format(n1))
while cont > 1:
    print('{} x '.format(cont), end='')
    cont -= 1
print('1 = {}'.format(n3))
f = 1
'''n = int(input('Digite um número para fatorar: '))
for c in range(n,  0, -1):
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
print(f)'''



