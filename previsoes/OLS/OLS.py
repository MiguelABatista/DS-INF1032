import pandas as pd
import statsmodels.api as sm
import os
import seaborn as sns
import matplotlib.pyplot as plt

weather_data = "file pra uma estacao qualquer"
lettuce_prices = "file pro preco do alface"

lettuce_prices['data'] = pd.to_datetime(lettuce_prices['data'])
lettuce_prices.set_index('data', inplace=True)

folder_path = "path pros dados meteo"

coefficients = pd.DataFrame(columns= ["estacao"]+list(weather_data.columns))
coefficients = coefficients.drop(columns=["Unnamed: 0", "data"])

pvalues = pd.DataFrame(columns = ["estacao"]+list(weather_data.columns))
pvalues = pvalues.drop(columns=["Unnamed: 0", "data"])

for file_name in os.listdir(folder_path):
    if file_name.endswith('.csv'):
      station = file_name[0:4]

      file_path = os.path.join(folder_path, file_name)
      station_data = pd.read_csv(file_path)

      station_data["data"] = pd.to_datetime(station_data["data"])
      lettuce_prices["data"] = pd.to_datetime(lettuce_prices["data"])
      station_data.set_index("data", inplace= True)

      station_data = station_data.merge(lettuce_prices, on='data')
      station_data.dropna(inplace = True)
      station_data = station_data.drop(columns=['Unnamed: 0_x', 'data'])

      X = station_data[station_data.columns[0:-3]] 
      y = station_data['preco_corrigido']

      X = sm.add_constant(X)

      model = sm.OLS(y, X)
      results = model.fit()

      residual = results.resid
        

      coefficients.loc[station] = [station] + list(results.params[1:])

      pvalor = results.pvalues
      pvalues.loc[station] = [station] + list(results.pvalues[1:])

sns.heatmap(coefficients.iloc[:, 1:], annot=False, cmap='coolwarm')
