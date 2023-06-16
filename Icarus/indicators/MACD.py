import numpy as np

class MACD:
    """
    Initialize the MACD class with given data, short-term period, long-term period, and signal period.
    
    Parameters:
        data (list or numpy array): The input data for which MACD needs to be calculated.
        short_period (int, optional): The short-term period. Default is 12.
        long_period (int, optional): The long-term period. Default is 26.
        signal_period (int, optional): The signal period. Default is 9.
    """
    def __init__(self, short_period=12, long_period=26, signal_period=9, data=[]):
        self.short_period = short_period
        self.long_period = long_period
        self.signal_period = signal_period
        self.data = np.array(data)
        if len(data) >= long_period:
            self.calculate_macd()
        else:
            self.macd_line = None
            self.signal_line = None
            self.macd_histogram = None
        

    def calculate_macd(self):
        """
        Calculate the MACD line, signal line, and MACD histogram.
        
        Returns:
            null: The calculated MACD line, signal line, and MACD histogram are stored in the class variables.
        """
        # Calculate the short-term exponential moving average (EMA)
        short_ema = self.calculate_ema(self.data, self.short_period)

        # Calculate the long-term exponential moving average (EMA)
        long_ema = self.calculate_ema(self.data, self.long_period)

        # Calculate the MACD line
        macd_line = short_ema - long_ema

        # Calculate the signal line (EMA of the MACD line)
        signal_line = self.calculate_ema(macd_line, self.signal_period)

        # Calculate the MACD histogram
        macd_histogram = macd_line - signal_line

        self.macd_line, self.signal_line, self.macd_histogram = macd_line, signal_line, macd_histogram

    def calculate_ema(self,prices, period):
        """
        Calculate the Exponential Moving Average (EMA) with the given alpha (smoothing factor).
        
        Parameters:
            prices (list or numpy array): The input data for which EMA needs to be calculated.
            period (int): The size of the window for calculating EMA.
            
            Returns:
                numpy array: The calculated EMA values.
        """
        ema = np.zeros_like(prices)
        ema[0] = prices[0]
        alpha = 2 / (period + 1)

        for i in range(1, len(prices)):
            ema[i] = alpha * prices[i] + (1 - alpha) * ema[i - 1]

        return ema
    
    def add_data_point(self, data_point):
        """
        Add a new data point to the existing data and recalculate the MACD line, signal line, and MACD histogram.
        
        Parameters:
            data_point (float or int): The new data point to be added.
        """
        np.append(self.data, data_point)
        if len(self.data) > self.long_period:
            self.calculate_macd()    
    
    def get_lines(self):
        """
        Returns:
            tuple: The calculated MACD line, signal line, and MACD histogram.
        """
        return self.macd_line[-1], self.signal_line[-1], self.macd_histogram[-1]
    
        
        
