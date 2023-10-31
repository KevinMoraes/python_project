def area(a, b):
    adt = a * b
    print(f'A área de um terreno {a}X{b} é de {adt} metros quadrados.')
def linha(txt):
    print('-' *20)
    print(f' {txt} ')
    print('-' * 20)
linha('Controle de Terrenos')
n1 = float(input('LARGURA (m):'))
n2 = float(input('COMPRIMENTO (m):'))
area(n1, n2)