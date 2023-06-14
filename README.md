
# ICARUS-BT

![ICARUS-BT](./preview.jpg?raw=true)

# Riley: Backtesting Engine for Trading Strategies

[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/release/python-370/)
[![PyPI](https://img.shields.io/pypi/v/icarus-bt?color=blue)](https://pypi.org/project/icarus-bt/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/icarus-bt?color=blue)](https://img.shields.io/github/downloads/devthakker/icarus-bt/total.svg)
![GitHub](https://img.shields.io/pypi/l/icarus-bt?color=blue)

## Overview
Icarus is a Python package designed to facilitate the backtesting of trading strategies. It provides a framework to simulate and evaluate trading decisions based on historical data, calculate various performance metrics, and generate graphical representations of the results. Riley is equipped with features to compute metrics like Sharpe ratio and Sortino ratio, allowing traders and quantitative analysts to assess the risk-adjusted returns of their strategies.

## Features
1. Backtesting: Riley enables users to simulate the execution of trading strategies on historical data. It supports various order types, including market orders, limit orders, and stop orders, allowing for flexible trade execution scenarios.

2. Performance Metrics: The package includes functions to calculate essential performance metrics commonly used in financial analysis. These metrics include but are not limited to the following:
   - [Sharpe Ratio: Measures the risk-adjusted return of a strategy.](https://www.investopedia.com/terms/s/sharperatio.asp)
   - [Sortino Ratio: Similar to Sharpe Ratio, but focuses on downside risk.](https://www.investopedia.com/terms/s/sortinoratio.asp)
   - [Maximum Drawdown: Determines the largest peak-to-trough decline in strategy value.](https://www.investopedia.com/terms/m/maximum-drawdown-mdd.asp)
   - [Calmar Ratio: Measures the risk-adjusted return of a strategy relative to its maximum drawdown.](https://www.investopedia.com/terms/c/calmarratio.asp)
   - [Annualized Returns: Calculates the compounded annual growth rate of the strategy.](https://www.investopedia.com/terms/a/annualized-total-return.asp)
   - [Total Return: Computes the overall return of the strategy.](https://www.investopedia.com/terms/t/totalreturn.asp)

3. Data Sources: Icarus provides support for multiple data sources, including Yahoo Finance (via `yfinance`) and CSV files. This allows users to easily fetch historical price data or load data from their own sources.

4. Graphical Representation: Riley provides capabilities to generate graphical representations of backtesting results. This includes visualizations of strategy performance, equity curves, trade signals, and other relevant data.

## Installation
To install Icarus, follow these steps:

1. Ensure that you have Python 3.7 or above installed on your system.
2. Open a terminal or command prompt.
3. Run the following command to install Riley using pip:

```python
pip install ICARUS-BT
```

## Getting Started
To begin using Icarus for backtesting trading strategies, follow the example below:

```python
import Icarus as ic
import strategy as st


# Create an instance of the BacktestEngine
riley = ic.Riley()

# Set Cash Amount
riley.set_cash(10000)

# Fetch data chosen source
data = ic.source.csv('HistoricalData/F.csv')

# Alternatively, pull data from Yahoo Finance
# Also, you can specify the start and end dates

# data = bt.source.PandasDF(data.data)
# data = bt.source.yFinance('F', '2020-01-01', '2020-12-31')

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

# Run the backtest
riley.run()

# Generate graphical representation of the backtest results
riley.plot()
# riley.plot_bar()
```

## Documentation
For more information on how to use Riley, please refer to the [documentation](https://icarus-bt.readthedocs.io/en/latest/).

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Icarus is an open-source project, and contributions are welcome. If you find any issues, have suggestions for improvements, or would like to add new features, please submit a pull request on the GitHub repository.

## Contact
If you have any questions, suggestions, or feedback, feel free to reach out to the development team at dthakker@gmail.com

We hope Icarus proves to be a valuable tool for backtesting and evaluating your trading strategies. Happy trading!
