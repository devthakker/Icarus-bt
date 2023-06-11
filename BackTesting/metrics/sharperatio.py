import pandas as pd

class SharpeRatio:
    def __init__(self, returns, risk_free_rate=.02):
        self.portfolio = pd.DataFrame(returns, columns=['Daily'])
        self.portfolio['Pct'] = self.portfolio['Daily'].pct_change(1)
        self.risk_free_rate = risk_free_rate

    def calculate(self):
        sharpe_ratio = (self.portfolio['Pct'].mean() / self.portfolio['Pct'].std())*(252**.5)
        return sharpe_ratio


