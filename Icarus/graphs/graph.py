import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

class Graph:
    """
    Graphs the backtest.
    
    Args:
        data (pandas.DataFrame): The data to graph.
        data_length (int): The length of the data.
        ticker (str): The ticker of the stock.
        pct (float): The percent change of the stock.
        hist (list): The history of the account value.
        
    Methods:
        plot: Plots the data.
        plot_bar: Plots the data as a bar graph.
    """
    def __init__(self, data, data_length, ticker, pct, hist, metrics):
        self.data = data
        self.data_length = data_length
        self.ticker = ticker
        self.pct_change = pct
        self.account_value_history = hist
        self.metrics = metrics
        
    def plot(self, save: bool = False, name: str = 'Backtest.png'):
        """
        Plots the data
        
        Args:
            save (bool, optional): Save the plot to a file. Defaults to False.
            name (str, optional): Name of the file to save. Defaults to 'Backtest.png'.
        """
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=False, figsize=(12, 8))
        ax1.grid(color='grey', linestyle='solid')
        ax2.grid(color='grey', linestyle='solid')
        import numpy as np
        x = np.arange(0, self.data_length)
        ax1.set_facecolor('black')
        ax2.set_facecolor('black')
        if self.data['close'][0] > self.data['close'][self.data_length-1]:
            ax1.plot(self.data['close'], label='Stock Close Price', color='red')
        else:
            ax1.plot(self.data['close'], label='Stock Close Price', color='green')
        ax1.set_title('Backtest on {} - From {} - {}'.format(self.ticker, self.data['timestamp'][0], self.data['timestamp'][self.data_length-1]))
        ax1.set_ylabel('Stock Price')
        
        ticks = int(self.data_length/8)
        ax1.set_xticks(x[::ticks],self.data['timestamp'][::ticks].apply(lambda x: x[0:11]))

        ax2.set_xticks(x[::ticks],self.data['timestamp'][::ticks].apply(lambda x: x[0:11]))
        
        ax1.legend(loc='upper left')
        if self.pct_change>0:
            ax2.plot(self.account_value_history, label='Account Value', color='green')
        else:
            ax2.plot(self.account_value_history, label='Account Value', color='red')
        ax2.set_ylabel('Account Value')
        ax2.set_xlabel('Time')
        ax2.legend(loc='upper left')
        
        data = pd.DataFrame(self.metrics, index=['  '+self.ticker+ '  '])
             
        ax3.table(cellText=np.round(data.values,2), colLabels=data.columns,
                  rowLabels=data.index,rowLoc='center',cellLoc='center',loc='top',
                  colWidths=[0.25]*len(data.columns))
            
        # ax3.table(cellText=data.values, colLabels=data.columns, loc='center')
        ax3.axis('off')
        ax3.axis('tight')
        ax3.set_facecolor('black')
        ax3.grid(color='grey', linestyle='solid')
        
        
        fig.tight_layout()
        if save == False:
            plt.show()
            return
        else:
            plt.savefig(name)
            plt.close()
            return
        
    def plot_bar(self, save: bool = False, name: str = 'Backtest.png'):
        """
        Plots the backtest as a bar chart.
        
        Args:
            save (bool): Whether or not to save the plot.
            name (str): The name of the plot.
        """

        x = np.arange(0,self.data_length)
        fig, ax = plt.subplots(1, figsize=(12,6))
        ax.set_title('Backtest on {} - From {} - {}'.format(self.ticker, self.data['timestamp'][0], self.data['timestamp'][self.data_length-1]))

        for idx, val in self.data.iterrows():
            color = '#2CA453'
            if val['open'] > val['close']: color= '#F04730'
            plt.plot([x[idx], x[idx]], [val['low'], val['high']], color=color)
            plt.plot([x[idx], x[idx]-0.1], [val['open'], val['open']], color=color)
            plt.plot([x[idx], x[idx]+0.1], [val['close'], val['close']], color=color)
            
        # ticks
        plt.ylabel('USD')# grid
        ax.xaxis.grid(color='black', linestyle='dashed', which='both', alpha=0.1)# remove spines
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        if save == False:
            plt.show()
            return
        else:
            plt.savefig(name)
            plt.close()
            return