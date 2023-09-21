import csv
novos_dados=[
    ['Tiburcio','tiby','18','321'],
    ['otto','ots','88','645']
]
with open('d:/usuario.csv', 'a', newline="") as file:
    escreve_csv=csv.writer(file) #passa a funcao de escrita
    for linha in novos_dados:
        escreve_csv.writerow(linha) #escreve as linhas
