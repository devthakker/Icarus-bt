import pandas as pd
import logging
import matplotlib.pyplot as plt

class Riley:
    """
    Riley is a class that allows for the backtesting of trading strategies.
    
    Attributes:
        optimization (bool): Whether or not to optimize the strategy
        cash (float): The amount of cash to start with
        strategy (Strategy): The strategy to backtest
        data (pd.DataFrame): The data to backtest on
        stake (float): The amount of cash to use per trade
    """
    
    def __init__(self, optimization=False, log=False) -> None:
        self.optimization = optimization
        self.log = log
        self.cash = None
        self.strategy = None
        self.data = None
        self.stake = None
        
        
    def set_cash(self, cash):
        self.cash = cash
        return
    
    def set_strategy(self, strategy):
        self.strategy = strategy
        return
    
    def add_data_dataframe(self, data):
        if isinstance(data, pd.DataFrame):
            df = pd.DataFrame(data)
            if 'open' not in df.columns:
                raise Exception('Data must contain an open column')
            if 'high' not in df.columns:
                raise Exception('Data must contain a high column')
            if 'low' not in df.columns:
                raise Exception('Data must contain a low column')
            if 'close' not in df.columns:
                raise Exception('Data must contain a close column')
            self.data = df
        else:
            raise Exception('Data must be a pandas dataframe')
        return
    
    def add_data_csv(self, path):
        if isinstance(path, str):
            df = pd.read_csv(path)
            if 'open' not in df.columns:
                raise Exception('Data must contain an open column')
            if 'high' not in df.columns:
                raise Exception('Data must contain a high column')
            if 'low' not in df.columns:
                raise Exception('Data must contain a low column')
            if 'close' not in df.columns:
                raise Exception('Data must contain a close column')
            self.data = df
        else:
            raise Exception('Path is invalid')
        return
    
    def set_stake(self, stake):
        self.stake = stake
        return
    
    def optimize(self):
        optimization_range = self.strategy.optimization_range
    
    def run(self):
        if self.cash is None:
            raise Exception('Cash must be set')
        if self.strategy is None:
            raise Exception('Strategy must be set')
        if self.data is None:
            raise Exception('Data must be set')
        if self.stake is None:
            raise Exception('Stake must be set')
        
        
        if self.optimization:
            optimization = self.optimize()
        
        return optimization
    