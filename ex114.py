import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mNão foi possivel acessar o site pudim no momento!\033[m')
else:
    print('\033[0;32mConsegui acessar o site pudim com sucesso!\033[m')
    print(site.read())