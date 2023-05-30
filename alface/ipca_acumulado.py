import pandas as pd

IPCA_path = "alface\\IPCA-15.csv"

df_ipca = pd.read_csv(IPCA_path) 
df_ipca['data'] = df_ipca['data'].astype(str)
df_ipca['IPCA'] = df_ipca['IPCA'].str.replace(',', '.').astype(float)
df_ipca['data'] = pd.to_datetime(df_ipca['data'], format='%Y.%m')
df_ipca.set_index('data', inplace=True)
data_inicial = pd.to_datetime('2015-01-01')
data_final = pd.to_datetime('2022-12-31')
df_ipca = df_ipca.loc[(df_ipca['data'] >= data_inicial) & (df_ipca['data'] <= data_final)]
df_ipca['IPCA acumulado'] = (1 + df_ipca['IPCA'])
print(df_ipca)
df_ipca.pop("IPCA")
df_ipca.to_csv('alface\\ipca_acumulado.csv', sep=';', decimal=',')
print(df_ipca)