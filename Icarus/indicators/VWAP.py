import matplotlib.pyplot as plt

class VWAP:
    """
    VWAPCalculator is a class that calculates the volume weighted average price (VWAP) of a stock.
    
    Attributes:
        
        total_volume (int): The total volume of the stock.
        cumulative_price_volume (float): The cumulative price volume of the stock.
        cumulative_time_weighted_price_volume (float): The cumulative time weighted price volume of the stock.  
        moving_volume (int): The moving volume of the stock.
        moving_cumulative_price_volume (float): The moving cumulative price volume of the stock.
        vwap (float): The volume weighted average price of the stock.
        """
    def __init__(self, total_volume=0, cumulative_price_volume=0, cumulative_time_weighted_price_volume=0, moving_volume=0, moving_cumulative_price_volume=0):
        self.total_volume = total_volume
        self.cumulative_price_volume = cumulative_price_volume  
        self.cumulative_time_weighted_price_volume = cumulative_time_weighted_price_volume
        self.moving_volume = moving_volume
        self.moving_cumulative_price_volume = moving_cumulative_price_volume
        
        if self.total_volume > 0:
            self.calculate_vwap()
        else:
            self.vwap = []

    def calculate_vwap(self):
        """
        Calculates the volume weighted average price (VWAP) of a stock.
        """
        if self.total_volume == 0:
            return None
        vwap = self.cumulative_price_volume / self.total_volume
        self.vwap.append(vwap)

    def calculate_twap(self, total_time):
        """
        Calculates the time weighted average price (TWAP) of a stock.
        """
        if self.cumulative_time_weighted_price_volume == 0:
            return None
        twap = self.cumulative_time_weighted_price_volume / (self.total_volume * total_time)
        return twap

    def calculate_mvwap(self, period):
        """
        Calculates the moving volume weighted average price (MVWAP) of a stock.
        """
        if self.moving_volume < period:
            return None
        mvwap = self.moving_cumulative_price_volume / self.moving_volume
        return mvwap
    
    def add_data_point(self, price, volume, timestamp):
        """
        Adds a data point to the VWAP calculator.
        """
        self.total_volume += volume
        self.cumulative_price_volume += price * volume
        self.cumulative_time_weighted_price_volume += price * volume * timestamp
        self.moving_volume += volume
        self.moving_cumulative_price_volume += price * volume
        self.calculate_vwap()
        
    def get_vwap(self):
        """
        Returns the volume weighted average price (VWAP) of a stock.
        """
        return self.vwap
    
    def plot_show(self):
        """
        Plot the VWAP values calculated.
        """
        plt.figure(figsize=(12, 6))
        plt.title('VWAP')
        plt.plot(self.vwap, label='VWAP')
        plt.legend(loc='upper left')
        plt.show()
        return
    
    def plot_save(self, filename):
        """
        Plot the VWAP values calculated and save to file.
        
        Parameters:
            filename (str): The filename to save the plot to.
        """
        plt.figure(figsize=(12, 6))
        plt.title('VWAP')
        plt.plot(self.vwap, label='VWAP')
        plt.legend(loc='upper left')
        plt.savefig(filename)
        return
        

