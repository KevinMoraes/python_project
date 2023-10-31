resp = False
lista = []
listapar = []
listaimp = []
r = 'S'
while resp != True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar?[S/N] ')).upper()
    if r == 'N':
        resp = True
for v in lista :
    if v % 2 == 0:
        listapar.append(v)
    if v % 2 == 1:
        listaimp.append(v)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimp}')