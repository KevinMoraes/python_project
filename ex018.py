import math
ang = float(input('Digite o ângulo: '))
se = math.sin(math.radians(ang))
co = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Seno {:.2f} \n Coseno {:.2f} \n Tangente {:.2f}'.format(se, co, tang))
