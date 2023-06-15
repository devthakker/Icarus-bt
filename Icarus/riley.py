from Icarus.graphs.graph import *
from Icarus.source import *
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
    
    def optimize(self):
        optimization_range = self.strategy.optimization_range
        
    def plot_bar(self, save: bool=False, name: str='Backtest.png'):
        """
        Plots the backtest as a bar chart.
        
        Args:
            save (bool): Whether or not to save the plot.
            name (str): The name of the plot.
        """
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
        plot = Graph(self.data, self.data_length, self.ticker, self.pct_change, self.account_value_history, self.metrics)
        plot.plot(save=save, name=name)
        return
        
        
    
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
        
        length = len(self.data)
        
        #Loop through each bar
        pbar = tqdm(total=length, desc='Backtesting on {}'.format(self.ticker), unit='bars')
        
        for bar in self.data.iterrows():
            
            self.account_value_history.append(self.account_value)
            
            try:
                #Create dictionary from row
                ohlc = {'open': bar[1]['open'], 'high': bar[1]['high'], 'low': bar[1]['low'], 'close': bar[1]['close'], 'volume': bar[1]['volume'], 'time': bar[1]['timestamp']}
            except:
                #Create dictionary from row
                ohlc = {'open': bar[1]['open'], 'high': bar[1]['high'], 'low': bar[1]['low'], 'close': bar[1]['close']}

            #Update current position
            # CURRENT_POSITION = self.strategy.update_current_position(CURRENT_POSITION, ohlc)

            self.strategy.add_input_value(ohlc)
            if(CURRENT_POSITION['shares']==0):
                if self.strategy.check_for_buy(ohlc) == True:
                    match self.stake_type:
                        case 'quantity':
                            cost = self.stake * ohlc['close']
                            if cost > self.cash:
                                raise Exception('Not enough cash')
                            else:
                                self.cash -= cost
                                CURRENT_POSITION['shares'] += self.stake
                                CURRENT_POSITION['price'] = ohlc['close']
                                self.account_value = self.cash + (CURRENT_POSITION['shares'] * ohlc['close'])
                        case 'percentage':
                            cash = (self.cash * (self.stake/100))
                            cost = cash/ohlc['close']
                            if cost > self.cash:
                                raise Exception('Not enough cash')
                            else:
                                self.cash -= cost
                                CURRENT_POSITION['shares'] += (cash/ohlc['close'])
                                CURRENT_POSITION['price'] = ohlc['close']
                                self.account_value = self.cash + (CURRENT_POSITION['shares'] * ohlc['close'])
                        case 'dollars':
                            shares = math.floor(self.stake/ohlc['close'])
                            cost = shares * ohlc['close']
                            if cost > self.stake:
                                raise Exception('Not enough cash')
                            else:
                                self.cash -= cost
                                CURRENT_POSITION['shares'] == shares
                                CURRENT_POSITION['price'] = ohlc['close']
                                self.account_value = self.cash + (CURRENT_POSITION['shares'] * ohlc['close'])
            elif(CURRENT_POSITION['shares']>0):
                if self.strategy.check_for_sell(ohlc) == True:
                    self.cash += CURRENT_POSITION['shares'] * ohlc['close']
                    CURRENT_POSITION['shares'] = 0
                    CURRENT_POSITION['price'] = 0
                    self.account_value = self.cash
                    
                    
            else:
                # print("No signal to buy or sell")
                pass
                
            pbar.update(1)
                
            
        pbar.close()
            
            
        #Update account value
            
        if CURRENT_POSITION['shares'] > 0:
            self.account_value = round(self.cash + (CURRENT_POSITION['shares'] * CURRENT_POSITION['price']),2)
            self.account_value_history.append(self.account_value)
        else:
            self.account_value = round(self.cash,2)
            self.account_value_history.append(self.account_value)
            
        if self.optimization:
            optimization = self.optimize()
            return optimization
                        
        
        else:
            FINAL_VALUES = {'start': startDate, 'end': endDate, 'start_value': self.account_value_history[0], 'end_value': self.account_value_history[len(self.account_value_history)-1]}
            self.final_values = FINAL_VALUES
            PERCENTAGE_CHANGE = round(((FINAL_VALUES['end_value'] - FINAL_VALUES['start_value']) / FINAL_VALUES['start_value']) * 100, 2)
            self.pct_change = PERCENTAGE_CHANGE
            print(FINAL_VALUES)
            print('Percentage Change: {}%'.format(PERCENTAGE_CHANGE))
            if len(self.metrics) > 0:
                data = self.calculate_metrics()
            return self.account_value   