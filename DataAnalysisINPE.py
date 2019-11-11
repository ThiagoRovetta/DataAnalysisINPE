# Feito por: Thiago Vinicius Ferrerira Rovetta
#!/usr/bin/env python
# coding: utf-8

# Importando as bibliotecas utilizadas
import requests
import pandas as pd
import matplotlib.pyplot as plt

low_memory=False

# abrindo a página e coletando os dados através de uma request GET e transformando em formato JSON
r = requests.get('http://teste-inpe.herokuapp.com/').json()

# montando um DataFrame
df = pd.DataFrame(data=r)

# criando um arquivo CSV para melhor visualização dos dados
df.to_csv('teste.csv', header=['id', 'comp_bx', 'comp_by', 'comp_bz', 'comp_bt', 'lon_gsm', 'lat_gsm', 'density', 'speed', 'temperature'], index=None)

# com base nos valores vistos no arquivo CSV, filtrei os valores aparentemente errados
df = df.query('(comp_bx < 999999999) and (comp_by < 999999999) and (comp_bz < 999999999) and (comp_bt < 999999999) and (lon_gsm < 999999999) and (lat_gsm < 999999999) and (density < 999999999) and (speed < 999999999) and (temperature < 999999999)')[['id', 'comp_bx', 'comp_by', 'comp_bz', 'comp_bt', 'lon_gsm', 'lat_gsm', 'density', 'speed', 'temperature']]

# mostra as 5 primeiras linhas do dataframe 
print(df.head())

# mostra algumas informações estatísticas dos dados
print(df.describe())

# A seguir, inicio a criação dos gráficos.

# comando usado para aumentar o tamanho das figuras
plt.rcParams['figure.figsize'] = (10,7)

# criando o gráfico da frequência da densidade dos dados
plt.figure(1)
plt.hist(df['density'], bins=range(1, 10, 1), cumulative = False)
plt.title('Distribuição de densidades', fontsize=18)
plt.xlabel('Densidade (unidades de densidade)', fontsize=18)
plt.ylabel('Frequência', fontsize=18)

# criando o gráfico da frequência da velocidade dos dados
plt.figure(2)
plt.hist(df['speed'], bins=range(350, 460, 5))
plt.title('Distribuição de velocidades', fontsize=18)
plt.xlabel('Velocidade (unidades de velocidade)', fontsize=18)
plt.ylabel('Frequência', fontsize=18)

# criando o gráfico da frequência da temperatura dos dados
plt.figure(3)
plt.hist(df['temperature'], bins=range(10000, 185000, 5000))
plt.title('Distribuição de temperaturas', fontsize=18)
plt.xlabel('Temperatura (unidades de temperatura)', fontsize=18)
plt.ylabel('Frequência', fontsize=18)

# criando o gráfico da latitude e longitude dos dados
plt.figure(4)
plt.scatter(df['lon_gsm'], df['lat_gsm'])
plt.xlim(0,370)
plt.ylim(-90,50)
plt.xlabel('Longitude(°)', fontsize=18)
plt.ylabel('Latitude (°)', fontsize=18)
plt.title('Ocorrência dos dados conforme sua latitude e longitude', fontsize=18)
plt.show()
