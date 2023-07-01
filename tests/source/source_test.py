import unittest
import Icarus as ic
import pandas as pd

class TestDataMethods(unittest.TestCase):

    def test_csv(self):
        data = ic.source.csv('tests/data/VZ.csv')
        df = pd.read_csv('tests/data/VZ.csv')
        length = len(df)
        self.assertEqual(data.path, 'tests/data/VZ.csv')
        self.assertEqual(data.data_length, length)
        self.assertEqual(data.data['open'][0], df['open'][0])
        self.assertEqual(data.data['open'][length-1], df['open'][length-1])
        self.assertIsInstance(data.data, pd.DataFrame)
        self.assertIsInstance(data.data['open'][0], float)
        
    def test_pandasDF(self):
        df = pd.read_csv('tests/data/VZ.csv')
        length = len(df)
        data = ic.source.PandasDF(df)
        self.assertEqual(data.data_length, length)
        self.assertEqual(data.data['open'][0], df['open'][0])
        self.assertEqual(data.data['open'][length-1], df['open'][length-1])
        self.assertIsInstance(data.data, pd.DataFrame)
        self.assertIsInstance(data.data['open'][0], float)
        

    def test_yFinance(self):
        data = ic.source.yFinance('VZ', '2020-01-01', '2020-01-31')
        self.assertEqual(data.ticker, 'VZ')
        self.assertEqual(data.data_length, 20)
        self.assertIsInstance(data.data, pd.DataFrame)
        self.assertIsInstance(data.data['open'][0], float)

if __name__ == '__main__':
    unittest.main()