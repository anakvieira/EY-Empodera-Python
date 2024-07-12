#Leitura de dados do teclado é feita através da função: input. Por padrão é string, mas pode ser mudada. Validação para garantir.

#Desafio 4: Escrever uma função que imprima em quais linhas do arquivo aparece o parâmetro da função. Caso a palavra não exista no arquivo, nada deve ser impresso.

def verifica_existencia_palavra(palavra):
    with open("poema.txt") as f:
        conteudo_arquivo = f.readlines()

        num_linha = 0
        for linha in conteudo_arquivo:
            if palavra in linha:
                print("Palavra {0} encontrada na linha {1}".format(palavra,num_linha+1))
                num_linha += 1
verifica_existencia_palavra("Sabiá")