import matplotlib.pyplot as plt

class STOCHOSCILLATOR:
    """
    Stochastic Oscillator
    
    Formula:
    %K = (Current Close - Lowest Low)/(Highest High - Lowest Low) * 100
    %D = 3-day SMA of %K
    """
    def __init__(self, period, smoothing_period, oversold_threshold, overbought_threshold,high_prices=None, low_prices=None, close_prices=None):
        self.stoch = None
        self.smoothed = None
        self.period = period
        self.smoothing_period = smoothing_period
        self.oversold_threshold = oversold_threshold
        self.overbought_threshold = overbought_threshold
        self.high_prices = high_prices if high_prices is not None else []
        self.low_prices = low_prices if low_prices is not None else []
        self.close_prices = close_prices if close_prices is not None else []
        self.stoch_values = []
        self.smoothed_values = []
        if len(self.high_prices) > self.period and len(self.low_prices) > self.period and len(self.close_prices) > self.period:
            self.calculate()


    def calculate(self):
        """
        Calculates the stochastic oscillator.
        """
        if len(self.high_prices) < self.period:
            return None
        highest_high = max(self.high_prices)
        lowest_low = min(self.low_prices)
        latest_close = self.close_prices[-1]
        stochastic_value = (latest_close - lowest_low) / (highest_high - lowest_low) * 100

        if len(self.close_prices) >= self.smoothing_period:
            smoothed_stochastic = sum(self.close_prices[-self.smoothing_period:]) / self.smoothing_period
        else:
            smoothed_stochastic = None

        self.stoch, self.smoothed =  stochastic_value, smoothed_stochastic
        self.stoch_values.append(stochastic_value)
        self.smoothed_values.append(smoothed_stochastic)

    def is_oversold(self):
        """
        Returns True if the stochastic oscillator is oversold.
        """
        return self.stoch <= self.oversold_threshold

    def is_overbought(self):
        """
        Returns True if the stochastic oscillator is overbought.""
        """
        return self.stoch >= self.overbought_threshold
    
    def add_data_point(self, high, low, close):
        """
        Adds a data point to the stochastic oscillator.
        """
        self.high_prices.append(high)
        self.low_prices.append(low)
        self.close_prices.append(close)
        if len(self.high_prices) > self.period:
            self.calculate()
    
    def get_stoch(self):
        """
        Returns the stochastic oscillator.
        """
        return self.stoch
    
    def get_smoothed(self):
        """
        Returns the smoothed stochastic oscillator.
        """
        return self.smoothed
    
    def plot_show(self):
        """
        Plots the stochastic oscillator.
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
        ax1.set_title('Stock Prices')
        ax1.plot(self.high_prices, label='High Price')
        ax1.plot(self.low_prices, label='Low Price')
        ax1.plot(self.close_prices, label='Close Price')
        ax1.legend(loc='upper left')
        ax2.set_title('Stoch - {} Period - {} Smoothing Period'.format(self.period, self.smoothing_period))
        ax2.plot(self.stoch_values, label='Stoch')
        ax2.plot(self.smoothed_values, label='Smoothed')
        ax2.legend(loc='upper left')
        plt.tight_layout()
        plt.show()
        return

    def plot_save(self, path):
        """
        Saves the stochastic oscillator plot to the path.
        """
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6))
        ax1.set_title('Stock Prices')
        ax1.plot(self.high_prices, label='High Price')
        ax1.plot(self.low_prices, label='Low Price')
        ax1.plot(self.close_prices, label='Close Price')
        ax1.legend(loc='upper left')
        ax2.set_title('Stoch - {} Period - {} Smoothing Period'.format(self.period, self.smoothing_period))
        ax2.plot(self.stoch_values, label='Stoch')
        ax2.plot(self.smoothed_values, label='Smoothed')
        ax2.legend(loc='upper left')
        plt.tight_layout()
        plt.savefig(path)
        return