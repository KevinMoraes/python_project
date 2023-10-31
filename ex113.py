def LeiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mO valor digitado não foi um número inteiro!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[0;31mO Usuário decidiu terminar o console!\033[m')
            return 0
        else:
           return n


def LeiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mUsuário digitou um valor real invalido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[0;31mConsole interrompido no processo!\033[m')
            return 0
        else:
            return n

print('')
print('-'*30)
n1 = LeiaInt('Digite um número Inteiro: ')
n2 = LeiaFloat('Digite um número Real: ')
print(f'Você acabou de digitar o número {n1}')
print(f'Voce acabou de digitar o número {n2}')
