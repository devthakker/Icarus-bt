from riley import Riley
import sys
sys.path.append('../Back-Testing')
from strategy import BollingerBands

# Create an instance of Riley
riley = Riley()
riley.set_cash(10000)
riley.add_data_csv('HistoricalData/F.csv')
riley.set_strategy(BollingerBands(20,1,2,2))
riley.set_stake_quantity(5)
riley.run()