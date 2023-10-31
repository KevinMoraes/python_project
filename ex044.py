prod = float(input('Qual o valor do produto: '))
print('Forma de pagamento:\n1 para dinheiro/cheque\n2 para cartão\n3 para 2x cartão\n4 para 3x ou mais no cartão')
fdpg = int(input('Qual a forma de pagamento:'))
dez = prod - (prod * 10)/100
cin = prod - (prod * 5 )/100
tre = (prod * 20)/100 + prod
doisx = 0
vezes = 0
if fdpg == 1:
    print('Seu valor a pagar é {:.2f}'.format(dez))
elif fdpg == 2:
    print('Seu valor a pagar é {:.2f}'.format(cin))
elif fdpg == 3 :
    doisx = prod / 2
    print('Seu valor a pagar é de 2 vezes de {:.2f}'.format(doisx))
elif fdpg == 4 :
    vezes = int(input('Em quantas vezes vai pagar: '))
    doisx = tre / vezes
    print (tre)
    print('Seu valor a pagar é {:.2f}'.format(doisx))
else:
    print('Valor nâo reconhecido, tente novamente.')
