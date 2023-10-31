import math
import random

a1: str = input('Primeiro aluno: ')
a2: str = input('Segundo aluno: ')
a3: str = input('terceiro aluno: ')
a4: str = input('Quarto aluno: ')
seq = a1, a2, a3, a4
print ('O(a) aluno(a) escolhido(a) foi {}'.format(random.choice(seq)))