import numpy as np

class SortinoRatio :
    def __init__(self, returns, risk_free_rate):
        self.returns = returns
        self.risk_free_rate = risk_free_rate

    def calculate(self):
        excess_returns = self.returns - self.risk_free_rate
        downside_returns = np.where(excess_returns < 0, excess_returns, 0)
        average_excess_return = np.mean(excess_returns)
        downside_deviation = np.std(downside_returns)

        sortino_ratio = average_excess_return / downside_deviation if downside_deviation != 0 else 0
        return sortino_ratio
