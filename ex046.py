from time import sleep
print('----------CONTAGEM REGRESSIVA COMEÇANDO!----------')
for c in range(10, -1, -1):
    print(c)
    sleep(1)
    if c == 0:
        print('FOGOS PIU PIU!!!')