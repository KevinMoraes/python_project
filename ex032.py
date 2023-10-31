'''Um ano bissexto acontece de 4 em 4 anos, o ultimo ano bissexto foi em 2020'''
from datetime import date
ano = int(input('Digite um ano qualquer (se quizer analizar o ano atula digite  0): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO!'.format(ano))
