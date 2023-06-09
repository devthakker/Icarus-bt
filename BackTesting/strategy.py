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
    
    def add_input_value(self, line):
        self.BBONE.add_input_value(line['close'])
        self.BBTWO.add_input_value(line['close'])
        self.history.append(line)
        return self.history
        
    def check_for_buy(self, line):
        if self.BBONE.has_output_value() and self.BBTWO.has_output_value():
            if self.BBONE[-1].lb > line['close'] and self.BBTWO[-1].lb < line['close']:
                # if self.BBONE[-2].lb < line['close']:
                    return True
        return False
    
    
    def buy(self, line):
        pass
    
    def check_for_sell(self, line):
        if self.BBONE.has_output_value() and self.BBTWO.has_output_value():
            if self.BBONE[-1].ub < line['close'] and self.BBTWO[-1].ub > line['close']:
                # if self.BBONE[-1].ub > line['close']:
                    return True
        return False
    
    def sell(self, line):
        pass
    
    
    