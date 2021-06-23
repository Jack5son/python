#importando as bibliotecas
import matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

'''
#Numpy array é uma estrutura de dados que contém números
# Criação de array 1D
l = [1,2,3,4,5]
x = np.array(l)
print("x:", l)
print("Shape:",x.shape)

#Criação de array 2D
l = [[1,2,3],[4,5,6]]
x= np.array(l)
print("x:", l)
print("Shape:",x.shape)

#Criação de array 3D
l = [[1,2,3],[1,2,3],[1,2,3]]
x = np.array(l)
print("x:", x)
print("Shape:", x.shape)

#Arrays contendo apenas 0
dim = (3,3) #(Linhas, colunas)
x = np.zeros(dim)
print("x:\n", x)
print("Shape:",x.shape)

a = [23,24,25,67]

print(a[1])
#pegar o ultimo elemento do array
print(a[-1])
print(a[-2])

b = [[1,4,3],[1,6,8]]
#pegar elemento da 2D
print(b[1][2])


#slicing
a= [0,1,2,3,4,5,6,7,8,9,10]

print(a[0:6])

#Em array 2D

b = [[1,2,3,4,5,6,7,8,9,10],[10,9,8,7,6,5,4,3,2,1]]

print(b[1:5][1:5])


# Comparações Boleanas
A = np.array([1,2,3])
B = np.array([2,0,2])
s = 3

# menor
print("Comparação menor")
print(A < B)
print(A < s)

# menor ou igual
print("Comparação menor ou igual")
print(A <= B)
print(A <= s)

#indexação boleana
a = np.array([1,2,3])
cond = a <= 2
d = a[cond]
print("Condição:",cond)
print("D:",d)



e = np.array([
    [1,3,7],
    [4,11,21],
    [42,8,9]])

k = 10
cond = e > k
y = e[cond]

print("Condição:\n", cond)
print(y)
#extrair o numero de elementos no array
print(f"Números de elementos que são maiores que {k}:", len(e[cond]))

#Somente valores pares do Array
cond = (e % 2) == 0

print("Condição:",cond)
print(e[cond])
print("Quantidade de numeros pares:", len(e[cond]))

e = np.array([
    [1,3,7],
    [4,11,21],
    [42,8,9]])

#Transformação de matrizes
print ("Transformação de matrizes\n",e.reshape(9,1)) #alterado para 9 linhas e uma coluna

#Transposição da matriz
print("Transposição da matriz:\n",e.T)

#soma de todos elementos
print("Soma de todos elementos:", np.sum(e))
print("Soma das linhas:",np.sum(e, axis= 0))
print("Soma das colunas:",np.sum(e, axis= 1))

#média de todos elementos
print("Média de todos elementos:", np.mean(e))
print("Média das linhas:",np.mean(e, axis= 0))
print("Média das colunas:",np.mean(e, axis= 1))

#mediana de todos elementos
print("Mediana de todos elementos:", np.median(e))
print("Mediana das linhas:",np.median(e, axis= 0))
print("Mediana das colunas:",np.median(e, axis= 1))



#Regrssão Linear
#Dados

x = [-1.,-0.77777778, -0.55555556, -0.33333333, -0.11111111,
     0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657,
     1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]




# Transformando numpy para arrays colunas
x, y = np.array(x).reshape(-1,1), np.array(y).reshape(-1,1)

#adicionando bias: para estimar o termo b
x = np.hstack((x, np.ones(x.shape)))

#estima a e b
beta = np.linalg.pinv(x).dot(y)
print("a estimado:", beta[0][0])
print("b estimado", beta[1][0])

#plot dados
plt.figure(figsize=(10,5)) # tamanho da figura
plt.plot(x,y, 'o', label = 'Dados Originais') # 'o' faz o plot do tipo scater e não do tipo linha
plt.plot(x, x.dot(beta), label = 'Regressão Linear')
plt.legend()
plt.xlabel("x")
plt.xlabel("y")
plt.title("Regressão linear com Numpy")
plt.grid() # linhas da grid
plt.show()


#pandas
#leitura de dados csv

df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")
print(df)

#Planilhas com duas aba ou mais
excel_file = pd.ExcelFile("https://pycourse.s3.amazonaws.com/temperature.xlsx")
df2 = pd.read_excel(excel_file, sheet_name="Sheet1")
print(df2)

df3 = pd.read_excel(excel_file, sheet_name="Sheet2")
print(df3)

#definir quantidade de linhas que quer ver
n =3
print(df.head(n))
#mostrar as "n" ultimas linha
print(df.tail(n))

#data types
print(df.dtypes)

#Estatisticas basicas
print(df.describe())

#dataframe info
print(df.info())

#nomes das colunas - Renomear
#df.columns = ["col1","col2","col3"]

df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")
#indexação direta
print(df['temperatura'])


#indexação boleana
print(df[df['classification'] == 'quente'])



#pandas series por ter um atributo
print(type(df['temperatura']))
#panda frame por ter mais de um atributo
print(type(df[['date','temperatura']]))

#metodo iloc pega pelo indece da coluna
print(df.iloc[:1])
#metodo loc pega o nome da coluna
print(df.loc[:'temperatura'])

#indexação boleana mais coluna
print(df.loc[df['classification'] == 'quente','temperatura'])



#Ordenar em ordem crescente
print(df.sort_values(by=['temperatura']))
print(df.sort_values(by=['classification','temperatura']))

#colocar de forma decrecente
print(df.sort_values(by='temperatura', ascending='false'))



#df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")

#panda frame por ter mais de um atributo
#df[['date']]

#indexação direta
#print(df['temperatura'])

df.plot(figsize = (10,5), grid=True)
df.plot(style= '-o', linewidth =3, figsize = (10,5), grid= True)

df['classification'].value_counts().plot.bar(figsize = (10,5), rot=0)
df.plot (x='temperatura')

'''

df = pd.read_csv("https://pycourse.s3.amazonaws.com/bike-sharing.csv")
dg = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")
print(df)

#Estatisticas basicas
#print(df.describe())

#dataframe info
#print(df.info())

#Estatisticas basicas
#print(df['temp'].describe())

#indexação boleana mais coluna
#print(df['datetime'].info())
print(df['datetime'].describe())

#Agrupar por
print(dg.groupby(by ='classification').mean())
print(dg.groupby(by='classification'))

#somar todos os elementos
print(dg.groupby(by ='classification').sum())

#remoção de uma coluna
print (dg.drop('temperatura', axis = 1))

print(dg.head())

#converter

df['datetime'] = pd.to_datetime(df['datetime'])

df.plot(x='datetime', y= 'total_count')
plt.show()

