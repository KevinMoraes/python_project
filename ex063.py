print('-'*30)
print('   Sequencia de fibonacci')
print('-'*30)
n = int(input('Digite quantos termos voçê quer ver: '))
cont = 0
n1 = n3 = 0
n2 = 1
print('{} -> {} '.format(n1, n2), end='-> ')
while cont < n:
    n3 = n1 + n2
    print('{} '.format(n3), end='-> ')
    n1 = n2
    n2 = n3
    cont += 1
