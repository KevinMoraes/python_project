kmh = float(input('Digite a velocidade do seu carro: '))
custo = kmh - 80
multa = custo * 7.0
if kmh > 80:
    print('Você foi MULTADO! Sua multa sera de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia, Dirija com segurança!')