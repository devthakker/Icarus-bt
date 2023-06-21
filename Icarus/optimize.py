class Optimization:
    def __init__(self, ticker: str, strategy, data, cash: float, stake_type: str, stake: float, log=False) -> None:
        self.ticker = ticker
        self.strategy = strategy
        self.data = data
        self.cash = cash
        self.stake_type = stake_type
        self.stake = stake
        self.account_value = 0
        self.account_value_history = []
        self.metrics = {}
        self.pct_change = None
        self.data_length = len(self.data)
        self.final_value = None
        self.starting_cash = self.cash
        