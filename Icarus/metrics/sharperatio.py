import pandas as pd

class SharpeRatio:
    """
    Sharpe Ratio
    The Sharpe ratio is a measure of risk-adjusted return.
    It describes how much excess return you receive for the volatility of holding a riskier asset.
    The higher the Sharpe ratio, the better the risk-adjusted return.
    
    Attributes
        returns (list): A list of returns
        risk_free_rate (float): The risk-free rate of return
    """
    def __init__(self, returns, risk_free_rate=.02):
        self.portfolio = pd.DataFrame(returns, columns=['Daily'])
        self.portfolio['Pct'] = self.portfolio['Daily'].pct_change(1)
        self.risk_free_rate = risk_free_rate

    def calculate(self):
        """
        Calculates the Sharpe ratio of a portfolio
        """
        sharpe_ratio = (self.portfolio['Pct'].mean() / self.portfolio['Pct'].std())*(252**.5)
        return sharpe_ratio


