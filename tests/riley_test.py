import sys
sys.path.append('../Icarus-BT')
import Icarus as ic
import strategy as st


# Create an instance of the BacktestEngine
riley = ic.Riley()

# Set Cash Amount
riley.set_cash(10000)

# Fetch data chosen source
data = ic.source.csv('HistoricalData/F.csv')

# Alternatively, pull data from Yahoo Finance
# Also, you can specify the start and end dates

# data = bt.source.PandasDF(data.data)
# data = bt.source.yFinance('F', '2020-01-01', '2020-12-31')

# Add data to the backtest engine
riley.add_data(data)

# Set the ticker for the backtest
riley.set_ticker('F')

#Add the strategy class
riley.set_strategy(st.BollingerBands())

# Set the stake amount
riley.set_stake_quantity(50)

# Alternatively, you can set the stake percentage or the stake dollars
# riley.set_stake_percentage(100)
# riley.set_stake_dollars(1000)

# Add metrics to the backtest engine
riley.add_metric(ic.metrics.SharpeRatio, 'sharpe')
riley.add_metric(ic.metrics.SortinoRatio, 'sortino')

# Run the backtest
riley.run()

# Generate graphical representation of the backtest results
riley.plot()
# riley.plot_bar()