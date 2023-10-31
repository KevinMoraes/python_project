cond = False
n1 = n = 0
cont = 0
while not cond:
    n = int(input('Digite um valor[999 para parar]: '))
    n1 += n
    cont += 1
    if n == 999:
        n1 -= n
        cont -= 1
        cond = True

print('Voce digitou {} e a soma entre eles foi {}'.format(cont, n1))
