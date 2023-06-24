from setuptools import setup, find_packages


# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='icarus-bt',
    version='0.2.1',
    description='A backtesting framework for algorithmic trading',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'yfinance', 'pandas', 'tqdm', 'mplfinance'],
    author='Devin Thakker',
    author_email='devin.thakker@outlook.com',
    url='https://github.com/devthaakker/icarus-bt',
    license='MIT',
    download_url='https://github.com/devthakker/Icarus-bt/archive/refs/tags/v0.2.1.tar.gz',
    keywords=['backtesting', 'trading', 'algorithmic trading', 'finance', 'stock market', 'stock', 'market', 'backtest', 'backtesting framework', 'backtesting library', 'backtesting tool', 'backtesting software', 'backtesting python', 'backtesting python library', 'backtesting python framework', 'backtesting python tool', 'backtesting python software', 'backtesting python library finance', 'backtesting python framework finance', 'backtesting python tool finance', 'backtesting python software finance', 'backtesting python library stock market', 'backtesting python framework stock market', 'backtesting python tool stock market', 'backtesting python software stock market'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    python_requires='>=3.10'
)