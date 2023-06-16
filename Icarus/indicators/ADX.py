import matplotlib.pyplot as plt

class ADX:
    """
    Average Directional Index
    
    Attributes:
        period (int): The period of the ADX.
        high_prices (list): The high prices of the stock.
        low_prices (list): The low prices of the stock.
        close_prices (list): The close prices of the stock.
    """
        
        
    def __init__(self, period, high_prices=None, low_prices=None, close_prices=None):
        self.period = period
        self.high_prices = [] if high_prices is None else high_prices
        self.low_prices = [] if low_prices is None else low_prices
        self.close_prices = [] if close_prices is None else close_prices
        self.previous_high = None
        self.previous_low = None
        self.true_ranges = []
        self.directional_movements = []
        self.directional_movement_index = None if len(self.high_prices) < self.period else self.calculate()

    def calculate(self):
        """
        Calculates the ADX of a stock.
        
        Returns:
            float: The ADX of the stock."""
        if len(self.high_prices) < self.period:
            return None

        self.calculate_true_ranges()
        self.calculate_directional_movements()

        true_range_average = sum(self.true_ranges) / len(self.true_ranges)
        positive_directional_movement_average = sum(self.positive_directional_movements) / len(self.positive_directional_movements)
        negative_directional_movement_average = sum(self.negative_directional_movements) / len(self.negative_directional_movements)

        positive_directional_index = (positive_directional_movement_average / true_range_average) * 100
        negative_directional_index = (negative_directional_movement_average / true_range_average) * 100

        directional_movement_index = abs(positive_directional_index - negative_directional_index) / (positive_directional_index + negative_directional_index) * 100

        self.directional_movement_index = directional_movement_index
        
        self.directional_movements.append(directional_movement_index)

    def calculate_true_ranges(self):
        """
        Calculates the true ranges of a stock.
        """
        self.true_ranges = []
        for i in range(len(self.high_prices)-self.period,len(self.high_prices)):
            high_low_range = self.high_prices[i] - self.low_prices[i]
            high_close_range = abs(self.high_prices[i] - self.close_prices[i - 1])
            low_close_range = abs(self.low_prices[i] - self.close_prices[i - 1])
            true_range = max(high_low_range, high_close_range, low_close_range)
            self.true_ranges.append(true_range)

    def calculate_directional_movements(self):
        """
        Calculates the directional movements of a stock.
        """
        self.positive_directional_movements = []
        self.negative_directional_movements = []
        for i in range(len(self.high_prices)-self.period,len(self.high_prices)):
            if i == len(self.high_prices)-self.period:
                self.positive_directional_movements.append(0)
                self.negative_directional_movements.append(0)
                self.previous_high = self.high_prices[i]
                self.previous_low = self.low_prices[i]
            else:
                high_movement = self.high_prices[i] - self.previous_high
                low_movement = self.previous_low - self.low_prices[i]
                if high_movement > low_movement and high_movement > 0:
                    self.positive_directional_movements.append(high_movement)
                else:
                    self.positive_directional_movements.append(0)
                if low_movement > high_movement and low_movement > 0:
                    self.negative_directional_movements.append(low_movement)
                else:
                    self.negative_directional_movements.append(0)
                self.previous_high = self.high_prices[i]
                self.previous_low = self.low_prices[i]
                
    def add_data_point(self, high, low, close):
        """
        Adds a data point to the ADX.
        """
        self.high_prices.append(high)
        self.low_prices.append(low)
        self.close_prices.append(close)
        if len(self.high_prices) > self.period:
            self.calculate()
    
    def get_directional_movement_index(self):
        """
        Returns:
            float: The ADX of the stock.
        """
        return self.directional_movement_index

    def plot_show(self):
        """
        Plots the ADX.
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        ax1.plot(self.high_prices, label='High')
        ax1.plot(self.low_prices, label='Low')
        ax1.plot(self.close_prices, label='Close')
        ax1.set_title('Stock')
        ax1.set_ylabel('Price')
        ax1.legend(loc='upper left')
        ax2.plot(self.directional_movements, label='Directional Movement Index')
        ax2.set_title('Directional Movement Index')
        ax2.set_xlabel('Period')
        ax2.set_ylabel('Directional Movement Index')
        ax2.legend(loc='upper left')
        plt.show()
        
    def plot_save(self, filename):
        """
        Plots the ADX and saves it to a file.
        
        Args:
            filename (str): The filename to save the plot to.
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        ax1.plot(self.high_prices, label='High')
        ax1.plot(self.low_prices, label='Low')
        ax1.plot(self.close_prices, label='Close')
        ax1.set_title('Stock')
        ax1.set_ylabel('Price')
        ax1.legend(loc='upper left')
        ax2.plot(self.directional_movements, label='Directional Movement Index')
        ax2.set_title('Directional Movement Index')
        ax2.set_xlabel('Period')
        ax2.set_ylabel('Directional Movement Index')
        ax2.legend(loc='upper left')
        plt.savefig(filename)
        plt.close()
        
