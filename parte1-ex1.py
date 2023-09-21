try:
    #criando um arquivo 
    #fecha os arquivo automaticamente
    with open('d:/mafagafo.txt' , 'w') as arquivo:
        arquivo.write('Um ninho de mafagafos, ')
        arquivo.write('tinham sete mafagafinhos.\n')
        arquivo.write('quem desmafagar esses mafagafinhos ')
        arquivo.write('bom desmafagafador sera')
    #lendo o arquivo
    arquivo = open('d:/mafagafo.txt', 'r')
    print(arquivo.read())
    arquivo.close()
except FileNotFoundError:
    print('Arquivo inexistente')