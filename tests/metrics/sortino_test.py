import sys
sys.path.append('../Icarus-BT')
import unittest
import Icarus as ic
import Example as st

class TestSortino(unittest.TestCase):

    def test_sharpe(self):
        data = ic.source.csv('tests/data/VZ.csv')
        strat = st.StrategyExample.BollingerBands()
        riley = ic.Riley()
        riley.set_cash(10000)
        riley.add_data(data)
        riley.set_ticker('VZ')
        riley.set_strategy(strat)
        riley.set_stake_quantity(50)
        name = 'sortino'
        riley.add_metric(ic.metrics.SortinoRatio, name)
        data = riley.run()
        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['Metrics'], dict)
        sortino = 0.008149839664628783
        self.assertIsInstance(data['Metrics'][name], float)
        self.assertEqual(data['Metrics'][name], sortino)
        
        
if __name__ == '__main__':
    unittest.main()
        