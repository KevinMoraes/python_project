from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano em que nasceu: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('MIRÍM!')
elif idade > 9 and idade <= 14:
    print(' INFANTÍL!')
elif idade > 14 and idade <= 19:
    print('JÚNIOR!')
elif idade > 19 and idade <= 25:
    print('SéNIOR!')
else:
    print('MASTER!')
