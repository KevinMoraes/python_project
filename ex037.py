num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das opções :
[1] CONVERTER PARA BINÁRIO
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1 :
    print('O numero {} convertido para BINÁRIO fica {}'.format(num, bin(num)[2:]))
elif opcao == 2 :
    print('O numero {} convertido para OCTAL fica {}'.format(num, oct(num)[2:]))
elif opcao == 3 :
    print('O numero {} convertido para HEXADECIMAL fica {}'.format(num, hex(num)[2:]))
else:
    print('Voce nao digitou uma das opções seu bullo!!')