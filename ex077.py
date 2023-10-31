Palavras = ('APRENDER',
            'PROGRAMAR',
            'LINGUAGEM',
            'PYTHON',
            'CURSO',
            'GRATIS',
            'ESTUDAR',
            'PRATICAR',
            'TRABALHAR',
            'MERCADO',
            'PROGAMADOR',
            'FUTURO')
'''a = 0
e = 0
i = 0
o = 0
u = 0
quebrado = ' '
cont = 0
while True:
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    for pos in range(0, len(Palavras)):
        quebrado = Palavras[pos]
        for letra in range(0, len(quebrado)):
            if quebrado[letra] == 'A':
                a += 1
            if quebrado[letra] == 'E':
                e += 1
            if quebrado[letra] == 'I':
                i += 1
            if quebrado[letra] == 'O':
                o += 1
            if quebrado[letra] == 'U':
                u += 1

    print(a)
    print(e)
    print(i)
    print(o)
    print(u)
    cont += 1
    if cont == len(Palavras):
        break'''
for p in Palavras:
    print(f'\nNa palavra {p} temos ', end= '')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')