a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite o ultimo numero: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor é {}.\nO maior valor é {}'.format(menor, maior))
