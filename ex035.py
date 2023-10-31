n1 = float(input('Digite o primeiro segmento: '))
n2 = float(input('Digite o segundo segmento: '))
n3 = float(input('Digite o terceiro segmento: '))
'''como saber qual é o maior valor'''
'''maior = 0
resp = 0
if n1 > n2 and n1 > n3:
    maior = n1
else:
    if n2 > n1 and n2 > n3:
        maior = n2
    else:
        if n3 > n1 and n3 > n2:
            maior = n3
if maior == n1 :
    resp = n2 + n3
    if resp <= maior:
        print ('pode formar um triângulo')
    else:
        print('NÃO pode formar um triangulo')
else:
    if maior == n2:
        resp = n1 + n3
        if resp <= maior:
            print('pode formar um triângulo')
        else:
            print('NÃO pode formar um triângulo')
    else:
        if maior == n3:
            resp = n1 + n2
            if resp <= maior:
                print('pode formar um triângulo')
            else:
                print('NÃO pode formar um triângulo')'''

'''print ('o maior é {:.0f}'.format(maior))'''
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Pode formar um triangulo')
else:
    print('nao pode formar o triangulo')