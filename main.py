from trading.traditional_strategies import *
from trading.ai_strategies import *
from trading.trader import *

if __name__ == "__main__":

    ## Initialize the AITrader
    trader = AITrader(start_date="2019-01-01", end_date="2021-01-01")

    # Set your desired strategy; for example, using the BuyHoldStrategy
    trader.add_strategy(MLTradingStrategy, params={'model_name': 'Logistic_Regression'},)

    # Run the backtest
    trader.run(1, stock_ticker="AAPL")

    # Plot the results
    trader.plot()