import pandas as pd

alface_path = "C:\\Users\\u2112200\\Documents\DS\\alface_rio.CSV"
IPCA_path = "C:\\Users\\u2112200\\Documents\\DS\\IPCA-15.csv"
# Carregando os conjuntos de dados
df_alface = pd.read_csv(alface_path)
df_ipca = pd.read_csv(IPCA_path) 

df_alface['data_hora'] = pd.to_datetime(df_alface['data_hora'])
df_ipca['data_hora'] = pd.to_datetime(df_ipca['data_hora'])

data_inicial = pd.to_datetime('2015-01-01')
data_final = pd.to_datetime('2022-12-31')

df_ipca = df_ipca.loc[(df_ipca['data_hora'] >= data_inicial) & (df_ipca['data_hora'] <= data_final)]

df_merged = df_alface.merge(df_ipca, on='data_hora', how='inner')

variacao_ipca = (df_merged['IPCA'] - df_merged.loc[df_merged['data_hora'] == data_inicial, 'IPCA'].values[0]) / df_merged.loc[df_merged['data_hora'] == data_inicial, 'IPCA'].values[0] * 100

print(variacao_ipca)
# Aplique a variação percentual do IPCA ao preço do alface
df_merged['alface_deflacionado'] = df_merged['alface'] * (1 + (variacao_ipca / 100))

#print(df_merged[['data_hora', 'alface', 'IPCA', 'alface_deflacionado']])
