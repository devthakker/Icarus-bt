class CalmarRatio:
    def __init__(self, returns):
        self.returns = returns

    def calculate(self):
        annualized_return = self.calculate_annualized_return()
        max_drawdown = self.calculate_max_drawdown()

        calmar_ratio = annualized_return / max_drawdown if max_drawdown != 0 else 0
        return calmar_ratio

    def calculate_annualized_return(self):
        num_periods = len(self.returns)
        total_return = (1 + sum(self.returns)) ** (1 / num_periods) - 1
        annualized_return = (1 + total_return) ** 252 - 1  # Assuming 252 trading days in a year
        return annualized_return

    def calculate_max_drawdown(self):
        peak = self.returns[0]
        drawdown = 0.0
        max_drawdown = 0.0

        for ret in self.returns:
            if ret > peak:
                peak = ret
                drawdown = 0.0
            else:
                drawdown = (peak - ret) / peak
                if drawdown > max_drawdown:
                    max_drawdown = drawdown

        return max_drawdown
