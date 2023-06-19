import pandas as pd
import os
from pathlib import Path

directory = r'C:\Users\thoma\OneDrive\Documentos\GitHub\DS-INF1032\acumulado_com_shift\acumulado_com_shift'

all_data = pd.DataFrame()

for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(directory, filename))
        df.drop('Unnamed: 0', inplace=True, axis=1)

        df['filename'] = Path(filename).stem

        all_data = pd.concat([df, all_data])

all_data.to_csv(r'C:\Users\thoma\OneDrive\Documentos\GitHub\DS-INF1032\acumulado_com_shift\concatenado.csv')
