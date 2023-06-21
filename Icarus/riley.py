from Icarus.graphs.graph import *
from Icarus.source import *
from Icarus.runners import *
from Icarus.optimize import *
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import logging
from tqdm import tqdm
import math


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
        self.starting_cash = None
        self.account_value = 0
        self.account_value_history = []
        self.ticker = ""
        self.metrics = {}
        self.pct_change = None
        self.data_length = None
        self.final_value = None
        
    def set_ticker(self, ticker: str):
        """
        Sets the ticker to backtest.
        
        Args:
            ticker (str): The ticker to backtest.
        """
        self.ticker = ticker
        return
        
    def set_cash(self, cash: float):
        """
        Sets the amount of cash to start with.
        
        Args:
            cash (float): The amount of cash to start with.
        """
        self.starting_cash = cash
        self.account_value = cash
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
    
    def add_data(self, data):
        """
        Adds data to back instance of Riley.
        
        Args:
            data (csv or pd.DataFrame): The data to backtest on.
        """
        if isinstance(data.data, pd.DataFrame):
            self.data = data.data
            self.data_length = data.data_length
        else:
            raise Exception('Data must be a pandas dataframe')
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
    
    def add_metric(self, metric, name: str):
        """
        Adds a metric to track during the backtest.
        
        Args:
            metric: The metric to track.
            name (str): The name of the metric.
        """
        self.metrics[name] = metric   
        return
        
    def calculate_metrics(self):
        """
        Calculates all metrics.
        """
        data = {}
        for metric in self.metrics:
            match metric:
                case 'sharpe':
                    sharpe = self.metrics[metric](self.account_value_history)
                    self.metrics[metric] = sharpe.calculate()
                    data['sharpe'] = self.metrics[metric]
                    print("Sharpe Ratio: " + str(self.metrics[metric]))
                case 'sortino':
                    sor = self.metrics[metric](self.account_value_history)
                    self.metrics[metric] = sor.calculate()
                    print("Sortino Ratio: " + str(self.metrics[metric]))
                    data['sortino'] = self.metrics[metric]
                case 'maxdrawdown':
                    mdd = self.metrics[metric](self.account_value_history)
                    self.metrics[metric] = mdd.calculate()
                    print("Max Drawdown: " + str(self.metrics[metric]))
                    data['max_drawdown'] = self.metrics[metric]
                case 'calmar':
                    calmar = self.metrics[metric](self.account_value_history)
                    self.metrics[metric] = calmar.calculate()
                    print("Calmar Ratio: " + str(self.metrics[metric]))
                    data['calmar'] = self.metrics[metric]
                case 'annualreturn':
                    annual_return = self.metrics[metric](self.account_value_history)
                    self.metrics[metric] = annual_return.calculate()
                    print("Annual Return: " + str(self.metrics[metric]))
                    data['annual_return'] = self.metrics[metric]
                case 'totalreturn':
                    total_return = self.metrics[metric](self.starting_cash, self.final_values['end_value'])
                    self.metrics[metric] = total_return.calculate()
                    print("Total Return: " + str(self.metrics[metric]))
                    data['total_return'] = self.metrics[metric]
                    
        return data
        
    def plot_bar(self, save: bool=False, name: str='Backtest.png'):
        """
        Plots the backtest as a bar chart.
        
        Args:
            save (bool): Whether or not to save the plot.
            name (str): The name of the plot.
        """
        if self.optimization:
            return
        else:
            plot = Graph(self.data, self.data_length, self.ticker, self.pct_change, self.account_value_history, self.metrics)
            plot.plot_bar(save=save, name=name)
            return
        
    def plot(self, save: bool=False, name: str='Backtest.png'):
        """
        Plots the backtest as a line chart.
        
        Args:
            save (bool): Whether or not to save the plot.
            name (str): The name of the plot.
        """
        if self.optimization:
            return
        else:
            plot = Graph(self.data, self.data_length, self.ticker, self.pct_change, self.account_value_history, self.metrics)
            plot.plot(save=save, name=name)
            return
        
    def plot_candlestick(self,mav: tuple=(3,5), save: bool=False, name: str='Backtest.png'):
        """
        Plots the backtest as a candlestick chart.
        """
        if self.optimization:
            return
        else:
            plot = Graph(self.data, self.data_length, self.ticker, self.pct_change, self.account_value_history, self.metrics)
            plot.mpl(mav)
            return
        
    def optimize(self):
        optimization_range = self.strategy.optimize_range
        optimized = Optimization(self.ticker, self.data, self.strategy, self.stake, self.stake_type, self.cash, optimization_range)
        
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
        
            
        if self.optimization:
            optimization = self.optimize()
            return optimization
        else:        
            RUNNER = Runner(self.ticker, self.data, self.strategy, self.stake, self.stake_type, self.cash)
            FINAL_VALUES = RUNNER.run()
            self.account_value_history = FINAL_VALUES.account_value_history
            self.final_values = FINAL_VALUES
            self.pct_change = FINAL_VALUES.pct_change
            print(str(FINAL_VALUES))
            if len(self.metrics) > 0:
                data = self.calculate_metrics()
            return self.account_value   