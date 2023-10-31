n1 = int(input('Digite o primeiro lado: '))
n2 = int(input('Digite o segundo lado:'))
n3 = int(input('Digite o terceiro lado: '))
if n1 < n2 + n3 or n2 < n1 + n3 or n3 < n1 + n2:
    print('Pode formar um triÂngulo', end='')
    if n1 == n2 and n1 == n3:
        print('Equilátero')
    elif n1 == n2 and n1 != n3 or n1 == n3 and n1 != n2 or n2 == n3 and n2 != n1:
        print('Isoceles')
    elif n1 != n2 and n1 != n3 and n2 != n3 and n3 != n1:
        print('Escaleno')
else:
    print('Não pode formar um truângulo')
