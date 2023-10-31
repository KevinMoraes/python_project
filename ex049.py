n1 = 0
n2 = 0
tab = int(input('qual tabuada voce deseja ver?: '))
print('************TABUADA************')
'''for c in range(0, 11, 1):
    n1 = c * tab
    print('{} x {} = {}'.format(c, tab, n1))'''
for c in range(1, 11):
    print('{} x {} = {}'.format(tab, c, tab*c))

print('Fim')