#Imprimir todos os pares de números cuja soma seja igual a x. A lista é composta dos números inteiros de 0 até x-1.

valor = 36
acum = 0

for item in range(valor):
    for item_aux in range(item + 1, valor):
        if item + item_aux == valor:
            print("{0} + {1} = {2}".format(item, item_aux, valor))

print("====================")

lista = range(valor)
for item in range(int(valor / 2)):
    if(valor - item) in lista:
        print("{0} + {1} = {2}".format(item, valor - item, valor))