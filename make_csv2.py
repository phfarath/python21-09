import csv

print('digite um genero: ')
escolha=input()
with open('d:/filmes.csv', 'r') as file:
    filmes= csv.reader(file)
    for i in filmes:
        if i[1]== escolha:
            print(i[0])