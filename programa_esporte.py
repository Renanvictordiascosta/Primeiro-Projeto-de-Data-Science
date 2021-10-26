#Fazer um programa em Python que
#Leia uma planilha no Excel referente a esportes praticados e faça:
#um histograma mostrando a idade dos praticantes do gênero masculino de cada esporte
#um histograma mostrando a idade dos praticantes do gênero feminino de cada esporte
#um histograma mostrando a idade dos praticantes de cada esporte de ambos os gêneros
#PS: Modifique o comando pandas na linha 12 corretamente, para se adequar ao caminho correto a ser percorrido para chegar na planilha do excel, no seu computador.

import matplotlib.pyplot as plot #biblioteca para mostrar os gráficos
import pandas as pd #biblioteca para ler a planilha
from time import sleep #biblioteca para dar um tempo de descanso entre os gráficos

dados = pd.read_excel("/Users/renanvictordiascosta/Desktop/EsportesX.xlsx") #planilha sendo importada

index_dados = dados[dados["Esporte"] != "Natação"].index #informando o que será filtrado
z = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
z.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS NADADORES DE AMBOS OS GÊNEROS") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(5) #descanso entre esse e o próximo gráfico

index_dados = dados[(dados["Gênero"] == "Masculino") | (dados["Esporte"] != "Natação")].index #informando o que será filtrado
x = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
x.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS NADADORES DO GÊNERO FEMININO") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(5) #descanso entre esse e o próximo gráfico

index_dados = dados[(dados["Gênero"] == "Feminino") | (dados["Esporte"] != "Natação")].index #informando o que será filtrado
y = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
y.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS NADADORES DO GÊNERO MASCULINO") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(10) #descanso entre os gráficos de esportes diferentes

index_dados = dados[dados["Esporte"] != "Vôlei"].index #informando o que será filtrado
z = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
z.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS JOGADORES DE VÔLEI DE AMBOS OS GÊNEROS") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(5) #descanso entre esse e o próximo gráfico

index_dados = dados[(dados["Gênero"] == "Masculino") | (dados["Esporte"] != "Vôlei")].index #informando o que será filtrado
x = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
x.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS JOGADORES DE VÔLEI DO GÊNERO FEMININO") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(5) #descanso entre esse e o próximo gráfico

index_dados = dados[(dados["Gênero"] == "Feminino") | (dados["Esporte"] != "Vôlei")].index #informando o que será filtrado
y = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
y.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS JOGADORES DE VÔLEI DO GÊNERO MASCULINO") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(10) #descanso entre os gráficos de esportes diferentes

index_dados = dados[dados["Esporte"] != "Corrida"].index #informando o que será filtrado
z = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
z.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS CORREDORES DE AMBOS OS GÊNEROS") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(5) #descanso entre esse e o próximo gráfico

index_dados = dados[(dados["Gênero"] == "Masculino") | (dados["Esporte"] != "Corrida")].index #informando o que será filtrado
x = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
x.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS CORREDORES DO GÊNERO FEMININO") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(5) #descanso entre esse e o próximo gráfico

index_dados = dados[(dados["Gênero"] == "Feminino") | (dados["Esporte"] != "Corrida")].index #informando o que será filtrado
y = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
y.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS CORREDORES DO GÊNERO MASCULINO") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(10) #descanso entre os gráficos de esportes diferentes

index_dados = dados[dados["Esporte"] != "Artes Marciais"].index #informando o que será filtrado
z = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
z.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS LUTADORES DE AMBOS OS GÊNEROS") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(5) #descanso entre esse e o próximo gráfico

index_dados = dados[(dados["Gênero"] == "Masculino") | (dados["Esporte"] != "Artes Marciais")].index #informando o que será filtrado
x = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
x.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS LUTADORES DO GÊNERO FEMININO") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(5) #descanso entre esse e o próximo gráfico

index_dados = dados[(dados["Gênero"] == "Feminino") | (dados["Esporte"] != "Artes Marciais")].index #informando o que será filtrado
y = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
y.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS LUTADORES DO GÊNERO MASCULINO") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(10) #descanso entre os gráficos de esportes diferentes

index_dados = dados[dados["Esporte"] != "Futebol"].index #informando o que será filtrado
z = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
z.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS JOGADORES DE FUTEBOL DE AMBOS OS GÊNEROS") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(5) #descanso entre esse e o próximo gráfico

index_dados = dados[(dados["Gênero"] == "Masculino") | (dados["Esporte"] != "Futebol")].index #informando o que será filtrado
x = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
x.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS JOGADORES DE FUTEBOL DO GÊNERO FEMININO") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(5) #descanso entre esse e o próximo gráfico

index_dados = dados[(dados["Gênero"] == "Feminino") | (dados["Esporte"] != "Futebol")].index #informando o que será filtrado
y = dados.drop(index_dados) #assumindo uma variável para receber o valor com informações filtradas
y.hist(column=["Idade"], bins=75) #chamando essa variável para informar o tipo de gráfico pedido, o tamanho e o as informações buscadas
plot.title("IDADE DOS JOGADORES DE FUTEBOL DO GÊNERO MASCULINO") #dar um título ao gráfico
plot.show() #mostrar o gráfico já devidamente tratado
sleep(10) #descanso entre os gráficos de esportes diferentes
