import matplotlib.pyplot as plt
import yfinance as yf
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
    
    def get_data_yf(self, ticker: str, start: str, end: str, interval: str='1d'):
        """
        Adds data to back instance of Riley with a csv file.
        
        Args:
            ticker (str): The ticker of the stock to get data for.
            start (str): The start date of the data.
            end (str): The end date of the data.
            interval (str): The interval of the data.
            Options for interval are 1d, 5d, 1wk, 1mo, 3mo"""
        
        ticker = yf.Ticker(ticker)
        
        df = ticker.history(ticker, start=start, end=end, interval=interval)
            
        return df
    
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
        
        for bar in self.data.iterrows():
            try:
                #Create dictionary from row
                ohlc = {'open': bar[1]['open'], 'high': bar[1]['high'], 'low': bar[1]['low'], 'close': bar[1]['close'], 'volume': bar[1]['volume'], 'time': bar[1]['timestamp']}
            except:
                #Create dictionary from row
                ohlc = {'open': bar[1]['open'], 'high': bar[1]['high'], 'low': bar[1]['low'], 'close': bar[1]['close']}

            #Update current position
            # CURRENT_POSITION = self.strategy.update_current_position(CURRENT_POSITION, ohlc)

            print(ohlc)
            
        if self.optimization:
            optimization = self.optimize()
            return optimization
        else:
            print("No optimization")
            return    