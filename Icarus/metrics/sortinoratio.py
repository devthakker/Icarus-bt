import numpy as np
import pandas as pd

class SortinoRatio:
    """
    Sortino Ratio
    The Sortino ratio is a measure of risk-adjusted return.
    It describes how much excess return you receive for the volatility of holding a riskier asset.
    The higher the Sortino ratio, the better the risk-adjusted return.
    
    The Sortino ratio is similar to the Sharpe ratio, except it uses downside deviation instead of standard deviation in the denominator.
    
    Attributes
        returns (list): A list of returns
        risk_free_rate (float): The risk-free rate of return
        """
    def __init__(self, returns, risk_free_rate=.02):
        self.returns = pd.DataFrame(returns, columns=['Daily'])
        self.returns['Pct'] = self.returns['Daily'].pct_change(1)
        self.risk_free_rate = risk_free_rate

    def calculate(self):
        """
        Calculates the Sortino ratio of a portfolio
        """
        downside_returns = np.where(self.returns['Pct'] < 0, self.returns['Pct'], 0)
        average_excess_return = np.mean(self.returns['Pct'])
        downside_deviation = np.std(downside_returns)
        sortino_ratio = average_excess_return / downside_deviation if downside_deviation != 0 else 0
        return sortino_ratio
