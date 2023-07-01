import sys
sys.path.append('../Icarus-BT')
import unittest
import Icarus as ic
import Example as st

class TestMaxDrawdown(unittest.TestCase):

    def test_sharpe(self):
        data = ic.source.csv('tests/data/VZ.csv')
        strat = st.StrategyExample.BollingerBands()
        riley = ic.Riley()
        riley.set_cash(10000)
        riley.add_data(data)
        riley.set_ticker('VZ')
        riley.set_strategy(strat)
        riley.set_stake_quantity(50)
        name = 'maxdrawdown'
        riley.add_metric(ic.metrics.MaxDrawdown, name)
        data = riley.run()
        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['Metrics'], dict)
        maxReturn = 0.03290364943656383
        self.assertIsInstance(data['Metrics']["max_drawdown"], float)
        self.assertEqual(data['Metrics']["max_drawdown"], maxReturn)
        
        
if __name__ == '__main__':
    unittest.main()
        