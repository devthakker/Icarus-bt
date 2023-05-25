from talipp.indicators import *

class BollingerBands():
    
    def __init__(self, df, period, one_std, two_std, cash):
        self.df = df
        self.period = period
        self.BBONE = BB(period, one_std)
        self.BBTWO = BB(period, two_std)
        self.cash = cash
        
        
    def check_for_buy(self, line):
        pass
    
    def buy(self, line):
        pass
    
    def check_for_sell(self, line):
        pass
    
    def sell(self, line):
        pass
    
    def run(self):
        pass