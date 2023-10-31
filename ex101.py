from datetime import date
def voto(n):
    '''
    calcula a dataatual com o ano que a pessoa nasce para saber se a pessoa tem idade para votar.
    NEGADO para menor de 18.
    OBRIGATÓRIO para maior de 18.
    OPCIONAL para maiores de 65.
    :param n: ano em que a pessoa nasceu.
    :return: sem retorno
    '''
    global nasc
    global otro
    anoatual = date.today().year
    nasc = anoatual - n
    if nasc < 18:
        print(f'Com {nasc} anos o voto é NEGADO!')
        otro = 'NEGADO'
    if nasc >= 18:
        print(f'Com {nasc} anos o voto é OBRIGATÓRIO!')
        otro = 'OBRIGATÓRIO'
    if nasc >= 65:
        print(f'Com {nasc} anos o voto é OPICIPNAL!')
        otro = 'OPCIONAL'
    return(nasc)
    return(otro)

otro = ''
print('--'* 15)
voto(int(input('Em que ano voce nasceu? ')))
print(f'Com {nasc} anos : VOTO {otro}')

