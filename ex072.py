r = 111111
num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'nove','Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
count = enumerate(num)
while True:
    r = int(input('Digite um número entre 0 e 20: '))
    if r >= 0 and r <= 20:
        break
print(f'Voce digitou o numero {num[r]}')