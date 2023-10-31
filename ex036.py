valor_casa = int(input('Digite o valor da casa: '))
pagamento = int(input('Quantos anos vai pagar: '))
salario = int(input('Qual seu salário mensal: '))
pagamento = pagamento * 12
n1 = salario * 30 / 100
n2 = salario + n1
div = valor_casa/pagamento

if n2 < div:
    print('O valor apresentado exede 130% do seu salário.')
    print('O empréstimo será negado!')
else:
    print('Todo o mês voce tera de pagar R${:.1f}'.format(div))
    print('Emprestimo aceito!')
