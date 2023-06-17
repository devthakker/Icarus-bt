import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class BollingerBands:
    """
    Initialize the BollingerBands class with given data, window size, and number of standard deviations.
        
    Parameters:
        data (list or numpy array): The input data for which Bollinger Bands need to be calculated.
        window (int, optional): The size of the moving window. Default is 20.
        num_std (int, optional): The number of standard deviations for the Bollinger Bands. Default is 1.
    """
    def __init__(self, window=20, num_std=1, data=None):
        if data is None:
            self.data = []
        else :
            self.data = data
        self.window = window
        self.num_std = num_std
        self.upper_band = []
        self.middle_band = []
        self.lower_band = []
        if len(self.data) > 20:
            self.calculate()
    
    def calculate(self):
        """
        Calculate the Bollinger Bands.
        
        """
        data = pd.DataFrame(self.data)
        rolling_mean = data.rolling(window=self.window).mean()
        rolling_std = data.rolling(window=self.window).std()
        self.upper_band = rolling_mean + (self.num_std * rolling_std)
        self.middle_band = (rolling_mean)
        self.lower_band = (rolling_mean - (self.num_std * rolling_std))
        return
    
    def add_data_point(self, new_data_point):
        """
        Add a new data point to the existing data.
        
        Parameters:
            new_data_point (float or int): The new data point to be added.
        """
        self.data.append(new_data_point)
        if self.upper_band is not None:
            self.calculate()
        return
    
    def has_output(self):
        """
        Returns True if the Bollinger Bands have been calculated.
        
        Returns:
            bool: True if the Bollinger Bands have been calculated.
        """
        return len(self.upper_band) > 0
            
    def get_BollingerBands(self):
        """
        Returns the current Bollinger Bands values.
        
        Returns:
            tuple: A tuple containing three current values for: upper_band, middle_band, and lower_band.
        """
        return (float(self.upper_band.values[-1]), float(self.middle_band.values[-1]), float(self.lower_band.values[-1]))

    
    
    