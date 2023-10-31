n1 = float(input('Digite o preço do seu produto: '))
promo = (n1*5)/100
val = n1 - promo
print('Seu produto de R${:.2f} com o desconto de 5% fica = R${:.2f}'.format(n1 ,val))