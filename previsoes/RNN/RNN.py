import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from datetime import datetime

df_meteorologia = pd.read_csv('meteorologia\\acumulados\\A601.csv')  
df_precos_alface = pd.read_csv('alface\\alface_corrigido.csv') 

df_precos_alface['data'] = pd.to_datetime(df_precos_alface['data'])
df_meteorologia['data'] = pd.to_datetime(df_meteorologia['data'])
df_precos_alface.drop(columns=['preco','Unnamed: 0'], inplace = True)

df_merged = pd.merge(df_meteorologia, df_precos_alface, on='data')
df_merged['dias'] = (df_merged['data'] - pd.to_datetime('2015-01-01')).dt.days
df_merged.drop(columns=['data'], inplace = True)


# Dividir os dados em recursos (X) e alvo (y)
X = df_merged.drop('preco_corrigido', axis=1).values
y = df_merged['preco_corrigido'].values

# Normalizar os dados
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y.reshape(-1, 1))

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, shuffle=False)

# Reshape dos dados para o formato adequado para a entrada da RNN
X_train = np.reshape(X_train, (X_train.shape[0], 1, X_train.shape[1]))
X_test = np.reshape(X_test, (X_test.shape[0], 1, X_test.shape[1]))

# Construir o modelo da RNN (LSTM)
model = Sequential()
model.add(LSTM(units=50, input_shape=(1, X.shape[1])))
model.add(Dense(units=1))

# Compilar o modelo
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# Definir Early Stopping para evitar overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

# Treinar o modelo
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test), callbacks=[early_stopping])

# Avaliar o modelo
loss = model.evaluate(X_test, y_test)
print('Loss:', loss)

# Fazer previsões com o modelo treinado
predictions = model.predict(X_test)

# Desnormalizar as previsões
predictions = scaler.inverse_transform(predictions)

# Exibir as previsões
print('Previsões:', predictions)

# Plotar o histórico de treinamento
import matplotlib.pyplot as plt

plt.plot(y_test, label='Valores de Teste')
plt.plot(predictions, label='Previsões')
plt.xlabel('Índice')
plt.ylabel('Valor')
plt.legend()
plt.show()
