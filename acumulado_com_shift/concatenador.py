import pandas as pd
import os
from pathlib import Path

directory = r'C:\Users\thoma\OneDrive\Documentos\GitHub\DS-INF1032\acumulado_com_shift\acumulado_com_shift'

all_data = pd.DataFrame()

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(directory, filename))
        df.drop('Unnamed: 0', inplace=True, axis=1)

        df.columns = [f'{x}_{Path(filename).stem}' for x in df.columns]

        all_data = pd.concat([df, all_data], axis=1)

all_data.to_pickle(r'C:\Users\thoma\OneDrive\Documentos\GitHub\DS-INF1032\acumulado_com_shift\concatenado.zip')
