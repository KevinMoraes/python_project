nome = str(input('nome: '))
dados = {'Nome' : nome}
media = float(input(f'qual foi a média de {dados["Nome"]}:'))
if media >= 7:
    situacao = 'Aprovado'
elif media < 7:
    situacao = 'Reprovado'
dados['Média']= media
dados['Situação']= situacao

for k, v in dados.items():
    print(f' {k} é igual a {v}')
