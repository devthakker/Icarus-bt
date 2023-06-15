from talipp.indicators import *
import matplotlib.pyplot as plt
import Icarus as ic

# Example class of a strategy

# Name your class accordingly and inherit from ic.strategy
class BollingerBands(ic.strategy):
    
    # Define the __init__ method
    # This is where you will define your indicators
    # and any other variables you need
    # If you would like to run an optimization, you have to provide the optimize and optimize_range parameters
    def __init__(self, optimize=False, optimize_range=range(1, 100)):
        # Call the super class's __init__ method and pass the optimize and optimize_range parameters
        super().__init__(optimize, optimize_range)
        
        # Define your indicators here or in a separate method
        # If you define them in a separate method, you must call that method here
        # This is how you will evaluate whether to send a buy or sell signal
        self.period = 20
        self.BBONE = BB(self.period, 1)
        self.BBTWO = BB(self.period, 2)
    
    
    # Necessary method to add input values to your indicators in the case of using this indicator package
    def add_input_value(self, line):
        # Add the input value to your indicators
        self.BBONE.add_input_value(line['close'])
        self.BBTWO.add_input_value(line['close'])

    # Necessary methods to check for buy and sell signals
    # These methods will be called by the backtest engine
    # They must match the names below
    # The line parameter is the current line of data and is a dictionary
    # This is a required parameter
    # You can add additional parameters if you would like but you would have to manipulate the backtest engine
    # The line parameter is in the format of {'open': 1.0, 'high': 1.0, 'low': 1.0, 'close': 1.0, 'volume': 1.0}
    
    # This method will be called to check for a buy signal
    # It must return true or false
    # If it returns true, a buy signal will be sent if there is no open position
    # If it returns false, no buy signal will be sent
    
    def check_for_buy(self, line):
        if self.BBONE.has_output_value() and self.BBTWO.has_output_value():
            if self.BBONE[-1].lb > line['close'] and self.BBTWO[-1].lb < line['close']:
                return True
        return False
    
    # This method will be called to check for a sell signal
    # It must return true or false
    # If it returns true, a sell signal will be sent for any open positions
    # If it returns false, no sell signal will be sent
    
    def check_for_sell(self, line):
        if self.BBONE.has_output_value() and self.BBTWO.has_output_value():
            if self.BBONE[-1].ub < line['close'] and self.BBTWO[-1].ub > line['close']:
                return True
        return False
    
    
    
    