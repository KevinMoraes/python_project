pes = 0
npi = 0
for c in range (1, 6):
    peso = float(input('Digite o {} peso: '.format(c)))
    if c == 1:
        pes = peso
        npi = peso
    else:
        if peso < npi:
            npi = peso
        if peso > pes:
            pes = peso

print('O maior peso digitado foi de {}Kg'.format(pes))
print('O menor peso digitado foi de {}Kg'.format(npi))
