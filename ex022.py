nome = str(input('Digite seu nome: '))
mai = nome.upper()
min = nome.lower()

pro = nome.strip().split()
pao = ''.join(pro)
feito = len(pao)

pra = nome.split()
pri = len(pra[0])

print(mai)
print(min)
print(feito)
print(pri)