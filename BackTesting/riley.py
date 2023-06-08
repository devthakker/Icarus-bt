import pandas as pd

class Riley:
    
    def __init__(self, optimization=False) -> None:
        self.optimization = optimization
        self.cash = None
        self.strategy = None
        self.data = None
        
    def set_cash(self, cash):
        self.cash = cash
        return
    
    def set_strategy(self, strategy):
        self.strategy = strategy
        return
    
    def add_data_dataframe(self, data):
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
        else:
            raise Exception('Data must be a pandas dataframe')
        return
    
    def add_data_csv(self, path):
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
        else:
            raise Exception('Path is invalid')
        return
    
    