def nota(*float, sit = False):
    '''
    -> Função para notas e situações de vários alunos.
    :param float: uma ou mais notas dos alunos (aceita várias).
    :param sit:  valor situação aparece, opcional(True/False).
    :return: Dicionário com várias informações sobre a situação da turma.
    '''
    global mai
    global men
    global resp
    mai = men = cont = 0
    med = 0
    for c in float:
        med += c
        if cont == 0:
            mai = c
            men = c
        if c > mai:
            mai = c
        if c < men:
            men = c
        cont += 1
        print(f'{c}')
    medi = med / len(float)
    tot = len(float)
    situa = ''
    resp = {'Total' : tot, 'Maior' : mai, 'Menor' : men, 'Media': medi}
    if medi < 6:
        situa = 'RUIM'
    if medi >= 6:
        situa = 'RAZOÁVEL'
    if medi >= 7:
        situa = 'BOA'
    if sit == True:
        resp['Situação'] = situa



nota(3.5, 2, 6.5, 2, 7, 4, sit= True)
print('--'* 30)
print(resp)
help(nota)