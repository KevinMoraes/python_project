num = int(input('Digite seu número: '))
'''uni = (num[3])
dez = (num[2])
cen = (num[1])
mil = (num[0])
print('Unidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(num[3], num[2], num[1, num[0]]))'''
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))
