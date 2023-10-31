from random  import randint
cinum= (randint(0,10), randint(0,10), randint(0,10),randint(0,10), randint(0,10))
print(cinum)
maior = cinum[0]
menor = cinum[0]
'''if maior < cinum[1]:
    maior = cinum[1]
if maior < cinum[2]:
    maior = cinum[2]
if maior < cinum[3]:
    maior = cinum[3]
if maior < cinum[4]:
    maior = cinum[4]'''
print(f'O maior número foi: {max(cinum)}')
'''if menor > cinum[1]:
    menor = cinum[1]
if menor > cinum[2]:
    menor = cinum[2]
if menor > cinum[3]:
    menor = cinum[3]
if menor > cinum[4]:
    menor = cinum[4]'''
print(f'O menor numero foi: {min(cinum)}')
c = 0
