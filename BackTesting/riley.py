import matplotlib.pyplot as plt
import pandas as pd
import logging

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
        self.logger = logging.getLogger(__name__)
        self.stake_type = None
        
        
    def set_cash(self, cash: float):
        """
        Sets the amount of cash to start with.
        
        Args:
            cash (float): The amount of cash to start with.
        """
        self.cash = cash
        return
    
    def set_strategy(self, strategy):
        """
        Sets the strategy to backtest.
        
        Args:
            strategy (Strategy): The strategy to backtest.
        """
        self.strategy = strategy
        return
    
    def add_data_dataframe(self, data: pd.DataFrame):
        """
        Adds data to back instance of Riley with a pandas dataframe.
        
        Args:
            data (pd.DataFrame): The data to backtest on.
        """
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
    
    def add_data_csv(self, path: str):
        """
        Adds data to back instance of Riley with a csv file.
        
        Args:
            path (str): The path to the csv file."""
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
    
    def set_stake_quantity(self, stake: float):
        """
        Sets the amount of cash to use per trade in the form of quantity of shares.
        Sets the stake type to quantity.
        
        Args:
            stake (float): The amount of shares to purchase in each trade.
        """
        self.stake = stake
        self.stake_type = 'quantity'
        return
    
    def set_stake_percentage(self, stake: float):
        """
        Sets the amount of cash to use per trade in the form of percentage of cash.
        Sets the stake type to percentage.
        
        Args:
            stake (float): The percentage of cash to use per trade.
        """
        self.stake = stake
        self.stake_type = 'percentage'
        return
    
    def set_stake_dollars(self, stake: float):
        """
        Sets the amount of cash to use per trade in the form of dollars.
        Sets the stake type to dollars.
        
        Args:
            stake (float): The amount of cash to use per trade.
        """
        self.stake = stake
        self.stake_type = 'dollars'
        return
    
    def optimize(self):
        optimization_range = self.strategy.optimization_range
        
    def plot(self):
        pass
    
    def run(self):
        """
        Runs the backtest.
        """
        
        #Check if all required variables are set
        if self.cash is None:
            raise Exception('Cash must be set')
        if self.strategy is None:
            raise Exception('Strategy must be set')
        if self.data is None:
            raise Exception('Data must be set')
        if self.stake is None:
            raise Exception('Stake must be set')
        
        #Initialize Variables
        
        #Create dictionary to store current position
        CURRENT_POSITION = {'shares': 0, 'price': 0}

        #Set start and end dates
        startDate = self.data['timestamp'][0]
        endDate = self.data['timestamp'][len(self.data)-1]
        
        
        if self.optimization:
            optimization = self.optimize()
        
        return optimization
    