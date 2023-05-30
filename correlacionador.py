import pandas as pd
from scipy.stats import spearmanr

def correlacionadores(estacao):
    colunas = ['precipitacao', 'pressao_atmosferica', 'pressao_max', 'pressao_min', 'radiacao', 'temperatura_do_ar', 'temperatura_orvalho', 'temperatura_max', 'temperatura_min', 'temperatura_orvalho_max', 'temperatura_orvalho_min', 'umidade_max', 'umidade_min', 'umidade_relativa', 'direcao_vento', 'rajada_max', 'velocidade_media_vento']
    meteorologia_path = 'C:\\Users\\Miguel\\Downloads\\ds\\DS\\por_estacao\\concatenados\\'+estacao+'.CSV'
    preco_alface_path = 'C:\\Users\\Miguel\\Downloads\\ds\\DS\\por_estacao\\dados_diarios\\alface_rio.CSV'
    df_meteorologia = pd.read_csv(meteorologia_path, encoding = "Latin-1", delimiter = ",")
    df_preco_alface = pd.read_csv(preco_alface_path, encoding = "Latin-1", delimiter = ",")
    df_meteorologia['data_hora'] = pd.to_datetime(df_meteorologia['data_hora'])
    df_preco_alface['data_hora'] = pd.to_datetime(df_preco_alface['data_hora'])
    
    df_combinado = pd.merge(df_meteorologia, df_preco_alface, on='data_hora')

    correlations = {}
    for coluna in colunas:
        correlation = df_combinado[coluna].corr(df_combinado['preco'], method='spearman')
        correlations[coluna] = correlation
    return correlations

estacoes = ["A601","A602","A603","A604","A606","A607","A608","A609","A610","A611","A618","A619","A620","A621","A624","A625","A626","A627","A628","A629","A630","A635","A636","A652","A659","A667"]

df_correlacoes = pd.DataFrame(index=estacoes)

for estacao in estacoes:
    correlacoes = correlacionadores(estacao)
    for coluna, correlacao in correlacoes.items():
        df_correlacoes.loc[estacao, coluna] = correlacao

df_correlacoes['MediaModuloCorrelacoes'] = df_correlacoes.abs().mean(axis=1)
df_correlacoes.reset_index(inplace=True)
df_correlacoes.to_csv('C:\\Users\\Miguel\\Downloads\\ds\\DS\\por_estacao\\dados_diarios\\correlacao.CSV', index=False)


print(df_correlacoes.head())