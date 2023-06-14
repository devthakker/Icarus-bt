
# ICARUS-BT

![ICARUS-BT](./preview.jpg?raw=true)

# Riley: Backtesting Engine for Trading Strategies

## Overview
Icarus is a Python package designed to facilitate the backtesting of trading strategies. It provides a framework to simulate and evaluate trading decisions based on historical data, calculate various performance metrics, and generate graphical representations of the results. Riley is equipped with features to compute metrics like Sharpe ratio and Sortino ratio, allowing traders and quantitative analysts to assess the risk-adjusted returns of their strategies.

## Features
1. Backtesting: Riley enables users to simulate the execution of trading strategies on historical data. It supports various order types, including market orders, limit orders, and stop orders, allowing for flexible trade execution scenarios.

2. Performance Metrics: The package includes functions to calculate essential performance metrics commonly used in financial analysis. These metrics include but are not limited to the following:
   - Sharpe Ratio: Measures the risk-adjusted return of a strategy.
   - Sortino Ratio: Similar to Sharpe Ratio, but focuses on downside risk.
   - Maximum Drawdown: Determines the largest peak-to-trough decline in strategy value.
   - Calmar Ratio: Measures the risk-adjusted return of a strategy relative to its maximum drawdown.
   - Annualized Returns: Calculates the compounded annual growth rate of the strategy.
   - Total Return: Computes the overall return of the strategy.

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
from riley import BacktestEngine
import yfinance as yf

# Create an instance of the BacktestEngine
backtester = BacktestEngine()

# Fetch historical price data from Yahoo Finance
symbol = "AAPL"  # Replace with your desired symbol
data = yf.download(symbol, start="2010-01-01", end="2023-06-11")
backtester.set_data(data)

# Alternatively, read data from a CSV file
# data = pd.read_csv("path/to/data.csv")
# backtester.set_data(data)

# Define your trading strategy
strategy = ...  # Implement your trading strategy here

# Run the backtest using the strategy
backtester.run_backtest(strategy)

# Calculate performance metrics
sharpe_ratio = backtester.calculate_sharpe_ratio()
sortino_ratio = backtester.calculate_sortino_ratio()

# Generate graphical representation of the backtest results
backtester.plot_results()
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
