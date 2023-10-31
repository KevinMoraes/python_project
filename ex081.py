resp = False
lista = []
cont = 0
r = 'N'
while resp != True:
    lista.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar?[S/N] ')).upper()
    if r == 'N':
        resp = True
if 5 in lista:
    print('o numero 5 está na lista!')
if 5 not in lista:
    print('o numero 5 NAO está na lista!')
lista.sort(reverse=True)
print(f'A ordem decrescente é {lista}')
print(f'Foram digitadosao todo {len(lista)} numeros')
