def aumentar(preço, taxa):
    res = ((preço/100) * taxa ) + preço
    return res


def diminuir(preço, taxa):
    res = ((preço/100) * taxa) - preço
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res