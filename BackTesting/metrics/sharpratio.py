import numpy as np

class SharpeRatioCalculator:
    def __init__(self, returns, risk_free_rate=.02):
        self.returns = returns
        self.risk_free_rate = risk_free_rate

    def calculate(self):
        excess_returns = self.returns - self.risk_free_rate
        average_excess_return = np.mean(excess_returns)
        std_deviation = np.std(self.returns)

        sharpe_ratio = average_excess_return / std_deviation if std_deviation != 0 else 0
        return sharpe_ratio


