final = False
f = ''
teste = 0
num = 0
copia = []
lista = []
lista.append((int(input('Digite um valor: '))))
print(f'O valor foi adicionado a lista...')
f = str(input('Quer continuar?[S/N] ')).upper()
if f == 'N':
    final = True
while final != True:
    lista.append((int(input('Digite um valor: '))))
    num = lista[-1]
    copia = lista[:]
    for i, c in enumerate(lista):
        if c == lista[i-1]:
            lista.pop()
            print(f'O valor nao pode ser adicionado...')
    if lista == copia:
        print(f'O valor foi adicionado a lista...')
    f = str(input('Quer continuar?[S/N] ')).upper()
    if f == 'N':
        final = True

lista.sort()
print(f'Voce digitou os valores {lista}')
