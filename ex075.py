print('Digite valores entr 0 e 10')
lista = (int(input('Digite um núero: ')),
         int(input('Digite outro: ')),
         int(input('Digite outro: ')),
         int(input('Digite mais um: ')))

novecont = 0
pares = 0
tres = False
for n in lista:
    if n % 2 == 0:
        pares += 1
for c in lista:
    if c == 9:
        novecont += 1

print(f'O 9 apareceu {novecont} vezes')
for f in lista:
    if f == 3:
        tres = True
if tres == True:
    tres = (f'O 3 apareceu na {lista.index(3)+1} posição')
else:
    tres = ('O 3 não apareceu')
print(tres)
print(f'Existem no total {pares} pares')
