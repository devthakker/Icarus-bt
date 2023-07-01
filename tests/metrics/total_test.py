import sys
sys.path.append('../Icarus-BT')
import unittest
import Icarus as ic
import Example as st

class TestTotal(unittest.TestCase):

    def test_sharpe(self):
        data = ic.source.csv('tests/data/VZ.csv')
        strat = st.StrategyExample.BollingerBands()
        riley = ic.Riley()
        riley.set_cash(10000)
        riley.add_data(data)
        riley.set_ticker('VZ')
        riley.set_strategy(strat)
        riley.set_stake_quantity(50)
        name = 'totalreturn'
        riley.add_metric(ic.metrics.TotalReturn, name)
        data = riley.run()
        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['Metrics'], dict)
        total = 7.827099999999991
        self.assertIsInstance(data['Metrics']["total_return"], float)
        self.assertEqual(data['Metrics']["total_return"], total)
        
        
if __name__ == '__main__':
    unittest.main()
        