import csv
with open('d:/usuario.csv', 'r') as file:
    #leitura dos arquivos 
    usuarios= csv.reader(file)
    next(usuarios)
    for linha in usuarios:
        if linha[3]== '18':
            print(linha[0])