from tqdm import tqdm
import pandas as pd
import numpy as np
import math

class final_value():
    def __init__(self, ticker, account_value, account_value_history, data, startDate, endDate, start_value):
        self.ticker = ticker
        self.account_value = account_value
        self.account_value_history = account_value_history
        self.data = data
        self.startDate = startDate
        self.endDate = endDate
        self.end_value = self.account_value_history[len(self.account_value_history)-1]
        self.start_value = self.account_value_history[0]
        self.pct_change = round(((self.account_value - self.start_value)/self.start_value)*100, 2)
        self.start_value = start_value
              
    def __str__(self) -> str:
        return f'Final Data on {self.ticker} from {self.startDate} to {self.endDate} \nStarting Cash: {self.start_value} \nFinal Value: {self.account_value} \nPercent Change: {self.pct_change}'
   


class Runner():
    def __init__(self, ticker, data=None, strategy=None, stake=0, stake_type='quantity', cash=0):
        self.current_position = {'shares': 0, 'price': 0.0}
        self.data = data
        self.strategy = strategy
        self.stake = stake
        self.stake_type = stake_type
        self.cash = cash
        self.starting_cash = cash
        self.account_value_history = []
        self.account_value = self.cash
        self.length = len(self.data)
        self.ticker = ticker
        #Set start and end dates
        self.startDate = self.data['timestamp'][0]
        self.endDate = self.data['timestamp'][len(self.data)-1]
     
    def run(self):
        #Loop through each bar
        pbar = tqdm(total=self.length, desc='Backtesting on {}'.format(self.ticker), unit='bars')
        
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
            if(self.current_position['shares']==0):
                if self.strategy.check_for_buy(ohlc) == True:
                    match self.stake_type:
                        case 'quantity':
                            cost = self.stake * ohlc['close']
                            if cost > self.cash:
                                raise Exception('Not enough cash')
                            else:
                                self.cash -= cost
                                self.current_position['shares'] += self.stake
                                self.current_position['price'] = ohlc['close']
                                self.account_value = self.cash + (self.current_position['shares'] * ohlc['close'])
                        case 'percentage':
                            cash = (self.cash * (self.stake/100))
                            cost = cash/ohlc['close']
                            if cost > self.cash:
                                raise Exception('Not enough cash')
                            else:
                                self.cash -= cost
                                self.current_position['shares'] += (cash/ohlc['close'])
                                self.current_position['price'] = ohlc['close']
                                self.account_value = self.cash + (self.current_position['shares'] * ohlc['close'])
                        case 'dollars':
                            shares = math.floor(self.stake/ohlc['close'])
                            cost = shares * ohlc['close']
                            if cost > self.stake:
                                raise Exception('Not enough cash')
                            else:
                                self.cash -= cost
                                self.current_position['shares'] == shares
                                self.current_position['price'] = ohlc['close']
                                self.account_value = self.cash + (self.current_position['shares'] * ohlc['close'])
            elif(self.current_position['shares']>0):
                if self.strategy.check_for_sell(ohlc) == True:
                    self.cash += self.current_position['shares'] * ohlc['close']
                    self.current_position['shares'] = 0
                    self.current_position['price'] = 0
                    self.account_value = self.cash
                    
                    
            else:
                # print("No signal to buy or sell")
                pass
                
            pbar.update(1)
                
            
        pbar.close()
            
            
        #Update account value
            
        if self.current_position['shares'] > 0:
            self.account_value = round(self.cash + (self.current_position['shares'] * self.current_position['price']),2)
            self.account_value_history.append(self.account_value)
        else:
            self.account_value = round(self.cash,2)
            self.account_value_history.append(self.account_value)
            
        FINAL_VALUES = final_value(self.ticker, self.account_value, self.account_value_history, self.data, self.startDate, self.endDate, self.starting_cash)
        return FINAL_VALUES