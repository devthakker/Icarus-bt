class CalmarRatio:
    """
    Calmar Ratio = Annualized Return / Max Drawdown
    
    The Calmar ratio is a measure of risk-adjusted return based on the maximum drawdown.
    It measures the annualized return of an investment relative to its maximum drawdown.
    The higher the Calmar ratio, the better the risk-adjusted return.
    """
    def __init__(self, returns):
        self.returns = returns

    def calculate(self):
        """
        Calculates the Calmar ratio of a portfolio
        """
        annualized_return = self.calculate_annualized_return()
        max_drawdown = self.calculate_max_drawdown()

        calmar_ratio = annualized_return / max_drawdown if max_drawdown != 0 else 0
        return calmar_ratio

    def calculate_annualized_return(self):
        """
        Calculates the annualized return of a portfolio
        """
        num_periods = len(self.returns)
        total_return = (1 + sum(self.returns)) ** (1 / num_periods) - 1
        annualized_return = (1 + total_return) ** 252 - 1  # Assuming 252 trading days in a year
        return annualized_return

    def calculate_max_drawdown(self):
        """
        Calculates the maximum drawdown of a portfolio
        """
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
