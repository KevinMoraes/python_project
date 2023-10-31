pares = 0
rest = 0
'''for c in range(0, 51, 2):
    print(c)'''
for pares in range(2, 51):
    rest = pares % 2
    if rest == 0:
        print('.', end=' ')
        print(pares, end=' ')
