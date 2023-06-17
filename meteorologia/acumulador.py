import pandas as pd


def acumula(estacao):
    file_path ="meteorologia\\concatenados_diarios\\"+estacao+".CSV"
    df = pd.read_csv(file_path, encoding = "Latin-1", delimiter = ",")
    df_acumulado = pd.DataFrame()
    df_acumulado['data'] = df['data']
    df_acumulado['precipitacao'] = df['precipitacao'].rolling(window=130, min_periods=1).sum()
    df_acumulado['pressao_atmosferica'] = df['pressao_atmosferica'].rolling(window=130, min_periods=1).sum()
    df_acumulado['radiacao'] = df['radiacao'].rolling(window=130, min_periods=1).sum()
    df_acumulado['umidade_relativa'] = df['umidade_relativa'].rolling(window=130, min_periods=1).sum()
    df_acumulado['velocidade_media_vento'] = df['velocidade_media_vento'].rolling(window=130, min_periods=1).sum()
    df_acumulado.to_csv("meteorologia\\acumulados\\"+estacao+".csv")
    print(estacao + " feita")

estacoes = ["A601","A602","A603","A604","A606","A607","A608","A609","A610","A611","A618","A619","A620","A621","A624","A625","A626","A627","A628","A629","A630","A635","A636","A652","A659","A667"]

for estacao in estacoes:
    acumula(estacao)
