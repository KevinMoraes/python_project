from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano em que você nasceu: '))
idade = atual - nasc
print ('Voce tem {} em {}'.format(idade, atual))
conta = 0
sera = 0
if idade > 18 :
    conta = idade -  18
    sera = atual - conta
    print('Voce devia ter se alistado a {} anos'.format(conta))
    print('em {}'.format(sera))
elif idade <= 17 :
    conta = 18 - idade
    sera = atual + conta
    print ('Voce vai se alistar em {} anos'.format(conta))
    print('em {}'.format(sera))
else:
        print('ESTA NA HORA DE SE ALISTAR!')
