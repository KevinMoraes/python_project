from ex107 import moeda

p = float(input('Digite um valor em reais: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10% temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo em 13% temos {moeda.diminuir(p, 13)}')
