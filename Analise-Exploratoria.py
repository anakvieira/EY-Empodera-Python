import pandas as pd

dados = {'nome': ['Pedro', 'Maria', 'Janaina', 'Marco'],
         'cidade': ['Rio de Janeiro', 'Curitiba', 'Brasília', 'Salvador'],
         'idade': [34, 23, 32, 43],
         'nota': [83.0, 59.0, 86.0, 61.0],
         'time': ['Vasco', 'Fluminense', 'Atlético-PR', 'Bahia']}
dfAlunos = pd.DataFrame(data=dados)

print(dfAlunos)

dfAlunos.columns

dfAlunos.info()

#Calculo de Desvio Padrão, Mínimo, Quartis e Máximo
dfAlunos.describe().transpose()

#Acessar linhas de intervalo fechado
dfAlunos[1:3]

#Consultar informações específicas do dataframe
dfAlunos[['nome', 'nota']]

#Consultar informações e limitar o número de linhas exibidas
dfAlunos[['nome', 'nota']][1:3]

#Mesclar dataframes com pd.merge()
dfAlunos2 =pd.DataFrame({ 'nome': ['Pedro', 'Maria', 'Janaina', 'Marco'],
                           'altura': [1.71, 1.68, 1.72, 1.80] })
                           
dfAlunos_completo = pd.merge(dfAlunos, dfAlunos2, on = 'nome')
dfAlunos_completo

import pandas as pd

area = pd.Series({'Belo Horizonte': 423967, 'São Paulo': 695662,
                  'Curitiba': 141297, 'Rio de Janeiro': 170312})

pop = pd.Series({'Belo Horizonte': 2423642, 'São Paulo': 469562,
                 'Curitiba': 1141297, 'Rio de Janeiro': 3170312})

dados = pd.DataFrame({'área': area, 'população': pop})
dados

#Liste com a coluna população
dados['população']

#Liste com a coluna area
dados=['area']

#Abaixo da linha do elemento
dados.loc['Curitiba':]

#Colunas 0 e 1, linhas 0 e 1
dados.iloc[0:2, :1]

# Filtros e Manipulações

dados.filter(items=['area'])

#Procura por expressão que termina com 'e', nas linhas
dados.filter(regex='e$', axis=0)

#Procura por expressão que termina com 'ro', nas linhas
dados.filter(regex='ro$', axis=0)

#Procura por expressão contendo 'ri', nas linhas
dados.filter(likes='ri', axis=0)

#Visualização de Dados

# Salva e recupera do Google Drive (irá pedir autorização da 1a vez)
import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

demografia = pd.read_csv('/content/drive/My Drive/Demographic data.csv')
demografia.columns = ['País', 'Código', 'Natalidade',
                      'Internet', 'Renda']
demografia.head()

import pandas as pd
import random

# Criando dados aleatórios
# Ensure all lists have the same length (200 in this case)
paises = ["Brasil", "Estados Unidos", "China", "Índia", "Rússia", "Japão", "Alemanha", "França", "Reino Unido", "Itália"] * 20 # Repeat the list 20 times
codigos = [random.randint(100, 999) for _ in range(200)]
natalidade = [random.randint(1000, 10000) for _ in range(200)]
internet = [random.uniform(30, 90) for _ in range(200)]
renda = [random.randint(20000, 80000) for _ in range(200)]
populacao = [random.randint(1000000, 20000000) for _ in range(200)]
renda_media = [random.uniform(2000, 8000) for _ in range(200)]

# Criando o DataFrame
dados = pd.DataFrame({
    "País": paises,
    "Código": codigos,
    "Natalidade": natalidade,
    "Internet": internet,
    "Renda": renda,
    "População": populacao,
    "Renda Média": renda_media
})

# Exibindo as primeiras 5 linhas
print(dados.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Access the 'Internet' column from the DataFrame
vis1 = sns.distplot(dados["Internet"], bins=20) 
plt.show() # Display the plot