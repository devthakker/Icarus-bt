import sys
sys.path.append('../Icarus-BT')
import unittest
import Icarus as ic
import Example as st

class TestCalmar(unittest.TestCase):

    def test_calmar(self):
        data = ic.source.csv('tests/data/VZ.csv')
        strat = st.StrategyExample.BollingerBands()
        riley = ic.Riley()
        riley.set_cash(10000)
        riley.add_data(data)
        riley.set_ticker('VZ')
        riley.set_strategy(strat)
        riley.set_stake_quantity(50)
        name = 'calmar'
        riley.add_metric(ic.metrics.CalmarRatio, name)
        data = riley.run()
        self.assertIsInstance(data, dict)
        self.assertIsInstance(data['Metrics'], dict)
        calmar = 1.3823149226363243
        self.assertIsInstance(data['Metrics'][name], float)
        self.assertEqual(data['Metrics'][name], calmar)
        
        
if __name__ == '__main__':
    unittest.main()
        