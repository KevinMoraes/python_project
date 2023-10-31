jogador = {}
jogador['nome'] = str(input('Nome do jogador: '))
qp = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
n = qp
n1 = 0
gqp = list()
totalg = 0
while n1 != n:
    gqp.append(int(input(f'Quantos gols na partida {n1}')))
    n1 += 1
for v in gqp:
    totalg += v
jogador['gols'] = gqp
jogador['total'] = totalg
print('-=' *30)
print(jogador)
print('-=' *30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {qp} partidas.')
ppp = 0
m = 0
while ppp < qp:
    print(f'  => Na partida {ppp}, fez {gqp[m]} gols.')
    ppp += 1
    m += 1
print(f'Foi um total de {totalg} gols.')