from talipp.indicators import *
import matplotlib.pyplot as plt

class BollingerBands():
    
    def __init__(self, optimize=False, optimize_range=range(1, 100)):
        self.period = 20
        self.BBONE = BB(self.period, 1)
        self.BBTWO = BB(self.period, 2)
        self.history = []
        self.current_position = {'shares': 0, 'price': 0}
        self.account_value = 0
        self.account_value_history = []
        self.iterations = []
        if optimize:
            self.optimize_range = optimize_range
            self.optimize_results = {}
        
    def graph(self):
        pass
    
    def update_current_position(self, shares, price):
        self.current_position['shares'] = shares
        self.current_position['price'] = price
        return self.current_position
        
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
    
    
    