import json
usuarios= {
    'astro':{'nome': 'chico', 'login': 'chico', 'senha': '123'},
    'beri': {'nome': 'berisvaldo', 'login': 'beri', 'senha':'456'}
}
try: 
    with open('d:/usuario.json','w') as arquivo_json:
        json.dump(usuarios, arquivo_json)
except FileNotFoundError:
    print('nao existe o arquivo')