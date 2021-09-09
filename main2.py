import yfinance as yf

acao1 = yf.download('PETR4.SA', period = '1y')['Adj Close']
acao2 = yf.download('ITUB4.SA', period = '1y')['Adj Close']

acao1.plot()
acao2.plot()