import json
import os #verifica se o arquivo existe 
try:
    usuarios= {}
    if os.path.exists('d:/usuarios.json'):
        with open('d:/usuarios.json','r') as arquivo:
            usuarios= json.loads(arquivo.read())
    print(usuarios)
    print(usuarios['beri']['nome'])
except FileNotFoundError:
    print('nao existe ')
