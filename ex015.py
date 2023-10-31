k = float(input('Quantos Kilometro foram rodados?: '))
d = float(input('Quantos dias foio alugado?: '))
total = (k * 0.15) + (d * 60)
print('O total a pagar é {:.2f}'.format(total))