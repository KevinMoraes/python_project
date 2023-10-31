from time import sleep
dados = list()
lista = list()
media = []
respo= 0
n = 0
while True:
    nome = (str(input('Nome: ')))
    notum = (float(input('Nota 1: ')))
    notdois = (float(input('Nota 2: ')))
    med = notum + notdois/2
    print(med)
    media.append(med)
    dados.append(nome)
    dados.append(notum)
    dados.append(notdois)
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar?[S/N]: ')).upper()
    if resp == 'N':
        break
print('-='*30)
print('No. NOME       MÉDIA')
print('-'*20)
for c, p in enumerate(lista):
    print(f'{c}   {lista[c][0]}        {media[c]}')
while True:
    print('-'*30)
    n = int(input('Mostra nota de qual aluno?(999 para interromper): '))
    if n == 999:
        break
    respo = n
    print(f'Notas de {lista[respo][0]} são [{lista[respo][1]}, {lista[respo][2]}]')
print('FINALIZANDO...')
sleep(1)
print('<'*3, ' VOLTE SEMPRE ', '>'*3)
