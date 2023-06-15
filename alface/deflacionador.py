import pandas as pd

alface_path = "alface\\alface_rio.CSV"
IPCA_path = "alface\\ipca_acumulado.csv"

def gera_df(alface_path, IPCA_path):
    df_alface = pd.read_csv(alface_path)
    df_ipca = pd.read_csv(IPCA_path) 

    df_alface['data'] = pd.to_datetime(df_alface['data'])
    df_ipca['data'] = pd.to_datetime(df_ipca['data'])

    df_ipca.set_index('data', inplace=True)
    ipca_diario = df_ipca.asfreq('D', method='ffill')
    
    ipca_diario.pop(ipca_diario.columns[0])
    df_merged = df_alface.merge(ipca_diario, on='data', how='inner')
    return df_merged

df = gera_df(alface_path, IPCA_path)
df.drop("IPCA",axis=1,inplace=True)
df['preco_corrigido'] = df['preco']/df['IPCA acumulado']
df.drop("IPCA acumulado",axis=1,inplace=True)
df.to_csv("alface\\alface_corrigido.csv")
print(df.head())