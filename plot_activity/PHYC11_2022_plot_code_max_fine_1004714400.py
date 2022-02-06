#imports
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# importing stock data
start_date = '1999-05-07'
end_date = '2022-01-31'
ticker1 = 'qqq'
ticker2 = 'spy'
data1 = yf.download(ticker1,start_date, end_date)
#data1.tail #shows data format
qqq = data1['Open']
#spy = data2['Open']
#dates = data1['Date']

#save data output to file
#np.savetxt('plot_act_data', qqq)
data1.to_excel("data.xlsx") #exports data .csv is not supported :(
plt.figure(figsize=(10.0, 4.0))
plt.plot(qqq, color ='green')
plt.title('QQQ Price')
plt.xlabel('Time (Years)')
plt.ylabel('Price (USD)')
plt.rcParams.update({'font.size': 15})
#txt="Caption"
#plt.figtext(0.5, 0.0, txt, wrap=True, horizontalalignment='center', fontsize=15)
plt.tight_layout()
plt.show()
plt.savefig('QQQ_stock_data.pdf')
