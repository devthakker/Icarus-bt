import sys
sys.path.append('../Icarus-BT')
import Icarus as ic
import StrategyExample as st


# Create an instance of the BacktestEngine
riley = ic.Riley()

# Set Cash Amount
riley.set_cash(10000)

# Fetch data chosen source
data = ic.source.csv('SampleData/F.csv')

# Alternatively, pull data from Yahoo Finance
# Also, you can specify the start and end dates

# data = ic.source.PandasDF(data.data)
# data = ic.source.yFinance('F', '2020-01-01', '2020-12-31')

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
riley.add_metric(ic.metrics.MaxDrawdown, 'maxdrawdown')
# riley.add_metric(ic.metrics.CalmarRatio, 'calmar')
riley.add_metric(ic.metrics.AnnualizedReturn, 'annualreturn')
# riley.add_metric(ic.metrics.TotalReturn, 'totalreturn')

# Run the backtest
riley.run()

# Generate graphical representation of the backtest results
riley.plot()
# riley.plot_bar(True, 'Backtestbar.png')