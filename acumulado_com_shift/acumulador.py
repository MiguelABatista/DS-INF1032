import pandas as pd


def acumula(estacao):
    file_path = "meteorologia\\concatenados_diarios\\"+estacao+".CSV"
    colunas = ['precipitacao', 'pressao_atmosferica', 'pressao_max', 'pressao_min', 'radiacao', 'temperatura_do_ar', 'temperatura_orvalho', 'temperatura_max', 'temperatura_min', 'temperatura_orvalho_max', 'temperatura_orvalho_min', 'umidade_max', 'umidade_min', 'umidade_relativa', 'direcao_vento', 'rajada_max', 'velocidade_media_vento']

    df = pd.read_csv(file_path, encoding = "Latin-1", delimiter = ",")
    df_acumulado = pd.DataFrame()
    df_acumulado['data'] = df['data']
    df_acumulado.set_index('data')
    for coluna in colunas:
        df_acumulado[coluna] = (df[coluna].rolling(window=120, min_periods=1).sum()).shift(10)
    df_acumulado.to_csv("folder_do_thomaz\\acumulado_com_shift\\"+estacao+".csv")
    print(estacao + " feita")

estacoes = ["A601","A602","A603","A604","A606","A607","A608","A609","A610","A611","A618","A619","A620","A621","A624","A625","A626","A627","A628","A629","A630","A635","A636","A652","A659","A667"]

for estacao in estacoes:
    acumula(estacao)
