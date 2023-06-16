import matplotlib.pyplot as plt

class RSI:
    
    """
    Calculates the Relative Strength Index (RSI) of a stock based on its historical price data.

    Parameters:
    period (int): Number of periods to use for RSI calculation. Default is 14.
    data (list): A list of the stock prices in chronological order, with the most recent price last.
    
    Returns:
    rsi (float): The RSI of the stock.
    """
    
    def __init__(self, period=14, data=None):
        self.period = period
        self.rsi = None
        
        self.rsi_values = []

        if data is None:
            self.data = []
        else:
            self.data = data
            if len(self.data) > self.period:
                self.calculate_rsi()

    def calculate_rsi(self):
        """
        Calculate the RSI of the stock based on its historical price data.
        """
        if len(self.data) <= self.period:
            raise ValueError("Insufficient data to calculate RSI.")

        gains = []
        losses = []
        
        for i in range(len(self.data)-self.period , len(self.data)):
            print(i)
            price_diff = self.data[i] - self.data[i - 1]
            if price_diff > 0:
                gains.append(price_diff)
                losses.append(0)
            elif price_diff < 0:
                losses.append(abs(price_diff))
                gains.append(0)
            else:
                gains.append(0)
                losses.append(0)

        try:
            avg_gain = sum(gains) / self.period
        except ZeroDivisionError:
            avg_gain = 0
        
        try:
            avg_loss = sum(losses) / self.period
        except ZeroDivisionError:
            avg_loss = 0

        if avg_loss == 0:
            self.rsi = 100
            self.rsi_values.append(100)
            return

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        self.rsi = rsi
        self.rsi_values.append(rsi)
        return
        
    def add_data_point(self, value):
        """
        Add a new price to the data list and calculate the new RSI.
        """
        self.data.append(value)
        if(len(self.data) > self.period):
            self.calculate_rsi()
        return
        
    def get_rsi(self):
        """
        Return the current RSI value."""
        return self.rsi
    
    def plot_show(self):
        """
        Plot the RSI values over time.
        """
        plt.plot(self.rsi_values)
        plt.ylabel('RSI Values')
        plt.xlabel('Current Calculation')
        plt.title('RSI Chart')
        plt.show()
        return
        
    def plot_save(self, filename):
        """
        Save the RSI values over time to a file.
        """
        plt.plot(self.rsi_values, label='RSI')
        plt.plot(self.data, label='Data')
        plt.legend(loc = 'upper left')
        plt.ylabel('RSI Values')
        plt.xlabel('Current Calculation')
        plt.title('RSI Chart')
        plt.savefig(filename)
        plt.close()
        return