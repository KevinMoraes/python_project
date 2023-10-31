from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(0, 7+1):
    ano = int(input('Digite o ano em que voce nasceu: '))
    idade = atual - ano
    if idade <= 18:
        menor += 1
    else:
        maior += 1
print('Nesta contagem obtivemos {} pessoas de menor idade\nE {} pessoas e maior idade'.format(menor, maior))
