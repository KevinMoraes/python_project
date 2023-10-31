cont = s = n = 0
while True:
    n = int(input('Digite um número[999 para parar]: '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'Voce digitou {cont} valores e a soma entre eles deu {s}.')