from riley import Riley

from strategy import BollingerBands
import metrics

# Create an instance of Riley
riley = Riley()
riley.set_cash(10000)
riley.add_data_csv('HistoricalData/F.csv')
riley.set_ticker('F')
riley.set_strategy(BollingerBands())
riley.set_stake_quantity(50)
riley.add_metric(metrics.sharperatio)
riley.run()

# riley.plot()