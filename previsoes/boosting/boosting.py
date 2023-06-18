import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

df_meteorologia = pd.read_csv('meteorologia\\acumulados\\A601.csv')  
df_precos_alface = pd.read_csv('alface\\alface_corrigido.csv') 

df_precos_alface['data'] = pd.to_datetime(df_precos_alface['data'])
df_meteorologia['data'] = pd.to_datetime(df_meteorologia['data'])
df_precos_alface.drop(columns=['preco','Unnamed: 0'], inplace = True)

df_merged = pd.merge(df_meteorologia, df_precos_alface, on='data')
df_merged.drop(columns=['data'], inplace = True)

print(type(df_merged))
print(" ")
X = df_merged.drop('preco_corrigido', axis=1)
y = df_merged['preco_corrigido']

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Criar e treinar o modelo de Gradient Boosting
model = GradientBoostingRegressor()
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model.predict(X_test)

# Avaliar o desempenho do modelo
mse = mean_squared_error(y_test, y_pred)
print('Erro quadrático médio:', mse)

plt.plot(range(len(y_test)), y_test, label='Preço Real')
plt.plot(range(len(y_test)), y_pred, label='Previsão')
plt.xlabel('Índice do Teste')
plt.ylabel('Preço do Alface')
plt.legend()
plt.show()