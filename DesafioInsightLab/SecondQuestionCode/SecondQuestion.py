#Tratamento de arquivos
import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
#Biblioteca para aprendizado
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression as lm

#Leitura dos arquivos
def input_data():
    path = r'Dados/'
    files = glob.glob(path + "/*.csv")
    frame = []
    for unique_file in files:
        aux = pd.read_csv(unique_file, index_col = None, header = 0)
        frame.append(aux)
    dataframe = pd.concat(frame,axis=0,ignore_index=True)
    grouped = dataframe[['HORAOCORRENCIA','BAIRRO', 'CIDADE','DATACOMUNICACAO']]
    return grouped

def train(dataset):
    y = dataset.HORAOCORRENCIA
    x = dataset.drop('HORAOCORRENCIA', axis=1)
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
    #x_train.head()
    print(x_train.shape)
    #x_test.head()
    print(x_test.shape)
    model = lm().fit(x_train,y_train)
    prediction = model.predict(x_test)
    plt.scatter(y_test,prediction)
    plt.show()

def main():
    dataset = input_data()
    train(dataset)

main()