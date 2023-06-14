from heapq import nlargest
import sys
sys.path.append('../Back-Testing')
import pandas as pd
from talipp.indicators import *
from indicators.OHLCV import *
import matplotlib.pyplot as plt

import os 

files = os.listdir('HistoricalData')
files = [file.split('.')[0] for file in files]

results = {}

# files = ['F','AAPL', 'AAL']

#Iterate through all files in HistoricalData folder
for file in files:

    #Read in CSV file to pandas dataframe
    df = pd.read_csv("HistoricalData/{}.csv".format(file))

    #Count how many rows are in the dataframe
    count = 0
    
    #Create indicators
    BOL_ONE = BB(20, 2)
    BOL_TWO = BB(20, 3)
    ADX_ONE = ADX(14,20)
    RSI_ONE = RSI(14)
    
    #Set initial cash value
    cash = 10000

    #Set initial account value
    account_value = 0

    #Create list to store account value history
    account_value_history = []

    #Create list to store iterations
    iterations = []

    #Create dictionary to store current position
    CURRENT_POSITION = {'shares': 0, 'price': 0}

    #Set start and end dates
    startDate = df['timestamp'][0]
    endDate = df['timestamp'][len(df)-1]

    #Iterate through each row in the dataframe
    for line in df.iterrows():
        
        #Create dictionary from row
        ohlc = {'open': line[1]['open'], 'high': line[1]['high'], 'low': line[1]['low'], 'close': line[1]['close'], 'volume': line[1]['volume'], 'time': line[1]['timestamp']}
        
        # Add input values to indicators
        BOL_ONE.add_input_value(ohlc['close'])
        BOL_TWO.add_input_value(ohlc['close'])
        dict = ohlcv_from_dict(ohlc)
        ADX_ONE.add_input_value(dict)
        RSI_ONE.add_input_value(ohlc['close'])
        
        # Check if indicators have output values
        if BOL_ONE.has_output_value() and BOL_TWO.has_output_value() and RSI_ONE.has_output_value() and count > 25:
            #Check for buy and sell signals
            if ohlc['close'] < BOL_ONE[-1].lb and ohlc['close'] > BOL_TWO[-1].lb: # and (ADX_ONE[-1].adx) > 15 and RSI_ONE[-1] < 90 and ADX_ONE[-1].plus_di > ADX_ONE[-1].minus_di:
                # Check if we already have a position and continue if we do
                if CURRENT_POSITION['shares'] > 0:
                    continue
                else:
                    # print("Cash: {}".format(round(cash,2)))
                    # print("BUY, {} shares at ${} {}".format(int((cash/10)/ohlc['close']), ohlc['close'], ohlc['time']))
                    # print("BOL_ONE: {}, BOL_TWO: {}, ADX: {}, RSI: {}".format(round(BOL_ONE[-1].lb,2), round(BOL_TWO[-1].lb,2), round(ADX[-1].adx,2), round(RSI[-1],2)))
                    shares = int((cash/3)/ohlc['close'])
                    cash -= ohlc['close']*shares
                    CURRENT_POSITION['shares'] = shares
                    CURRENT_POSITION['price'] = ohlc['close']
                    
            # Check for sell signal
            if ohlc['close'] > BOL_ONE[-1].ub and ohlc['close'] < BOL_TWO[-1].ub:
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
            
        # Calculate account value    
        account_value = cash + CURRENT_POSITION['shares']*ohlc['close']
        
        # Add account value to account value history
        account_value_history.append(account_value)
        
        # print("Account Value: {}".format(round(account_value,2)))
        
        # Add iteration to iterations list
        iterations.append(count)
        count += 1
        
    # print(count)
        
    # Check if we have a position at the end of the backtest
    if CURRENT_POSITION['shares'] > 0:
        cash += CURRENT_POSITION['shares']*CURRENT_POSITION['price']
        account_value = cash
        # account_value_history.append(account_value)
        
    # Calculate percent change
    percent_change = ((account_value - 10000)/10000)*100
    
    results[file] = round(percent_change,3)
        
    plt.plot(iterations, account_value_history)
    plt.xlabel('{} - {}'.format(startDate, endDate))
    plt.ylabel('Account Value')
    plt.title("{} Backtest".format(file))
    plt.savefig('BackTestResults/{}.png'.format(file))
    plt.clf()
        
    print("Final Cash: ${} - {}".format(round(cash,2), file))
    
# res = nlargest(20, results, key=results.get)
print(results)
