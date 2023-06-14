class AnnualizedReturn:
    """
    Measures the annualized return of a portfolio
    
    Attributes
        returns (list): A list of returns
    """
    def __init__(self, returns):
        self.returns = returns

    def calculate(self):
        """
        Calculates the annualized return of a portfolio
        """
        num_periods = len(self.returns)
        total_return = (1 + sum(self.returns)) ** (1 / num_periods) - 1
        annualized_return = (1 + total_return) ** 252 - 1  # Assuming 252 trading days in a year
        return annualized_return
