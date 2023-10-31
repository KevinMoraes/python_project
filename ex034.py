sal = float(input('Digite seu salário: '))
aumento = 0

if sal <= 1.250:
    aumento = (sal * 15/100) + sal
    print('Seu novo salario é de R${}'.format(aumento))
else:
    aumento = (sal * 10/100) + sal
    print('Seu novo salário é de R${}'.format(aumento))
