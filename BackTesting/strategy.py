from talipp.indicators import *
import matplotlib.pyplot as plt

class BollingerBands():
    
    def __init__(self, df, period, one_std, two_std, cash, optimize=False, optimize_range=range(1, 100)):
        self.df = df
        self.period = period
        self.BBONE = BB(period, one_std)
        self.BBTWO = BB(period, two_std)
        self.cash = cash
        self.history = []
        self.current_position = {'shares': 0, 'price': 0}
        self.account_value = 0
        self.account_value_history = []
        self.iterations = []
        self.startDate = df['timestamp'][0]
        self.endDate = df['timestamp'][len(df)-1]
        if optimize:
            self.optimize_range = optimize_range
            self.optimize_results = {}
        
    def graph(self):
        pass
        
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
    
    def show_results(self):
        pass

    def optimize(self):
        pass
    
    def get_results(self):
        pass
    
    def get_best_results(self):
        pass
    
    
    