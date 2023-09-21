import json
import os
print ('ENTRAR')

login = input('login: ')
senha = input('senha: ')

try:
    with open(f'd:/{login}.txt', 'r')as f_json:
       arquivo_json= json.loads(f_json.read())
    
except OSError:
    print('login inválido ')
    login = input('login: ')
    senha = input('senha: ')
with open(f'd:/{login}.txt', 'r')as f_json:
    validar = f_json.readline()
    usuario1 = f_json.readline()
    senha1 = f_json.readline(10)
while (senha1 != senha):
    print('Senha invalida')
    senha = input('senha: ')

print('Acesso concedido')
print('-'*30)
print(f'usuario: {usuario1} \nlogin: {validar}')
print('-'*30)