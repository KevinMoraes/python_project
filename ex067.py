n = 1
tab = 0
c = 1
while True:
    print('-'*30)
    n = int(input('Qual tabuada voce quer ver?: '))
    print('-'*30)
    if n < 0:
        break
    while c < 11:
        print(f'{n} x {c} = {n*c}')
        c += 1
    c = 1
print('-'*50)
print('Programa TABUÁDA ENCERRADO! Volte sempre!')


