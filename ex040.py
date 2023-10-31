n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(media)
if media < 5.0 :
    print('Aluno REPROVADO!')
elif media >= 5.0 or media < 6.9:
    print('Aluno em RECUPERAÇÃO!')
elif media >= 7.0:
    print('aluno APROVADO! <3')
