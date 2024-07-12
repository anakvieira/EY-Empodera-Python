#Resolver uma equação de segundo grau utilizando a fórmula de baskara

a = 2
b = 4
c = -6

delta = (b ** 2) - (4 * a * c)

#Primeiro valor de x
x_1 = (-b + (delta ** (1/2))) / (2 * a)

#Segundo valor de x
x_2 = (-b -(delta ** (1/2))) / (2 * a)

print("As raízes da equação são %f e %f" % (x_1, x_2))

#Validando o resultado com x_1
print("Resultado da equação com x_1: ", (a * x_1 ** 2 + b * x_1 + c) == 0)

#Validando o resultado com x_2
print("Resultado da equação com x_2: ", (a *x_2 ** 2 + b * x_2 + c) == 0)