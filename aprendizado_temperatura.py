import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#Importando Scikit-learn

# pré-processamento
from sklearn.preprocessing import LabelEncoder

# modelo
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")
#print(df)

#Extração de x e y

x,y = df[['temperatura']].values, df[['classification']].values
#print('x:\n', x)
#print('y:\n', y)

#Conversão de y para valores númericos

le = LabelEncoder()
y = le.fit_transform(y.ravel())
#print('y:\n',y)

#Classificador - melhores coeficientes da função
clf = LogisticRegression()
clf.fit(x,y)

#Gerar 100 valores de temperatura
#linearmente espaçados entre 0 e 45
#predição em novos valores de temperatura
x_test = np.linspace(start=0., stop=45., num=100).reshape(-1,1)

#predição desses valores
y_pred = clf.predict(x_test)

#print(y_pred)

#Conversão do y_pred para os valores originais de Y quente, frio muito quente...
y_pred = le.inverse_transform(y_pred)
#print(y_pred)

#output - Gerando Data Frame
output = {'new_temp': x_test.ravel(),
        'new_class' : y_pred.ravel()}
output = pd.DataFrame(output)

#sistema automático

def classifica_temp():
    #Classifica a temperatura que o usuário enviar

    joga = True
    while joga:
        #Pega temperatura
        temp = input("Insira a temperatura (graus Celsius): ")

        #transformando em numpy array
        temp = np.array(float(temp)).reshape(-1,1)

        #realiza classificação
        class_temp = clf.predict(temp)

        #Transformação inversa para retornar a string original!
        class_temp = le.inverse_transform(class_temp)

        #classificação
        print(f"A classificação da temperatura {temp.ravel()[0]}º é:", class_temp[0])

        #perguntar
        joga = input("Nova classificação (y/n): ") == 'y'

classifica_temp()
