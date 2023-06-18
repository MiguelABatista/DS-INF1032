import pandas as pd
import numpy as np
import statsmodels.api as sm
import os
import seaborn as sns

lettuce_prices = pd.read_csv('/content/alface_corrigido.csv')
coeficientes = pd.DataFrame(columns = ["Estacao","Variavel", "Coeficiente"])

lettuce_prices['data'] = pd.to_datetime(lettuce_prices['data'])
lettuce_prices.set_index('data', inplace=True)

for file_name in os.listdir(folder_path):
    if file_name.endswith('.CSV'):
        # Extract the station name from the file name (assuming the file name format is 'station_name.csv')
        station = file_name[0:4]
        
        # Load the weather data for the current station
        file_path = os.path.join(folder_path, file_name)
        station_data = pd.read_csv(file_path)

        station_data["data_hora"] = pd.to_datetime(station_data["data_hora"])
        lettuce_prices["data"] = pd.to_datetime(lettuce_prices["data"])
        station_data.set_index("data_hora", inplace= True)
        
        daily_averages = station_data.resample('D').mean().reset_index()
        daily_averages.rename(columns={"data_hora":"data"}, inplace = True)

        daily_averages = daily_averages.shift(100)
        # Merge with lettuce prices data on the 'Date' column
        daily_averages = daily_averages.merge(lettuce_prices, on='data')
        daily_averages.dropna(inplace = True)
        daily_averages.drop(columns=["Unnamed: 0","data"], inplace = True)

        # Prepare the X (weather) and y (lettuce prices) variables for regression
        X = daily_averages[daily_averages.columns[0:-4]]  # Exclude the station column
        y = daily_averages['preco_corrigido']
        
        # Add a constant column to the X variables for the intercept
        X = sm.add_constant(X)
        
        # Perform the OLS regression
        model = sm.OLS(y, X)
        results = model.fit()
        
        # Extract the coefficients and add them as a row in the coefficients DataFrame
        coefficients.loc[station] = [station] + list(results.params[1:])  # Include the 'Station' column

sns.heatmap(coefficients.iloc[:,1:], annot=False, cmap='coolwarm')
