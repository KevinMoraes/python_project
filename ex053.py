frase = str(input('Digite a frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[:: -1]
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print('{}  {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo<3')
else:
    print('Nao tem paliondromo ai!')