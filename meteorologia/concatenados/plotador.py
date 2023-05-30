import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

path = "C:\\Users\\Miguel\\Downloads\\ds\\DS\\por_estacao\\concatenados"
for filename in os.listdir(path):
  if filename.endswith(".CSV"):
      data = pd.read_csv(os.path.join(path,filename), encoding = "Latin-1", delimiter = ",", header = 8)
      data.columns = ['precipitacao', 'pressao atmosferica', 'pressao_max', 'pressao_min', 'radiacao',
                'temperatura_do_ar', 'temperatura_orvalho', 'temperatura_max', 'temperatura_min', 'temperatura_orvalho_max',
                'temperatura_orvalho_min', 'umidade_max', 'umidade_min', 'umidade_relativa', 'direcao_vento', 'rajada_max',
                'velocidade_media_vento', 'data_hora']

      sns.set(style="darkgrid")
      plt.figure(figsize=(16,6))
      sns.lineplot(x='data_hora', y='temperatura_do_ar', data=data, label='Temperature')
      sns.lineplot(x='data_hora', y='precipitacao', data=data, label='Rain')
      plt.title('Temperature and Rain over time')
      plt.xlabel('Year')
      plt.ylabel('Temperature (°C) / Rain (mm)')
      plt.xlim(2015, None)
      plt.legend()
      plt.show() 