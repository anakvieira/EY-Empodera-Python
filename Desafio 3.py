#Criar uma função que receba dois parâmetros, o primeiro é uma lista e o segundo é um número inteiro. A saída eve ser uma nova lista onde cada elemento da lista foi multiplicado pelo segundo parâmetro.

def multiplica_por_n(lista, num):
    nova_lista = []
    
    for item in lista:
        nova_lista.append(item * num)
    return nova_lista

def multiplica_por_n_v2(lista, num):
    return [Item * num for item in lista]

print(multiplica_por_n([1,2,3,-1],5))
print(multiplica_por_n_v2([1,2,3,-1],5))