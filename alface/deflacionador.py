import pandas as pd

alface_path = "alface\\alface_rio.CSV"
IPCA_path = "alface\\IPCA-15.csv"
# Carregando os conjuntos de dados
df_alface = pd.read_csv(alface_path)
df_ipca = pd.read_csv(IPCA_path) 

df_alface['data'] = pd.to_datetime(df_alface['data'])
df_ipca['data'] = pd.to_datetime(df_ipca['data'])

data_inicial = pd.to_datetime('2015-01-01')
data_final = pd.to_datetime('2022-12-31')

df_ipca = df_ipca.loc[(df_ipca['data'] >= data_inicial) & (df_ipca['data'] <= data_final)]

df_merged = df_alface.merge(df_ipca, on='data', how='inner')

variacao_ipca = (df_merged['IPCA'] - df_merged.loc[df_merged['data'] == data_inicial, 'IPCA'].values[0]) / df_merged.loc[df_merged['data'] == data_inicial, 'IPCA'].values[0] * 100

print(variacao_ipca)
# Aplique a variação percentual do IPCA ao preço do alface
df_merged['alface_deflacionado'] = df_merged['alface'] * (1 + (variacao_ipca / 100))

#print(df_merged[['data', 'alface', 'IPCA', 'alface_deflacionado']])
