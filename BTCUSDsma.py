import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter

BTC_USD = yf.download("BTC-USD", start='2021-01-01', end='2022-01-01', interval='1d')









BTC_USD['SMA-15'] = BTC_USD['Close'].rolling(window = 15, min_periods =1).mean()
BTC_USD['SMA-9'] = BTC_USD['Close'].rolling(window = 9, min_periods =1).mean()
BTC_USD['SMA-30'] = BTC_USD['Close'].rolling(window = 30, min_periods =1).mean()




daldaldal = pd.DataFrame(index=BTC_USD.index)
short_interval = 10
long_interval = 40

daldaldal['Short'] = BTC_USD['Close'].rolling(window=short_interval, min_periods=1).mean()
daldaldal['Long'] = BTC_USD['Close'].rolling(window=long_interval, min_periods=1).mean()

daldaldal['Sinyal'] = 0.0
daldaldal['Sinyal'] = np.where(daldaldal['Short'] > daldaldal['Long'], 1.0, 0.0)

daldaldal['Pozisyon'] = daldaldal['Sinyal'].diff()








fig, grp = plt.subplots(dpi=750)

date_format = DateFormatter("%y-%h-%d")
grp.xaxis.set_major_formatter(date_format)
grp.tick_params(axis="x", labelsize = 10)
fig.autofmt_xdate()


grp.plot(BTC_USD['Close'], lw = 1, label = "Closing Price")
grp.plot(BTC_USD['SMA-9'], lw = 0.75, alpha = 0.75, label = "9 days sma")
grp.plot(BTC_USD['SMA-15'], lw = 0.75, alpha = 0.75, label = "15 days sma")
grp.plot(BTC_USD['SMA-30'], lw = 0.75, alpha = 0.75, label = "30 days sma")

grp.plot(daldaldal['Short'], lw=0.75, alpha=0.75, color='orange', label='şort sma')
grp.plot(daldaldal['Long'], lw=0.75, alpha=0.75, color='blue', label='long sma')

grp.plot(daldaldal.loc[daldaldal['Pozisyon']== 1.0].index, daldaldal.Short[daldaldal['Pozisyon']==1.0], marker=6, ms=4, linestyle='none', color='green') 
grp.plot(daldaldal.loc[daldaldal['Pozisyon']== -1.0].index, daldaldal.Short[daldaldal['Pozisyon']==-1.0], marker=7, ms=4, linestyle='none', color='red' )



grp.set_ylabel("btc/usdt")
grp.set_title("btc-usd graph")
grp.grid()
grp.legend()
plt.show()



""""""""""
for test
"""""""


baslangic_bakiye = 1000.0
deneme = pd.DataFrame(index = daldaldal.index)
deneme['donus'] = BTC_USD['Close'] / BTC_USD['Close'].shift(1)
deneme['alg_dönüş'] = np.where(daldaldal.Sinyal == 1, deneme.donus, 1.0)
deneme.['bakiye'] = baslangic_bakiye * deneme.donus.cumprod()

grp.plot(baslangic_bakiye*deneme.donus.cumprod(), lw=0.75, alpha = 0.75, label = "if hodl")
grp.plot(deneme['bakiye'], lw=0.75, alpha=0.75, label='sma yöntemi')
plt.show()
"""


