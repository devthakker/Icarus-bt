import sys
sys.path.append('../Icarus-BT')
import Icarus as bt
import strategy as st


# Create an instance of Riley
riley = bt.Riley()
riley.set_cash(10000)
data = bt.source.csv('HistoricalData/F.csv')
# data = bt.source.PandasDF(data.data)
# data = bt.source.yFinance('F', '2020-01-01', '2020-12-31')
riley.add_data(data)
riley.set_ticker('F')
riley.set_strategy(st.BollingerBands())
riley.set_stake_quantity(50)
# riley.set_stake_percentage(100)
# riley.set_stake_dollars(1000)
riley.add_metric(bt.metrics.SharpeRatio, 'sharpe')
riley.add_metric(bt.metrics.SortinoRatio, 'sortino')
riley.add_metric(bt.metrics.MaxDrawdown, 'maxdrawdown')
riley.add_metric(bt.metrics.CalmarRatio, 'calmar')
riley.run()
riley.plot()
# riley.plot_bar()