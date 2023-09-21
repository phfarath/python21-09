import json
import os
try:
    print('Faça seu cadastro: (y/n)')
    resp=(input()).lower()
    while resp!='n' :
        print('Digite o seu nome: ')
        nome=input()
        print('Digite seu login: ')
        login= input()
        print('Digite sua senha: ')
        senha=input()
        with open(f'd:/{login}.txt', 'a')as f_json:
            json.dump(nome, f_json)
            json.dump(login, f_json)
            json.dump(senha, f_json)
            print('Deseja continuar? (y/n)')
            resp=input().lower()
except FileNotFoundError:
    print('arquivo nao encontrado')