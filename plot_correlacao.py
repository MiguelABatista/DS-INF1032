import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Crie uma matriz de exemplo contendo números entre -1 e 1
df = pd.read_csv("correlacao_2.csv")

# Crie o mapa de calor usando seaborn
df = df.drop(df.columns[0], axis=1)
sns.heatmap(df, cmap='coolwarm', vmin=-1, vmax=1)

# Adicione rótulos aos eixos x e y
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exiba o mapa de calor
plt.show()
