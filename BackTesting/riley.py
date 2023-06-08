import pandas as pd

class Riley:
    
    def __init__(self, optimization=False) -> None:
        self.cash = None
        self.strategy = None
        self.data = None
        self.optimization = optimization
        self.strategy = None
        
    def set_cash(self, cash):
        self.cash = cash
        return
    
    def set_strategy(self, strategy):
        self.strategy = strategy
        return
    
    def set_data(self, data):
        if isinstance(data, pd.DataFrame):
            self.data = data
        else:
            self.data = pd.DataFrame(data)
        return