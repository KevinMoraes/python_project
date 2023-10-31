frase = str(input('Digite uma frase: ')).strip()
qa = frase.lower().count('a')
qai = frase.lower().find('a') + 1
qaf = frase.lower().rfind('a')+ 1
print('Existe no total {} as na frase'.format(qa))
print('A primeira letra a aparece em: {}'.format(qai))
print('A ultima letra A aparece em : {}'.format(qaf))
