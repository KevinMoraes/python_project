from time import sleep
def tiverde(txt):
    print(f'\033[1;49;42m{"~"*(len(txt)+ 4)}')
    print(f'\033[1;49;42m  {txt}  ')
    print(f'\033[1;49;42m{"~" * (len(txt) + 4)}')
def tiazul(txt):
    print(f'\033[0;49;44m{"~"*(len(txt)+ 4)}')
    print(f'\033[0;49;44m  {txt}  ')
    print(f'\033[0;49;44m{"~"*(len(txt)+ 4)}')
def ajuda():
    while True:
        tiverde('SISTEMA DE AJUDA PyHELP')
        sleep(0.5)
        n = str(input('\033[mFinção ou biblioteca > '))

        if n.upper() == 'FIM':
            break
        else:
            tiazul(f"Acessando manual do comando '{n}'... ")
            sleep(1)
            print('\033[7;49m', end='')
            help(n)
            print('\033[m', end='')
            sleep(0.5)
    print(f'\033[1;33;41mFIM!')





ajuda()