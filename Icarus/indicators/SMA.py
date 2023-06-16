import pandas as pd
import matplotlib.pyplot as plt

class SMA:
    """
    Initialize the SMA class with given data and period.
    
    Parameters:
        data (list or numpy array): The input data for which SMA needs to be calculated.
        period (int): The period for which SMA needs to be calculated.
    """
    
    def __init__(self, data, period):
        self.sma = None
        self.data = pd.Series(data)
        self.period = period
        self.sma_values = []
        if len(self.data) > self.period:
            self.calculate()
        
    def calculate(self):
        """
        Calculate the Simple Moving Average (SMA).
        """
        sma = self.data.rolling(self.period).mean()
        self.sma = sma.iloc[self.period-1:]
        self.sma_values = sma
        return
        
    def add_data_point(self, data_point):
        """
        Add a new data point to the existing data and recalculate the SMA.
        
        Parameters:
            data_point (float or int): The new data point to be added.
        """
        listTemp = self.data.values.tolist()
        listTemp.append(data_point)
        self.data = pd.Series(listTemp)
        if len(self.data) > self.period:
            self.calculate()
        return
                    
    def get_smavalue(self):
        """
        Returns:
            float: The calculated SMA value.
        """
        return self.sma.iloc[-1]
    
    def plot_show(self):
        """
        Plot the SMA values calculated.
        """
        plt.plot(self.sma_values.values, label='SMA')
        plt.plot(self.data.values, label='Data')
        plt.legend(loc = 'upper left')
        plt.ylabel('SMA Values')
        plt.xlabel
        plt.title('SMA Chart - {} Period'.format(str(self.period)))
        plt.show()
        return
        
    def plot_save(self, filename):
        """
        Save the SMA values calculated to a file.
        """
        plt.plot(self.sma_values.values, label='SMA')
        plt.plot(self.data.values, label='Data')
        plt.legend(loc = 'upper left')
        plt.ylabel('SMA Values')
        plt.xlabel
        plt.title('SMA Chart - {} Period'.format(str(self.period)))
        plt.savefig(filename)
        plt.close()
        return
            
