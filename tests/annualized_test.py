import sys
sys.path.append('../Icarus-BT')
import unittest
import Icarus as ic
import Example as st

class TestAnnualizedReturn(unittest.TestCase):

    def test_sharpe(self):
        data = ic.source.csv('tests/data/VZ.csv')
        strat = st.StrategyExample.BollingerBands()
        riley = ic.Riley()
        riley.set_cash(10000)
        riley.add_data(data)
        riley.set_ticker('VZ')
        riley.set_strategy(strat)
        riley.set_stake_quantity(50)
        name = 'annualreturn'
        riley.add_metric(ic.metrics.AnnualizedReturn, name)
        data = riley.run()
        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['Metrics'], dict)
        anReturn = 0.04548320562535646
        self.assertIsInstance(data['Metrics'][name], float)
        self.assertEqual(data['Metrics'][name], anReturn)
        
        
if __name__ == '__main__':
    unittest.main()
        