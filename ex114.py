import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[1;31mO site pudim não está acessível no momento.\033[m')
else:
    print('\033[1;32mO site Pudim foi acessado com sucesso.\033[m')
    print(site.read())
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print('\033[1;31mO site pudim não está acessível no momento.\033[m')
else:
    print('\033[1;32mO site Pudim foi acessado com sucesso.\033[m')
    print(site.read())
