
from math import hypot
n1 = float(input('Cateto oposto: '))
n2 = float(input('Cateto adjacente: '))
n3 = hypot(n1, n2)
print('Apartir dos catetos {:.2f}, {:.2f} apreentados temos a hipotenusa {:.2f}'.format(n1, n2, n3))

"""co = float(input('Cateto oposto: '))
ca = float(input('cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print ('sua hipotenusa é {:.2f}'.format(hi))"""