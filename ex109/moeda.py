def aumentar(preço=0, taxa=0, formato=False):
    '''
    FUnção que aumenta em taxa um valor.
    :param preço: valor.
    :param taxa: valor em % a ser aumentado.
    :param formato: se vai ser formatado com R$ e virgulas.
    :return: retorna o resultado.
    '''
    res = preço + ((preço*taxa) /100 )
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    '''
    Função que diminue em taxa um valor.
    :param preço: valor.
    :param taxa: valor em % a ser aumentado.
    :param formato: se vai ser formatado com R$ e virgulas.
    :return: retorna o resultado.
    '''
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    '''
    DObra o valor.
    :param preço: valor.
    :param formato: se vai ser formatado com R$ e virgulas.
    :return: retorna o valor.
    '''
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    '''
    Divide em dois o valor.
    :param preço: valor.
    :param formato: se vai ser formatado com R$ e virgulas.
    :return: retorna o valor.
    '''
    res = preço / 2
    return res if formato is True else moeda(res)


def moeda(preço=0, moeda="R$"):
    '''
    formata um valor solicitado.
    :param preço: valor.
    :param moeda: formatação do valor.
    :return: valor formatado.
    '''
    return f'{moeda}{preço:>.2f}'.replace('.', ',')
