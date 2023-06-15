import pandas as pd
import yfinance as yf

class csv:
    """
    CSV data source class
    """
    def __init__(self, path: str):
        self.path = path
        if isinstance(path, str):
            df = pd.read_csv(path)
            if 'open' not in df.columns:
                raise Exception('Data must contain an open column')
            if 'high' not in df.columns:
                raise Exception('Data must contain a high column')
            if 'low' not in df.columns:
                raise Exception('Data must contain a low column')
            if 'close' not in df.columns:
                raise Exception('Data must contain a close column')
            self.data = df
            self.data_length = len(df)
        else:
            raise Exception('Path is invalid')
        
class PandasDF:
    """
    Pandas dataframe data source class
    """
    def __init__(self, data: pd.DataFrame):
        if isinstance(data, pd.DataFrame):
            df = pd.DataFrame(data)
            if 'open' not in df.columns:
                raise Exception('Data must contain an open column')
            if 'high' not in df.columns:
                raise Exception('Data must contain a high column')
            if 'low' not in df.columns:
                raise Exception('Data must contain a low column')
            if 'close' not in df.columns:
                raise Exception('Data must contain a close column')
            self.data = df
            self.data_length = len(df)
        else:
            raise Exception('Data must be a pandas dataframe')
        return
 

class yFinance:
    """
    yFinance data source class
    """
    def __init__(self, ticker: str, start: str, end: str, interval: str='1d'):
        """
        Adds data to back instance of Riley with a csv file.
        
        Args:
            ticker (str): The ticker of the stock to get data for.
            start (str): The start date of the data.
            end (str): The end date of the data.
            interval (str): The interval of the data.
            Options for interval are 1d, 5d, 1wk, 1mo, 3mo
        """
        self.ticker = ticker
        self.interval = interval
        self.data = None
        self.data_length = None
        self.start = start
        self.end = end
        self._get_data()
    
    def _get_data(self):
        ticker = yf.Ticker(self.ticker)
        
        df = ticker.history(ticker, start=self.start, end=self.end, interval=self.interval)
        
        df.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'}, inplace=True)
        df["timestamp"] = df.index
        df["timestamp"] = df["timestamp"].apply(lambda x: str(x.date()))
        df.drop(columns=['Dividends', 'Stock Splits'], inplace=True)
        
        self.data = df
        self.data_length = len(df)