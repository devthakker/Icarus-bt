import sys
sys.path.append('../QUANT2023')
from talipp.indicators import CCI
from talipp.ohlcv import OHLCVFactory


def ohlcv_from_df(bar):
    df = bar.df
    open = list(df['open'])
    high = list(df['high'])
    low = list(df['low'])
    close = list(df['close'])
    volume = list(df['volume'])
    values = {'open': open, 'high': high, 'low': low, 'close': close, 'volume': volume}
    return OHLCVFactory.from_dict(values)



def ohlcv_from_bar(bar):
    open = [bar.open]
    high = [bar.high]
    low = [bar.low]
    close = [bar.close]
    volume = [bar.volume]
    values = {'open': open, 'high': high, 'low': low, 'close': close, 'volume': volume}
    return OHLCVFactory.from_dict(values)


def ohlcv_from_dict(dict):
    open = [dict['open']]
    high = [dict['high']]
    low = [dict['low']]
    close = [dict['close']]
    volume = [dict['volume']]
    values = {'open': open, 'high': high, 'low': low, 'close': close, 'volume': volume}
    return OHLCVFactory.from_dict(values)


