import pandas as pd
import os
import datetime

def hourly_to_daily(estacao):
    file_path = 'meteorologia\\concatenados\\'+estacao+'.CSV'
    df = pd.read_csv(file_path, encoding = "Latin-1", delimiter = ",")
    df['data_hora'] = pd.to_datetime(df['data_hora'])
    df.set_index('data_hora', inplace=True)

    df_diario = df.resample('D').mean()  
    df_diario.reset_index(inplace=True)
    df_diario.rename(columns={'data_hora': 'data'}, inplace = True)
    df_diario.to_csv("meteorologia\\concatenados_diarios\\"+estacao+".CSV", index=False)
    print(estacao + " feita")

estacoes = ["A601","A602","A603","A604","A606","A607","A608","A609","A610","A611","A618","A619","A620","A621","A624","A625","A626","A627","A628","A629","A630","A635","A636","A652","A659","A667"]


for estacao in estacoes:    
    hourly_to_daily(estacao)