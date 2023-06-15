import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter, YearLocator

alface_path = "alface\\alface_corrigido.csv"

df = pd.read_csv(alface_path)
price1 = df['preco']
price2 = df["preco_corrigido"]
data = df['data']
data = pd.to_datetime(df['data'])
print(data)
plt.plot(data,price1, label='Normal')
plt.plot(data,price2, label='Corrigido')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.title('Price Comparison')

ax = plt.gca()
ax.xaxis.set_major_locator(YearLocator())
ax.xaxis.set_major_formatter(DateFormatter('%Y'))

plt.show()
