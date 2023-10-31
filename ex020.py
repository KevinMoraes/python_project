import random
a1: str = input('Primeira pessoa:')
a2: str = input('Segunda pessoa: ')
a3: str = input('Terceira pessoa: ')
a4: str = input('Quarta pessoa: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(lista)
