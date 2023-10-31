times = ('Palmeiras', 'Internacional', 'Corinthians', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Atlético-MG', 'América-MG',
         'Botafogo', 'Fortaleza', 'Santos', 'São Paulo', 'Bragantino', 'Goiás', 'Coritiba', 'Ceará SC', 'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')
print(f'Lista de times do brasileirão:{times}')
#for t in times:
   # print(t)
print(f'Os primeiros 5 são:{times[0:5]}')
print(f'os ultimos 4 são:{times[-4:]}')
print(f'Em Ordem alfabética:{sorted(times)}')
print(f'O Corinthians esta na {times.index("Corinthians")+1} posição')
