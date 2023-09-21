import csv
filmes=[

]
print('deseja cadastrar filmes? (y/n)')
resp=(input()).lower()
while resp!='n' :
    titulo=input('digite o titulo: ')
    genero=input('digite o genero: ')
    duracao=input('digite o duracao: ')
    censura=input('digite o censura: ')
    diretor=input('digite o diretor: ')
    filmes.append([titulo,genero,duracao,censura,diretor])
    print('Deseja continuar? (y/n)')
    resp=input().lower()
    with open('d:/filmes.csv', 'a', newline='') as file:
        escreve_csv=csv.writer(file)
        for i in filmes:
            escreve_csv.writerow(i)
        
        
