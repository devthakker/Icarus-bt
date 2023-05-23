from heapq import nlargest
import sys
sys.path.append('../Back-Testing')
import pandas as pd
from talipp.indicators import *
from indicators.OHLCV import *
import matplotlib.pyplot as plt

import os 

# files = os.listdir('HistoricalData')
# files = [file.split('.')[0] for file in files]

results = {}

files = ['F','AAPL', 'AAL']

for file in files:

    df = pd.read_csv("HistoricalData/{}.csv".format(file))

    count = 0
    BOL_ONE = BB(20, 2)
    BOL_TWO = BB(20, 3)
    ADX_ONE = ADX(14,20)
    RSI_ONE = RSI(14)
    cash = 10000

    account_value = 0

    account_value_history = []

    iterations = []

    CURRENT_POSITION = {'shares': 0, 'price': 0}

    startDate = df['timestamp'][0]
    endDate = df['timestamp'][len(df)-1]

    for line in df.iterrows():
        
        ohlc = {'open': line[1]['open'], 'high': line[1]['high'], 'low': line[1]['low'], 'close': line[1]['close'], 'volume': line[1]['volume'], 'time': line[1]['timestamp']}
        BOL_ONE.add_input_value(ohlc['close'])
        BOL_TWO.add_input_value(ohlc['close'])
        dict = ohlcv_from_dict(ohlc)
        ADX_ONE.add_input_value(dict)
        RSI_ONE.add_input_value(ohlc['close'])
        if BOL_ONE.has_output_value() and BOL_TWO.has_output_value() and RSI_ONE.has_output_value() and count > 25:
            if ohlc['close'] < BOL_ONE[-1].lb and ohlc['close'] > BOL_TWO[-1].lb: # and (ADX_ONE[-1].adx) > 15 and RSI_ONE[-1] < 90 and ADX_ONE[-1].plus_di > ADX_ONE[-1].minus_di:
                if CURRENT_POSITION['shares'] > 0:
                    continue
                else:
                    # print("Cash: {}".format(round(cash,2)))
                    # print("BUY, {} shares at ${} {}".format(int((cash/10)/ohlc['close']), ohlc['close'], ohlc['time']))
                    # print("BOL_ONE: {}, BOL_TWO: {}, ADX: {}, RSI: {}".format(round(BOL_ONE[-1].lb,2), round(BOL_TWO[-1].lb,2), round(ADX[-1].adx,2), round(RSI[-1],2)))
                    shares = int((cash/10)/ohlc['close'])
                    cash -= ohlc['close']*shares
                    CURRENT_POSITION['shares'] = shares
                    CURRENT_POSITION['price'] = ohlc['close']
            elif ohlc['close'] > BOL_ONE[-1].ub and ohlc['close'] < BOL_TWO[-1].ub:
                if CURRENT_POSITION['shares'] > 0:
                    # print("SELL, {} shares at ${} {}".format(CURRENT_POSITION['shares'], ohlc['close'], ohlc['time']))
                    # print("BOL_ONE: {}, BOL_TWO: {}, ADX: {}, RSI: {}".format(round(BOL_ONE[-1].ub,2), round(BOL_TWO[-1].ub,2), round(ADX[-1].adx,2), round(RSI[-1],2)))
                    cash += ohlc['close']*CURRENT_POSITION['shares']
                    CURRENT_POSITION['shares'] = 0
                    CURRENT_POSITION['price'] = 0
                    # print("Cash: {}".format(round(cash,2)))
            # if CURRENT_POSITION['shares'] > 0:
            #     print("HOLD, {} shares at ${} {}".format(CURRENT_POSITION['shares'], ohlc['close'], ohlc['time']))
            # else:
            #     print("No Position Cash: {}".format(round(cash,2)))
                
        account_value = cash + CURRENT_POSITION['shares']*ohlc['close']
        
        account_value_history.append(account_value)
        
        # print("Account Value: {}".format(round(account_value,2)))
        
        iterations.append(count)
        count += 1
        
    # print(count)
        
    if CURRENT_POSITION['shares'] > 0:
        cash += CURRENT_POSITION['shares']*CURRENT_POSITION['price']
        account_value = cash
        # account_value_history.append(account_value)
        
    percent_change = ((account_value - 10000)/10000)*100
    
    results[file] = percent_change
        
    plt.plot(iterations, account_value_history)
    plt.xlabel('{} - {}'.format(startDate, endDate))
    plt.ylabel('Account Value')
    plt.title("{} Backtest".format(file))
    plt.savefig('BackTestResults/{}.png'.format(file))
    plt.clf()
        
    print("Final Cash: {} - {}".format(round(cash,2), file))
    
# res = nlargest(20, results, key=results.get)
# print(res)
