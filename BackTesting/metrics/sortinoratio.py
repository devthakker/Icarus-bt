import numpy as np
import pandas as pd

class SortinoRatio :
    def __init__(self, returns, risk_free_rate=.02):
        self.returns = pd.DataFrame(returns, columns=['Daily'])
        self.returns['Pct'] = self.returns['Daily'].pct_change(1)
        self.risk_free_rate = risk_free_rate

    def calculate(self):
        downside_returns = np.where(self.returns['Pct'] < 0, self.returns['Pct'], 0)
        average_excess_return = np.mean(self.returns['Pct'])
        downside_deviation = np.std(downside_returns)
        sortino_ratio = average_excess_return / downside_deviation if downside_deviation != 0 else 0
        return sortino_ratio
